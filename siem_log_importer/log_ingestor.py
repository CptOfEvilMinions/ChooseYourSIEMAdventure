from elasticsearch import Elasticsearch
from pylogbeat import PyLogBeatClient
from datetime import datetime
import argparse
import json

def logstash_ingest(logstash_host, logstash_port, log_file):
    """
    Send log file to Logstash
    """
    with open(log_file, 'r') as f:
        # Load JSON data
        json_data = json.load(f)

        # Create connector
        client = PyLogBeatClient(logstash_host, logstash_port, ssl_enable=True, ssl_verify=False)
        client.connect()
        for line in json_data:
            client.send([line])
                
        client.close()
        print (f"[+] - {datetime.now()} - Sucessfully uploaded JSON log file to {logstash_host}") 

def elasticsearch_ingest(es_host, es_port, log_file, index, es_username=None, es_password=None, es_threads=50):
    """
    Ingest log file straight into Elasticsearch - skipping Logstash
    """
    es = None
    if es_username and es_password is not None:
        es = Elasticsearch(
            hosts=[{'host': es_host, 'port': es_port}],
            http_auth=(es_username, es_password),
            maxsize=es_threads
        )
    else:
        es = Elasticsearch(
            hosts=[{'host': es_host, 'port': es_port}],
            maxsize=es_threads
        )

    counter = 0
    with open(log_file,'r') as json_file:
        for record in json_file:
            # Turn JSONs tring into dict
            record  = json.loads(record)

            json_id =  record['_id']
            json_body = record['_source']

            # Remove certain key-vaule pairs
            record.pop('_index', None)
            record.pop('_type', None)
            record.pop('_id', None)
            record.pop('_source', None)

            # Add
            res = es.index(index=index, id=json_id, body=json_body)
            counter = counter + 1

            if counter % 100 == 0:
                print (f"Uploaded docs counter: {counter}")

            if res['result'] != "created" and res['result'] != "updated":
                print(res['result'])

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--server_host', type=str, required=True, help='Specify server FQDN or IP address')
    parser.add_argument('--server_port', type=int, default=443, help='Specify the port to ingest logs')
    parser.add_argument('--platform', type=str, required=True, choices=['elasticsearch','logstash','splunk'], help='Specify the method to ingest logs')
    parser.add_argument('--log_file', type=str, required=True, help='File path to log file')
    parser.add_argument('--index', type=str, help='File path to log file')
    parser.add_argument('--siem_username', type=str, default='admin', help='SIEM username')
    parser.add_argument('--siem_password', type=str, default='Changeme123!', help='SIEM password')
    args = parser.parse_args()

    # Send logs to Logstash
    if args.platform == "logstash":
        logstash_ingest(args.server_host, args.server_port, args.log_file)
    elif args.platform == "elasticsearch":
        elasticsearch_ingest(args.server_host, args.server_port, args.log_file, args.index, args.siem_username, args.siem_password, 50)
    elif args.platform == "splunk":
        pass
    else:
        print ("Please select a valid platform to ingest logs")

    
    
