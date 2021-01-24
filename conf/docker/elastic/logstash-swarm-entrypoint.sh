#!/bin/bash

# Delete default config
rm /usr/share/logstash/pipeline/logstash.conf

############################# Change username and password variable name ############################
cp /usr/share/logstash/templates/30-output-elasticsearch.conf /usr/share/logstash/pipeline/30-output-elasticsearch.conf 
sed -i 's/{{ SIEM_USERNAME }}/logstash_writer/g' /usr/share/logstash/pipeline/30-output-elasticsearch.conf 
sed -i 's/{{ SIEM_PASSWORD }}/${LOGSTASH_WRITER_PWD}/g' /usr/share/logstash/pipeline/30-output-elasticsearch.conf 

############################ Create Logstash keystore and add credentials ############################
yes | /usr/share/logstash/bin/logstash-keystore create &>/dev/null
echo 'Created Logstash keystore'

# Add ogstash_writer password
cat /run/secrets/elastic-builtin-logstash_writer | /usr/share/logstash/bin/logstash-keystore add LOGSTASH_WRITER_PWD --stdin --force &>/dev/null
echo 'Added Logstash password for ES to Logstash keystore'

# Add logstash_system password
cat /run/secrets/elastic-builtin-logstash_system | /usr/share/logstash/bin/logstash-keystore add LOGSTASH_SYSTEM_PWD --stdin --force &>/dev/null
echo 'Added Logstash password for ES to Logstash keystore'

############################ Provide keystore credentials to check license information from license server ############################
echo 'xpack.monitoring.elasticsearch.username: "logstash_system"' >> /usr/share/logstash/config/logstash.yml
echo 'xpack.monitoring.elasticsearch.password: "${LOGSTASH_SYSTEM_PWD}"' >> /usr/share/logstash/config/logstash.yml

#### Start Logstash ####
/usr/local/bin/docker-entrypoint