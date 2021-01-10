# Test Logging Pipeline

## Run test script
1. `virtualenv -p python3 venv`
1. `source venv/bin/activate`
1. `pip3 install -r requirements.txt`
1. `python3 beats_input_test.py --host <SIEM host> -p <Beats input port - default 5044>`

## Check results on Graylog
1. Log into Graylog
1. System > inputs
1. Select "Show received messages" 
  1. ![graylog_beats_input_check](../.img/graylog_beats_input_check.png)

## Check results on Elastic
1. Log into Kibana
1. Stack Management > Kibana > Index patterns
  1. Select "Create index pattern"
  1. Enter `python-logstash-*` for index pattern name
  1. Create index pattern
1. Go to `python-logstash` index
  1. ![elastic_beats_input_check](../.img/elastic_beats_input_check.png)

## Check results on Splunk
1. Log into Splunk
1. Search & Reporting
1. Enter query: `index="main"`
  1. ![splunk_beats_input_check](../.img/splunk_beats_input_check.png)


## References
* [How To Get Current Timestamp In Python](https://timestamp.online/article/how-to-get-current-timestamp-in-python)
* [Github - eht16/pylogbeat](https://github.com/eht16/pylogbeat/)
* [PyLogBeat](https://pypi.org/project/pylogbeat/)
* []()
* []()
* []()
* []()
* []()
* []()