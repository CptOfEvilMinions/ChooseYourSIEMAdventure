#!/bin/bash

# Delete default config
rm /usr/share/logstash/pipeline/logstash.conf

############################# Change username and password variable name ############################
cp /usr/share/logstash/templates/30-output-splunk-hec.conf /usr/share/logstash/pipeline/30-output-splunk-hec.conf
sed -i "s/{{ SPLUNK_ZEEK_HEC_TOKEN }}/$(cat /run/secrets/splunk-hec-token)/g" /usr/share/logstash/pipeline/30-output-splunk-hec.conf

#### Start Logstash ####
/usr/local/bin/docker-entrypoint