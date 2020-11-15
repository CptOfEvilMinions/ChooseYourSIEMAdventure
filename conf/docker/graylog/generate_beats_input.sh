#!/bin/bash

SIEM_USERNAME=graylog-test-user
SIEM_PASSWORD=graylog-test-password
#GRAYLOG_URL=https://10.150.100.210:8443
GRAYLOG_URL=http://127.0.0.1:9000

### UNTIL ###
while [[ "$(curl -s -k -u ${SIEM_USERNAME}:${SIEM_PASSWORD} -H 'Content-Type: application/json' -X GET ${GRAYLOG_URL}/api/system/inputs -o /dev/null -w ''%{http_code}'')" != "200" ]]; do sleep 5; done

if [ `curl -k -s -u ${SIEM_USERNAME}:${SIEM_PASSWORD} -H 'Content-Type: application/json' -X GET ${GRAYLOG_URL}/api/system/inputs | grep -c "Beats input"` == 0 ]
then
  curl -k -u ${SIEM_USERNAME}:${SIEM_PASSWORD} -H 'Content-Type: application/json' -X POST ${GRAYLOG_URL}/api/system/inputs -d '{
    "title": "Beats input",
    "type": "org.graylog.plugins.beats.Beats2Input",
    "global": true,
    "configuration": {
      "recv_buffer_size": 1048576,
      "tcp_keepalive": false,
      "number_worker_threads": 4,
      "tls_client_auth_cert_file": "",
      "bind_address": "0.0.0.0",
      "tls_cert_file": "/usr/share/graylog/tls/graylog.crt",
      "port": 5044,
      "tls_key_file": "/usr/share/graylog/tls/graylog.key",
      "tls_enable": true,
      "tls_key_password": "",
      "tls_client_auth": "disabled",
      "override_source": null,
      "no_beats_prefix": false
    },
    "node": null
  }' -H 'X-Requested-By: cli'
else
  echo "Beats input exists already"
fi