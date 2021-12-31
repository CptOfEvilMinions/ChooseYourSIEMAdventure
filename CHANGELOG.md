# ChooseYourSIEMAdventure Changelog

<a name="splunk-v8.2.4"></a>
## [splunk-v8.2.4](https://github.com/CptOfEvilMinions/ChooseYourSIEMAdventure/releases/tag/splunk-v8.2.4)

[Git Commits](https://github.com/CptOfEvilMinions/ChooseYourSIEMAdventure/compare/graylog-v4.2.4...splunk-v8.2.4)


### Under the Hood improvements

- Updated [.env](https://github.com/CptOfEvilMinions/ChooseYourSIEMAdventure/blob/main/.env#L2) to use Splunk v8.2.4
- Updated [.env](https://github.com/CptOfEvilMinions/ChooseYourSIEMAdventure/blob/main/.env#L1) to use Elastic/Logstash v7.16.2
- Updated [docker-compose-swarm-splunk.yml](https://github.com/CptOfEvilMinions/ChooseYourSIEMAdventure/blob/main/docker-compose-swarm-splunk.yml#L5) to use `nginx:1.21.5-alpine`
- Updated [docker-compose-swarm-splunk.yml](https://github.com/CptOfEvilMinions/ChooseYourSIEMAdventure/blob/main/docker-compose-swarm-splunk.yml#L42) to use `splunk:8.2.4`
- Updated [docker-compose-swarm-splunk.yml](https://github.com/CptOfEvilMinions/ChooseYourSIEMAdventure/blob/main/docker-compose-swarm-splunk.yml#L42) to use `logstash:7.16.2`
- Updated [docker-compose-swarm-traefik-splunk.yml](https://github.com/CptOfEvilMinions/ChooseYourSIEMAdventure/blob/main/docker-compose-swarm-traefik-splunk.yml#L5) to use `splunk:8.2.4`
- Updated [docker-compose-swarm-traefik-splunk.yml](https://github.com/CptOfEvilMinions/ChooseYourSIEMAdventure/blob/main/docker-compose-swarm-traefik-splunk.yml#L38) to use `logstash:7.16.2`
- Updated [group_vars/splunk.yml](https://github.com/CptOfEvilMinions/ChooseYourSIEMAdventure/blob/main/group_vars/splunk.yml#L3) to use Splunk v8.2.4
- Updated [group_vars/splunk.yml](https://github.com/CptOfEvilMinions/ChooseYourSIEMAdventure/blob/main/group_vars/splunk.yml#L10) to use `Logstash:7.16.2`
- Updated [Splunk log test](pipeline_testers/beats_input_test.py)

### Bug Fixes

- Upgrading Splunk to a version that is [not vulnerable to log4j](https://www.splunk.com/en_us/blog/bulletins/splunk-security-advisory-for-apache-log4j-cve-2021-44228.html)
- Upgrading Logstash to a version that is [not vulnerable to log4j](https://discuss.elastic.co/t/apache-log4j2-remote-code-execution-rce-vulnerability-cve-2021-44228-esa-2021-31/291476)

### CI/CD

- Added GHA workflow to test changes to `docker-compose-splunk.yml`
- Added GHA workflow to test changes to `deploy_splunk.yml`

### Documentation

- Updated Splunk supported version to v8.2.4 on [README](README.md)

<a name="graylog-v4.2.4"></a>
## [graylog-v4.2.4](https://github.com/CptOfEvilMinions/ChooseYourSIEMAdventure/releases/tag/graylog-v4.2.4)

[Git Commits](https://github.com/CptOfEvilMinions/ChooseYourSIEMAdventure/compare/splunk-v8.2...graylog-v4.2.4)

### New Features

- Adding `CHANGELOG.md`

### Under the Hood improvements
- Added `-Dlog4j2.formatMsgNoLookups=true"` to `docker-compose-graylog.yml`, `docker-compose-swarm-graylog.yml`,and `docker-compose-swarm-traefik-elastic.yml`to Elasticsearch JAVA environment variable to [mitigate log4j vulnerability.](https://github.com/elastic/elasticsearch/issues/81618#issuecomment-991000240)
- Added [GRAYLOG_PASSWORD_SECRET to docker-compose-graylog.yml](https://github.com/CptOfEvilMinions/ChooseYourSIEMAdventure/blob/main/docker-compose-graylog.yml#L37)
- Updated [docker-compose-graylog.yml](https://github.com/CptOfEvilMinions/ChooseYourSIEMAdventure/blob/main/.env#L7) to use `nginx:1.21.5-alpine`
- Updated [docker-compose-graylog.yml](https://github.com/CptOfEvilMinions/ChooseYourSIEMAdventure/blob/main/docker-compose-graylog.yml#L56) to use `mongo:4.2.17`
- Updated [docker-compose-graylog.yml](https://github.com/CptOfEvilMinions/ChooseYourSIEMAdventure/blob/main/.env#L3) to use Graylog v4.2.4
- Updated [docker-compose-swarm-graylog.yml](https://github.com/CptOfEvilMinions/ChooseYourSIEMAdventure/blob/main/docker-compose-swarm-graylog.yml#L5) to use `nginx:1.21.5-alpine`
- Updated [docker-compose-swarm-graylog.yml](https://github.com/CptOfEvilMinions/ChooseYourSIEMAdventure/blob/main/docker-compose-swarm-graylog.yml#L91) to use `mongo:4.2.17`
- Updated [docker-compose-swarm-graylog.yml](https://github.com/CptOfEvilMinions/ChooseYourSIEMAdventure/blob/main/docker-compose-swarm-graylog.yml#L40) to use Graylog v4.2.4
- Updated [docker-compose-swarm-traefik-graylog.yml](https://github.com/CptOfEvilMinions/ChooseYourSIEMAdventure/blob/main/docker-compose-swarm-traefik-graylog.yml#L5) to use Graylog v4.2.4
- Updated [docker-compose-swarm-traefik-graylog.yml](https://github.com/CptOfEvilMinions/ChooseYourSIEMAdventure/blob/main/docker-compose-swarm-traefik-graylog.yml#L64) to use `mongo:4.2.17`
- Updated [group_vars/graylog.yml](https://github.com/CptOfEvilMinions/ChooseYourSIEMAdventure/blob/main/group_vars/graylog.yml#L4) to use Graylog v4.2.4
- Updated [group_vars/graylog.yml](https://github.com/CptOfEvilMinions/ChooseYourSIEMAdventure/blob/main/group_vars/graylog.yml#L16) to use `Elasticsearch:7.16.2`
- Updated [group_vars/graylog.yml](https://github.com/CptOfEvilMinions/ChooseYourSIEMAdventure/blob/main/group_vars/graylog.yml#L22) to use `mongo:4.2.17`
- Updated [Vagrantfile-graylog](https://github.com/CptOfEvilMinions/ChooseYourSIEMAdventure/blob/main/group_vars/graylog.yml#L4) to use Graylog v4.2.4
- Updated TLS config from 2048 bits to [4096 bits](https://github.com/CptOfEvilMinions/ChooseYourSIEMAdventure/blob/main/conf/tls/tls.conf#L2)

### Bug Fixes

- Upgrading Graylog to a version that is [not vulnerable to log4j](https://www.graylog.org/post/graylog-update-for-log4j)
- Upgrading Mongo to a version that is [not vulnerable to log4j](https://www.mongodb.com/blog/post/log4shell-vulnerability-cve-2021-44228-and-mongodb)

### CI/CD

- Added GHA workflow to test changes to `docker-compose-graylog.yml`
- Added GHA workflow to test changes to `deploy_graylog.yml`
- Added GHA workflow for tagged releases `.github/workflows/tagged-release.yml`

### Documentation

- Updated Graylog supported version to v4.2.4 on [README](README.md)
