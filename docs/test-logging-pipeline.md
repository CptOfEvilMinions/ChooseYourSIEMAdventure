# Test Logging Pipeline

1. `pip3 install 


```python
from datetime import datetime
from pylogbeat import PyLogBeatClient

client = PyLogBeatClient('<IP addr>', 5044, ssl_enable=True, ssl_verify=False)

message = {'@timestamp': datetime.now().timestamp(),  '@version': '1', '_type': 'test', 'message': 'hello world55555555555555'}

client.connect()
client.send([message])
client.close()
```

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