from pylogbeat import PyLogBeatClient
from datetime import datetime
from app.models import LogstashSIEM
import pandas as pd
import json


def streamJsonFileUpload(siem: LogstashSIEM) -> None:
    """
    Send log file to Logstash
    """
    with open(siem.LogFile, 'r') as jsonFile:
        counter = 0
        chunksize = 1000
        reader = pd.read_json(jsonFile, orient="records", lines=True, chunksize=chunksize)

        # Create Logstash connector
        client = PyLogBeatClient(siem.Host, siem.IngestPort, ssl_enable=True, ssl_verify=False)
        client.connect()

        for chunk in reader:
            # Convert Pandas dataframe to JSON list
            logEvents = list()
            if "json" in chunk.index:
                logEvents = json.loads(chunk['json'].to_json(orient="records"))
            else:
                d = json.loads(chunk.to_json(orient="records"))
                for logEvent in d:
                   logEvents.append( {"json": logEvent} )
            
            # Send logs to Logstash
            client.send(logEvents)
      
            # Increase counter
            counter = counter + chunksize
            print (f"[+] - {datetime.now()} - Uploaded {counter} events")  

        # Close connection to Logstash
        client.close()
        print (f"[+] - {datetime.now()} - Sucessfully uploaded JSON log file to {siem.Host}") 
        

def ImportLogs(siem: LogstashSIEM) -> None:
    print (f"[*] - {datetime.now()} - Importing logs into Logstash")

    # Stream file upload
    streamJsonFileUpload(siem)
    print (f"[+] - {datetime.now()} - Logs have been imported into Logstash")