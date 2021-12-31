# ChooseYourSIEMAdventure Changelog

<a name="graylog-v4.2.4"></a>
## [graylog-v4.2.4](https://github.com/osquery/osquery/releases/tag/graylog-v4.2.4)

[Git Commits](https://github.com/CptOfEvilMinions/ChooseYourSIEMAdventure/compare/splunk-v8.2...graylog-v4.2.4)

### New Features

- Adding `CHANGELOG.md`

### Under the Hood improvements
- Added `-Dlog4j2.formatMsgNoLookups=true"` `docker-compose-graylog.yml`, `docker-compose-swarm-graylog.yml`,and `docker-compose-swarm-traefik-elastic.yml`to Elasticsearch JAVA environment variable to [mitigate log4j vulnerability.](https://github.com/elastic/elasticsearch/issues/81618#issuecomment-991000240)
- Added [GRAYLOG_PASSWORD_SECRET to docker-compose](https://github.com/CptOfEvilMinions/ChooseYourSIEMAdventure/blob/main/docker-compose-graylog.yml#L37)
- Updated [Docker-compose](https://github.com/CptOfEvilMinions/ChooseYourSIEMAdventure/blob/main/.env#L7) to use `nginx:1.21.5-alpine`
- Updated [Docker-compose](https://github.com/CptOfEvilMinions/ChooseYourSIEMAdventure/blob/main/docker-compose-graylog.yml#L56) to use `mongo:4.2.17`
- Updated [Docker-compose](https://github.com/CptOfEvilMinions/ChooseYourSIEMAdventure/blob/main/.env#L3) to use Graylog v4.2.4
- Updated [Docker-compose-swarm](https://github.com/CptOfEvilMinions/ChooseYourSIEMAdventure/blob/main/docker-compose-swarm-graylog.yml#L5) to use `nginx:1.21.5-alpine`
- Updated [Docker-compose-swarm](https://github.com/CptOfEvilMinions/ChooseYourSIEMAdventure/blob/main/docker-compose-swarm-graylog.yml#L91) to use `mongo:4.2.17`
- Updated [Docker-compose-swarm](https://github.com/CptOfEvilMinions/ChooseYourSIEMAdventure/blob/main/docker-compose-swarm-graylog.yml#L40) to use Graylog v4.2.4
- Updated [Docker-compose-swarm-traefik](https://github.com/CptOfEvilMinions/ChooseYourSIEMAdventure/blob/main/docker-compose-swarm-traefik-graylog.yml#L5) to use Graylog v4.2.4
- Updated [Docker-compose-swarm-traefik](https://github.com/CptOfEvilMinions/ChooseYourSIEMAdventure/blob/main/docker-compose-swarm-traefik-graylog.yml#L64) to use `mongo:4.2.17`
- Updated [Ansible playbook](https://github.com/CptOfEvilMinions/ChooseYourSIEMAdventure/blob/main/group_vars/graylog.yml#L4) to use Graylog v4.2.4
- Updated [Ansible playbook](https://github.com/CptOfEvilMinions/ChooseYourSIEMAdventure/blob/main/group_vars/graylog.yml#L16) to use `Elasticsearch:7.16.2`
- Updated [Ansible playbook](https://github.com/CptOfEvilMinions/ChooseYourSIEMAdventure/blob/main/group_vars/graylog.yml#L22) to use `mongo:4.2.17`
- Updated [Vagrant](https://github.com/CptOfEvilMinions/ChooseYourSIEMAdventure/blob/main/group_vars/graylog.yml#L4) to use Graylog v4.2.4
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



