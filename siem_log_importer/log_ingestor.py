from app.models import ElasticsearchSIEM, LogstashSIEM, SplunkSIEM, GraylogSIEM
from app.elasticsearch import elasticsearch
from app.logstash import logstash
from app.splunk import splunk
import argparse
import sys

if __name__ == "__main__":
    ### Default arguments ####
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(help='help for subcommand')

    #### Init SIEM group args ####
    splunkArgs = subparsers.add_parser("splunk")
    graylogArgs = subparsers.add_parser("graylog")
    logstashArgs = subparsers.add_parser("logstash")
    elasticsearchArgs = subparsers.add_parser("elasticsearch")
    
    #### Splunk args ####
    splunkArgs.add_argument('--siem_host', type=str, required=True, help='Specify server FQDN or IP address')
    splunkArgs.add_argument('--siem_username', type=str, required=True, default='admin', help='SIEM username')
    splunkArgs.add_argument('--siem_password', type=str, required=True, default='Changeme123!', help='SIEM password')
    splunkArgs.add_argument('--siem_api_port', type=int, required=True, default=8443, help='Specify the port to interact with SIEM REST API')
    splunkArgs.add_argument('--ingest_port', type=int, required=True, default=8088, help='Specify the port to ingest logs')
    splunkArgs.add_argument('--log_file', type=str, required=True, help='File path to log file')
    splunkArgs.add_argument('--index', type=str, required=True, default="main", help='Specify the index to ingest logs into')
    splunkArgs.add_argument('--sourcetype', type=str, default="_json", help='Specify the index to ingest logs into')

    #### Graylog args ####
    graylogArgs.add_argument('--siem_host', type=str, required=True, help='Specify server FQDN or IP address')
    graylogArgs.add_argument('--log_file', type=str, required=True, help='File path to log file')
    graylogArgs.add_argument('--ingest_port', type=int, required=True, default=5044, help='Specify the port to ingest logs')
    
    #### Logstash args ####
    logstashArgs.add_argument('--siem_host', type=str, required=True, help='Specify server FQDN or IP address')
    logstashArgs.add_argument('--log_file', type=str, required=True, help='File path to log file')
    logstashArgs.add_argument('--ingest_port', type=int, required=True, default=5044, help='Specify the port to ingest logs')

    #### Elasticsearch args ####
    elasticsearchArgs.add_argument('--siem_host', type=str, required=True, help='Specify server FQDN or IP address')
    elasticsearchArgs.add_argument('--ingest_port', type=int, required=True, default=9200, help='Specify the port to ingest logs')
    elasticsearchArgs.add_argument('--siem_username', type=str, required=False, default=None, help='SIEM username')
    elasticsearchArgs.add_argument('--siem_password', type=str, required=False, default=None, help='SIEM password')
    elasticsearchArgs.add_argument('--log_file', type=str, required=True, help='File path to log file')
    elasticsearchArgs.add_argument('--index', type=str, required=True, help='Specify the index to ingest logs into')
    elasticsearchArgs.add_argument('--threads', type=int, default=50, help='Specify how many threads to use for ES client')
    args = parser.parse_args()

    # Create SIEM object and run import func based on platform type
    platform = sys.argv[1]
    if platform == "splunk":
        siem = SplunkSIEM(
            args.siem_host, 
            args.log_file,
            args.ingest_port, 
            args.index, 
            args.siem_api_port, 
            args.siem_username, 
            args.siem_password, 
        )
        splunk.ImportLogs(siem)
    elif platform == "logstash":
        siem = LogstashSIEM(args.siem_host, args.log_file, args.ingest_port)
        logstash.ImportLogs(siem)  
    elif platform == "elasticsearch":
        siem = ElasticsearchSIEM(
            args.siem_host,
            args.log_file,
            args.ingest_port, 
            args.index, 
            args.threads, 
            args.siem_username, 
            args.siem_password
            )
        elasticsearch.ImportLogs(siem)
    else:
        print ("Please select a valid platform to ingest logs")
    # Send logs to Logstash
    #if args.platform == "logstash":
    #    logstash_ingest(args.server_host, args.server_port, args.log_file)
    #elif args.platform == "elasticsearch":
    #    elasticsearch_ingest
    #elif args.platform == "splunk":
    #    pass
    #else:
    #    print ("Please select a valid platform to ingest logs")

    
    
