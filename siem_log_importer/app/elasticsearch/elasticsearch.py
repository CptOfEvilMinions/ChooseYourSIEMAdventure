from elasticsearch import Elasticsearch
from elasticsearch import helpers
from datetime import datetime
from app.models import ElasticsearchSIEM
import pandas as pd
import uuid
import json
import requests

def testHTTPS(siem: ElasticsearchSIEM) -> str:
    try:
       r = requests.get(f"http://{siem.Host}:{siem.IngestPort}",timeout=3)
       return "http"
    except requests.exceptions.HTTPError as err:
        return "https"

def indexExists(siem: ElasticsearchSIEM, es: Elasticsearch) -> bool:
    listIndexes = es.indices.get_alias(f"*{siem.Index}*")
    if len(listIndexes) != 0:
        print (f"[*] - {datetime.now()} - Index {siem.Index} already exists")
        return True
    return False

def createIndex(siem: ElasticsearchSIEM, es: Elasticsearch, request_body) -> None:
    res = es.indices.create(index = siem.Index, body = request_body)
    print (res)

def streamJsonFileUpload(siem: ElasticsearchSIEM) -> None:
    """
    Ingest log file straight into Elasticsearch - skipping Logstash
    """
    # Create ES connector
    es = None
    if siem.SiemUsername and siem.SiemPassword is not None:
        es = Elasticsearch(
            hosts=[{'host': siem.Host, 'port': siem.IngestPort}],
            scheme=testHTTPS(siem),
            http_auth=(siem.SiemUsername, siem.SiemPassword),
            maxsize=siem.Threads
        )
    else:
        es = Elasticsearch(
            hosts=[{'host': siem.Host, 'port': siem.IngestPort}],
            maxsize=siem.Threads
        )

    if indexExists(siem, es) == False:
        createIndex(siem, es, {})

    with open(siem.LogFile, 'r') as jsonFile:
        counter = 0
        chunksize = 1000
        reader = pd.read_json(jsonFile, orient="records", lines=True, chunksize=chunksize)

        for chunk in reader:
            # Convert Pandas dataframe to JSON list
            logEvents = list()
            if "json" in chunk.index:
                logEvents = json.loads(chunk['json'].to_json(orient="records"))
            else:
                d = json.loads(chunk.to_json(orient="records"))
                for logEvent in d:
                    logEvents.append( {"json": logEvent} )
            
            #### Upload JSON events #### 
            actions = [
            {
                "_index": f"{siem.Index}",
                "_id": uuid.uuid4(),
                "_source": logEvent["json"]
            }
            for logEvent in logEvents
            ]
            helpers.bulk(es, actions)

        
            # Increase counter
            counter = counter + chunksize
            print (f"[+] - {datetime.now()} - Uploaded {counter} events")  


        # Close connection to Logstash
        es.transport.close()
        print (f"[+] - {datetime.now()} - Sucessfully uploaded JSON log file to {siem.Host}") 
        

def ImportLogs(siem: ElasticsearchSIEM) -> None:
    print (f"[*] - {datetime.now()} - Importing logs into Elasticsearch")

    # Stream file upload
    streamJsonFileUpload(siem)
    print (f"[+] - {datetime.now()} - Logs have been imported into Elasticsearch")
