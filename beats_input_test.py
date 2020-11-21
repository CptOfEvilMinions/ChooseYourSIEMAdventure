from pylogbeat import PyLogBeatClient
import datetime
import argparse
import json

def send_log(host, port, message):
  # Generate test log event
  message = {
    "@timestamp": datetime.datetime.utcnow().replace(tzinfo=datetime.timezone.utc).isoformat(),
    "@version": "1",
    "host": "my-local-host",
    "level": "INFO",
    "logsource": "my-local-host",
    "message": "foo bar",
    "pid": 65534,
    "program": "example.py",
    "type": "python-logstash"
  }
  
  # Create connector
  client = PyLogBeatClient(host, port, ssl_enable=True, ssl_verify=False)

  # Connect to server, send log message, and close connection
  client.connect()
  client.send([message])
  client.close()

  print ("Log sent")

if __name__ == "__main__":
  my_parser = argparse.ArgumentParser()
  my_parser.add_argument('--host', type=str, required=True, help='Specify Logstash FQDN or IP address')
  my_parser.add_argument('-p','--port', type=int, default=5044, help='Specify Logstash port')
  my_parser.add_argument('-m','--message', type=str, default='hello world', help='Specify log message/payload')
  args = my_parser.parse_args()

  send_log(args.host, args.port, args.message)