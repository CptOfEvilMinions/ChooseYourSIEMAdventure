from datetime import datetime, date, timezone
from requests.auth import HTTPBasicAuth
from pylogbeat import PyLogBeatClient
import argparse
import requests
import json
import time
import sys
import string
import random
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class SIEM:
  def __init__(self, host, port, platform, ingest_port, siem_username, siem_password, retries):
    self.host = host
    self.port = port
    self.siem_username = siem_username
    self.siem_password = siem_password
    self.platform = platform
    self.ingest_port = ingest_port
    self.retries = retries
    self.random_message = self.generate_random_message()

  def generate_random_message(self):
    """
    Generate random message
    """
    random_message = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(64))
    print (f"[+] - {datetime.now()} - Generated random message: {random_message}")  
    return random_message


def send_log(siem):
  """
  Send randomly generated message
  """
  # Generate test log event
  message = {
    "@timestamp": datetime.utcnow().replace(tzinfo=timezone.utc).isoformat(),
    "@version": "1",
    "host": "my-local-host",
    "level": "INFO",
    "logsource": "my-local-host",
    "message": siem.random_message,
    "pid": 65534,
    "program": "example.py",
    "service": {
      "type": "test"
    }
  }
  print (message)
  
  # Create connector
  client = PyLogBeatClient(siem.host, siem.ingest_port, ssl_enable=True, ssl_verify=False)

  try:
    # Connect to server, send log message, and close connection
    client.connect()
    client.send([message])
    client.close()
    print (f"[+] - {datetime.now()} - Sucessfully sent random message to {siem.platform} - {siem.host}:{siem.port}") 
    return True , None
  except Exception as e:
    return False, e


def check_graylog(siem):
  """
  """
  headers ={
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'X-Requested-By': 'cli'
  }

  # Generate URL
  url = f"https://{siem.host}:{siem.port}/api/search/universal/relative?query={siem.random_message}&range=3600&limit=100&sort=timestamp:desc&pretty=true"

  for i in range(0, siem.retries):
    result = requests.get(url=url, headers=headers, auth=HTTPBasicAuth(siem.siem_username, siem.siem_password), verify=False).json()
    if len(result['messages']) > 0:
      return True
    time.sleep(3)

  return False


def check_elasticsearch(siem):
  """
  """
  search_dict = {
    "query": {
      "match": {
        "message": siem.random_message
      }
    }
  }
  
  indice_name = f"python-logstash-{str(datetime.utcnow().date()).replace('-','.')}"
  url = f"http://{siem.host}:{siem.port}/{indice_name}/_search"

  for i in range(0, siem.retries):
    result = requests.get(url=url, json=search_dict, auth=HTTPBasicAuth(siem.siem_username, siem.siem_password), verify=False).json()
    if int(result['hits']['total']['value']) > 0:
      return True
    time.sleep(3)

  return False


def check_splunk(siem):  
  """
  """
  #### Get session key ####
  session_key = requests.get(
    url = f"https://{siem.host}:{siem.port}/servicesNS/admin/search/auth/login", 
    data={'username': siem.siem_username,'password': siem.siem_password, "output_mode": "json"}, 
    verify=False
  ).json()['sessionKey']
  print ("[+] - Obtained session key")

  
  search_query = f"search index=main AND \"{siem.random_message}\""
  for i in range(0, siem.retries):
    #### Create search job ####
    sid = requests.post(url=f"https://{siem.host}:{siem.port}/services/search/jobs/", 
      data={ "search": search_query, "output_mode": "json"}, 
	    headers = { 'Authorization': ('Splunk %s' %session_key)},
	    verify = False
    ).json()['sid']
    print (f"[+] - Splunk search job id: {sid}")
    
    #### Wait for search job to finish ####
    done = False
    while not done:
      r = requests.get(url=f"https://{siem.host}:{siem.port}/services/search/jobs/{sid}",
        headers = { 'Authorization': (f"Splunk {session_key}")},
        data={"output_mode": "json"},
        verify = False
      )

      if r.json()['entry'][0]['content']['isDone'] == True:
        done = True
      else:
        time.sleep(1)

    #### Get results from job search ####
    r = requests.get(url=f"https://{siem.host}:{siem.port}/services/search/jobs/{sid}/results/",
      headers = { 'Authorization': (f"Splunk {session_key}")},
      data={'output_mode': 'json'},
      verify = False
    )


    for result in r.json()['results']:
      if result['_raw'] == siem.random_message:
        return True
    time.sleep(3)
  return False


if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument('--host', type=str, required=True, help='Specify server FQDN or IP address')
  parser.add_argument('--api_port', type=int, default=443, help='WebGUI port')
  parser.add_argument('--retries', type=int, default=10, help='Number of times to retry query')
  parser.add_argument('--ingest_port', type=int, default=5044, help='Specify port to ingest logs')
  parser.add_argument('--platform', type=str, required=True, choices=['elastic','graylog','splunk'], help='Specify SIEM platform')
  parser.add_argument('--siem_username', type=str, default='admin', help='SIEM username')
  parser.add_argument('--siem_password', type=str, default='Changeme123!', help='SIEM password')
  args = parser.parse_args()
 
  # Create SIEM object
  siem = siem = SIEM(args.host, args.api_port, args.platform, args.ingest_port, args.siem_username, args.siem_password, args.retries)

  # Send random message
  result, err = send_log(siem)
  if err != None:
    print (f"[-] - {datetime.now()} - Failed to send random message to {siem.platform} - {siem.host}:{siem.ingest_port}") 

  # Query for random message
  if siem.platform == 'elastic' and check_elasticsearch(siem):
    print (f"[+] - {datetime.now()} - Random message: {siem.random_message} ingested in {siem.platform}")
  elif siem.platform == 'graylog' and check_graylog(siem):
    print (f"[+] - {datetime.now()} - Random message: {siem.random_message} ingested in {siem.platform}")
  elif siem.platform == 'splunk'and check_splunk(siem):
    print (f"[+] - {datetime.now()} - Random message: {siem.random_message} ingested in {siem.platform}")
  else:
    print ("Failed")
