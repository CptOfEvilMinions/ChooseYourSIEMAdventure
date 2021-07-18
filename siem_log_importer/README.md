# SIEM JSON file log ingestor

## Local development
1. `virtualenv -p python3 venv`
1. `source venv/bin/activate`
1. `pip3 install -r requirements.txt`

## Upload Osquery logs to Splunk via HEC input
```bash
python3 log_ingestor.py splunk \
--siem_host <Splunk IP addr> \
--siem_api_port <Splunk API port> \
--index <index> \
--log_file <Osquery log file path> \
--siem_username <Splunk admin username> \
--siem_password <Splunk admin password> \
--ingest_port 8088
```

## Upload Zeek logs via Logstash input
```bash
python3 log_ingestor.py logstash \
--siem_host <Logstash IP addr> \
--ingest_port <Logstash BEATs port - default 5044> \
--log_file <Zeek log file path>
```


## Tested and supported SIEM versions
* `Splunk v8.1.2`
* `Graylog v4.1`
* `Logstah v7.13`
* `Elastic v7.13`

## References
### Python 
* [pydantic](https://pydantic-docs.helpmanual.io/usage/types/)
* [Python typing](https://docs.python.org/3/library/typing.html)
* [How to get current date and time in Python?](https://www.programiz.com/python-programming/datetime/current-datetime)
* [Correct way to try/except using Python requests module?](https://stackoverflow.com/questions/16511337/correct-way-to-try-except-using-python-requests-module)
* [CptOfEvilMinions/MyLoggingPipeline - splunk-kafka-connector.py](https://github.com/CptOfEvilMinions/MyLoggingPipeline/blob/master/splunk-kafka-connector.py)
* [`Iterable[(int, int)]` tuple is not allowed in type hints](https://stackoverflow.com/questions/39562977/iterableint-int-tuple-is-not-allowed-in-type-hints)
* [How to convert pandas DataFrame into JSON in Python?](https://www.geeksforgeeks.org/how-to-convert-pandas-dataframe-into-json-in-python/)
* [Pandas dataframe to json list format](https://stackoverflow.com/questions/43134637/pandas-dataframe-to-json-list-format)
* [Load Yelp reviews (or other huge JSON files) with ease](https://towardsdatascience.com/load-yelp-reviews-or-other-huge-json-files-with-ease-ad804c2f1537)
* [Python Requests - Advanced Usage](https://docs.python-requests.org/en/master/user/advanced/)
* [Python - Command Line Arguments](https://www.tutorialspoint.com/python/python_command_line_arguments.htm)
* [Rename a dictionary key](https://stackoverflow.com/questions/16475384/rename-a-dictionary-key)
* []()
* []()

### Splunk
* [Splunk REST API - check if index exists](https://community.splunk.com/t5/Archive/How-to-check-if-an-index-exists-efficiently/m-p/438034)
* [Splunk REST API is EASY to use](https://www.splunk.com/en_us/blog/tips-and-tricks/splunk-rest-api-is-easy-to-use.html)
* [Splunk - receivers/stream](https://docs.splunk.com/Documentation/Splunk/6.3.3/RESTREF/RESTinputExamples#receivers.2Fstream_POST)
* [Splunk - receivers/simple](https://docs.splunk.com/Documentation/Splunk/6.3.3/RESTREF/RESTinput#receivers.2Fsimple)
* [Splunk - Send multiple events to HEC in one request](https://docs.splunk.com/Documentation/Splunk/8.2.1/Data/HTTPEventCollectortokenmanagement)
* []()
* []()
* []()

### Graylog
* []()
* []()
* []()
* []()
* []()
* []()
* []()

### Elastic
* []()
* []()
* []()
* []()
* []()
* []()
