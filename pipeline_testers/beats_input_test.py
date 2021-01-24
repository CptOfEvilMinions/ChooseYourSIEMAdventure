from requests.auth import HTTPBasicAuth
from pylogbeat import PyLogBeatClient
from datetime import datetime, date, timezone
import argparse
import requests
import json
import time
import sys
import string
import random

def check_elasticsearch(es_host, es_port, es_username, es_password, retries, random_message):
  """
  """
  search_dict = {
    "query": {
      "match": {
        "message": random_message
      }
    }
  }
  
  indice_name = f"python-logstash-{str(date.today()).replace('-','.')}"
  url = f"http://{es_host}:{es_port}/{indice_name}/_search"

  for i in range(0, retries):
    result = requests.get(url=url, json=search_dict, auth=HTTPBasicAuth(es_username, es_password)).json()
    if int(result['hits']['total']['value']) > 0:
      return True
    time.sleep(3)

  return False


def send_log(host, port, message):
  # Generate random string
  random_message = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(64))
  print (f"Random message: {random_message}")

  # Generate test log event
  message = {
    "@timestamp": datetime.utcnow().replace(tzinfo=timezone.utc).isoformat(),
    "@version": "1",
    "host": "my-local-host",
    "level": "INFO",
    "logsource": "my-local-host",
    "message": random_message,
    "pid": 65534,
    "program": "example.py",
    "service": {
      "type": "python-logstash"
    }
  }
  
  # Create connector
  client = PyLogBeatClient(host, port, ssl_enable=True, ssl_verify=False)

  # Connect to server, send log message, and close connection
  client.connect()
  client.send([message])
  client.close()

  print ("Log sent")
  return random_message

if __name__ == "__main__":
  my_parser = argparse.ArgumentParser()
  my_parser.add_argument('--host', type=str, required=True, help='Specify Logstash FQDN or IP address')
  my_parser.add_argument('-p','--port', type=int, default=5044, help='Specify Logstash port')
  my_parser.add_argument('-m','--message', type=str, default='hello world', help='Specify log message/payload')
  my_parser.add_argument('-r','--retries', type=int, default=10, help='Number of times to retry query')
  my_parser.add_argument('--es_username', type=str, default='elastic', help='Elasticsearch username')
  my_parser.add_argument('--es_password', type=str, default='Changeme123!', help='Elasticsearch password')
  my_parser.add_argument('--es_port', type=int, default=9200, help='Elasticsearch port')
  args = my_parser.parse_args()

  # Generate random message and send it
  random_message = send_log(args.host, args.port, args.message)

  # Query for random message
  if check_elasticsearch(args.host, args.es_port, args.es_username, args.es_password, args.retries, random_message):
    print (f"[+] - {datetime.now()} - Random message: {random_message} ingested")
  else:
    sys.exit(f"[-] - {datetime.now()} - Random message: {random_message} NOT found in python-logstash-{str(date.today()).replace('-','.')} indice")
