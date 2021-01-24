#!/bin/bash

############################ Create Logstash keystore and add credentials ############################
yes | /usr/share/kibana/bin/kibana-keystore create
echo 'Created Kibana keystore'

echo 'kibana_system' | /usr/share/kibana/bin/kibana-keystore add elasticsearch.username --stdin --force
echo 'Added Kibana username for ES to Kibana keystore'

cat /run/secrets/elastic-builtin-kibana_system | /usr/share/kibana/bin/kibana-keystore add elasticsearch.password --stdin --force
echo 'Added Kibana password for ES to Kibana keystore'

############################ Provide keystore credentials to check license information from license server ############################
echo -e '\nelasticsearch.username: "${elasticsearch.username}"' >> /usr/share/kibana/config/kibana.yml
echo 'elasticsearch.password: "${elasticsearch.password}"' >> /usr/share/kibana/config/kibana.yml
cat /usr/share/kibana/config/kibana.yml

#### Start Kibana ####
/usr/local/bin/dumb-init /usr/local/bin/kibana-docker