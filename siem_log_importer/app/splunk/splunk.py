from datetime import datetime
from app.models import SplunkSIEM
import requests
import pandas as pd
import typing
import urllib3
import json
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def signIn(siem: SplunkSIEM) -> str:
    """
    Sign into Splunk and return session key
    """
    try:
        session_key = requests.get(
            url = f"https://{siem.Host}:{siem.Port}/servicesNS/admin/search/auth/login", 
            data={'username': siem.SiemUsername,'password': siem.SiemPassword, "output_mode": "json"}, 
            verify=False
        ).json()['sessionKey']
        print ("[+] - Obtained Splunk session key")
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)
    return session_key


def indexExists(siem: SplunkSIEM) -> bool:
    """
    https://github.com/splunk/splunk-sdk-python/blob/master/examples/index.py
    https://docs.splunk.com/DocumentationStatic/PythonSDK/1.6.5/client.html#splunklib.client.Indexes.delete
    https://docs.splunk.com/Documentation/Splunk/8.0.3/Search/ExportdatausingSDKs
    https://www.tutorialspoint.com/python/string_startswith.htm
    Use the Splunk API to check if an index exists
    """
    try:
        r = requests.get(
            url = f"https://{siem.Host}:{siem.Port}/services/data/indexes",
            headers = { 'Authorization': (f"Splunk {siem.SessionKey}")},
            data = {"output_mode": "json"},
            verify=False
        ).json()
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)

    # Generate Splunk index list
    indexList = [ index['name'] for index in r['entry'] if not index['name'].startswith("_") ]
    if siem.Index in indexList:
        print (f"[*] - {datetime.now()} - Index {siem.Index} already exists")
        return True
    return False


def createIndex(siem: SplunkSIEM):
    """
    Use the Splunk API to create an index
    https://docs.splunk.com/Documentation/Splunk/8.2.1/Indexer/Setupmultipleindexes
    """
    try:
        r = requests.post(
            url = f"https://{siem.Host}:{siem.Port}/services/data/indexes",
            headers = { 'Authorization': (f"Splunk {siem.SessionKey}")},
            data = {"name": "osquery", "datatype":"event", "output_mode": "json"},
            verify=False
        ).json()
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)
    print (f"[+] - {datetime.now()} - Created {siem.Index} index on Splunk")

def hecInputExists(siem: SplunkSIEM) -> typing.Tuple[bool, str, str]:
    """
    Use the Splunk API to list HEC inputs
    https://docs.splunk.com/Documentation/Splunk/8.2.1/Data/HTTPEventCollectortokenmanagement
    """
    try:
        r = requests.get(
            url = f"https://{siem.Host}:{siem.Port}/servicesNS/admin/splunk_httpinput/data/inputs/http/",
            headers = { 'Authorization': (f"Splunk {siem.SessionKey}")},
            data = {"output_mode": "json"},
            verify=False
        ).json()
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)

    # Generate Splunk HEC input list
    hecList = [ hec['name'].split("://")[1] for hec in r['entry'] ]
    if f"{siem.Index}_hec_token" in hecList:
        print (f"[*] - {datetime.now()} - HEC input {siem.Index}_hec_token already exists")
        for hecInput in r['entry']:
            if hecInput['name'].split("://")[1] == f"{siem.Index}_hec_token":
                return True, hecInput['content']['token'], hecInput['name']
    return False, "", ""

def createHECinput(siem: SplunkSIEM) -> typing.Tuple[str, str]:
    """
    Use the Splunk API to create HEC input
    https://docs.splunk.com/Documentation/Splunk/8.2.1/Data/HTTPEventCollectortokenmanagement
    """
    try:
        r = requests.post(
            url = f"https://{siem.Host}:{siem.Port}/servicesNS/admin/splunk_httpinput/data/inputs/http",
            headers = { 'Authorization': (f"Splunk {siem.SessionKey}")},
            data = { 
                        "name": f"{siem.Index}_hec_token", 
                        "index": f"{siem.Index}",
                        "sourcetype": f"{siem.Sourcetype}",
                        "output_mode": "json"
                    },
            verify=False
        ).json()
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)
    return r['entry'][0]['name'], r['entry'][0]['content']['token']

def deleteHECinput(siem: SplunkSIEM):
    """
    Use the Splunk API to delete HEC input
    https://docs.splunk.com/Documentation/Splunk/8.2.1/Data/HTTPEventCollectortokenmanagement
    """
    try:
        r = requests.delete(
            url = f"https://{siem.Host}:{siem.Port}/servicesNS/admin/splunk_httpinput/data/inputs/http/{siem.Index}_hec_token",
            headers = {'Authorization': (f"Splunk {siem.SessionKey}")},
            data = {"output_mode": "json"},
            verify=False
        )
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)
    
    if r.status_code == 200:
        print (f"[*] - {datetime.now()} - HEC input {siem.Index}_hec_token has been deleted")

def streamJsonFileUpload(siem: SplunkSIEM, hecURL: str, hecToken: str):
    # Create request stream session
    s = requests.Session()

    # Add headers
    s.headers.update({ 
        "Authorization": f"Splunk {hecToken}", 
    })

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

            # Iterate over all events
            splunkHECevents = str()
            for logEvent in logEvents:
                splunkHECevents = splunkHECevents + json.dumps({"event": logEvent})

            # Post log event BATCH
            s.post(
                url=f"https://{siem.Host}:{siem.Ingest_port}/services/collector",
                data=splunkHECevents,
                verify=False
            )

            # Increase counter
            counter = counter + chunksize
            print (f"[+] - {datetime.now()} - Uploaded {counter} events")  


def ImportLogs(siem: SplunkSIEM):
    print (f"[*] - {datetime.now()} - Importing logs into Splunk")

    # Sign into Splunk
    siem.SessionKey = signIn(siem)

    # Create HEC input
    exists, hecToken, hecURL = hecInputExists(siem)
    if exists == False:
        hecURL, hecToken = createHECinput(siem)

    
    # Create index
    if indexExists(siem) == False:
      print (f"[*] - {datetime.now()} - Creating {siem.Index} index")
      createIndex(siem)

    # Stream file upload
    streamJsonFileUpload(siem, hecURL, hecToken)
    print (f"[+] - {datetime.now()} - Logs have been imported into the following index: {siem.Index}")
    deleteHECinput(siem)