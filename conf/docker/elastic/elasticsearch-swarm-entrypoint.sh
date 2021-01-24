#!/bin/bash

#### Wait until Elasticsearch is avaliable ####
# https://www.elastic.co/guide/en/elasticsearch/reference/current/cluster-health.html
echo 'Waiting for Elasticsearch to be ready'
while [[ "$(curl -s -k -u elastic:$(cat /run/secrets/elastic-builtin-elastic) -H 'Content-Type: application/json' -X GET http://localhost:9200/_cluster/health -o /dev/null -w ''%{http_code}'')" != "200" ]]; do sleep 1; done
echo 'Elasticsearch is ready'


#### Create logstash_writer role ####
curl -s -k -u elastic:$(cat /run/secrets/elastic-builtin-elastic) -H 'Content-Type: application/json' -X POST http://localhost:9200/_xpack/security/role/logstash_writer -d '{"cluster": ["manage_index_templates", "monitor", "manage_ilm"], "indices": [{"names": [ "*-*" ], "privileges": ["write","create","delete","create_index","manage","manage_ilm"] }]}'

#### Create logstash_writer user ####
curl -s -k -u elastic:$(cat /run/secrets/elastic-builtin-elastic) -H 'Content-Type: application/json' -X POST http://localhost:9200/_security/user/logstash_writer -d "{\"password\" : \"$(cat /run/secrets/elastic-builtin-logstash_writer)\", \"roles\" : [ \"logstash_writer\" ], \"full_name\" : \"Logstash writer\", \"email\" : \"logstash_writer@elastic.local\"}"

##### Iterate the built in user accounts and set passwords based on secrets ####
# https://www.elastic.co/guide/en/elasticsearch/reference/current/built-in-users.html
for user in 'kibana_system' 'logstash_system' 'beats_system' 'apm_system' 'remote_monitoring_user' 'logstash_writer';
do
    curl --silent -u elastic:$(cat /run/secrets/elastic-builtin-elastic) -XPUT -H 'Content-Type: application/json' "http://localhost:9200/_xpack/security/user/${user}/_password" -d "{ \"password\":\"$(cat /run/secrets/elastic-builtin-${user})\" }" > /dev/null
    echo "Set password for ${user} - $(cat /run/secrets/elastic-builtin-${user})"
done
