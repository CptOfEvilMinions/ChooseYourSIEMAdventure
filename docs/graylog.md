# Graylog

## Default password
<span style="color:red;">Default password is set to `Changem123!`, see instructions in `docs/`</span>

## Elasticseach version
<span style="color:red;">Graylog v3.X depends on Elasticsearch 6.X</span>. This means the ulimit on Linux hosts needs to be increased.

## Access Rest API via web browser
* `https://<Docker IP addr>:8443/api/api-browser/global/index.html`

## Docker
1. Login into whatever host will be runnibg this docker-compose
1. `sysctl -w vm.max_map_count=262144`
1. `echo 'vm.max_map_count=262144' >> /etc/sysctl.conf`
1. `docker-compose -f docker-compose-graylog.yml build`
1. `docker-compose -f docker-compose-graylog.yml up -d`
1. `docker exec -it siem-graylog-graylog /usr/share/graylog/generate_beats_input.sh`
  1. Setup Beats input
1. Browse to `https://<Docker IP addr>:8443`
  1. Enter `admin` for username
  1. Enter `<SIEM_PASSWORD>` for password


## Ansible
1. Modify `hosts.ini`


## References
* [How to add color to Github's README.md file](https://stackoverflow.com/questions/11509830/how-to-add-color-to-githubs-readme-md-file)
* [Elasticsearch: Max virtual memory areas vm.max_map_count [65530] is too low, increase to at least [262144]](https://stackoverflow.com/questions/51445846/elasticsearch-max-virtual-memory-areas-vm-max-map-count-65530-is-too-low-inc)
* [Graylog - Elasticsearch system requirements](https://docs.graylog.org/en/3.1/pages/installation.html)
* [Github - Graylog - Elasticsearch 7 Support](https://github.com/Graylog2/graylog2-server/issues/5933)
* [Github - jalogisch/d-gray-lab](https://github.com/jalogisch/d-gray-lab/blob/master/docker-compose.yml)
* [How can I change my MONGODB_URI for my mlab provisioned DB on Heroku?](https://stackoverflow.com/questions/37900283/how-can-i-change-my-mongodb-uri-for-my-mlab-provisioned-db-on-heroku)
* [Dockerhub - Mongo](https://hub.docker.com/_/mongo?tab=description&page=1&name=4.2)
* [User not found on MongoDB Docker image with authentication](https://stackoverflow.com/questions/58406236/user-not-found-on-mongodb-docker-image-with-authentication)
* [Dockerhub - Mongo](https://hub.docker.com/_/mongo?tab=description&page=1&name=4.2)
* [Setup MongoDB server with docker](https://transang.me/setup-mongodb-server-with-docker/)
* [MongoDB Server Parameters](https://docs.mongodb.com/manual/reference/parameters/#param.authenticationMechanisms)
* [Authentication Examples](https://api.mongodb.com/python/current/examples/authentication.html)
* [User not found on MongoDB Docker image with authentication](https://stackoverflow.com/questions/58406236/user-not-found-on-mongodb-docker-image-with-authentication)
* [Connection String URI Format](https://docs.mongodb.com/manual/reference/connection-string/)
* [How to Enable Authentication on MongoDB](https://medium.com/mongoaudit/how-to-enable-authentication-on-mongodb-b9e8a924efac)
* [Error authenticating MongoCredential when trying to connect from spring boot docker container to mongo docker container?](https://stackoverflow.com/questions/61109707/error-authenticating-mongocredential-when-trying-to-connect-from-spring-boot-doc)
* [Operating System Packages](https://docs.graylog.org/en/3.3/pages/installation/operating_system_packages.html#prerequisites)
* [Graylog Docker NGINX Reverse Proxy HTTPS](https://community.graylog.org/t/graylog-docker-nginx-reverse-proxy-https/13696)
* [Deploying Graylog 3 With Docker](http://blog.audio-tk.com/2019/06/11/deploying-graylog-3-with-docker/)
* [Setting up Elasticsearch and Kibana on Docker with X-Pack security enabled](https://codingfundas.com/setting-up-elasticsearch-6-8-with-kibana-and-x-pack-security-enabled/index.html)
* [Github issue - Configure Beats Inputs,create input|output|snippet doesn't work #4241](https://github.com/Graylog2/graylog2-server/issues/4241)
* [Graylog - server.conf](https://docs.graylog.org/en/3.3/pages/configuration/server.conf.html#web-rest-api-options)
* [Automatically create UDP input for Graylog2 server running in Docker?](https://stackoverflow.com/questions/26615893/automatically-create-udp-input-for-graylog2-server-running-in-docker)
* [Graylog REST API](https://docs.graylog.org/en/3.1/pages/configuration/rest_api.html)
* [REST API browser (graylog 3.1) not accessible behind nginx reverse proxy](https://community.graylog.org/t/rest-api-browser-graylog-3-1-not-accessible-behind-nginx-reverse-proxy/12851/8)
* [Wait for an HTTP endpoint to return 200 OK with Bash and curl](https://gist.github.com/rgl/f90ff293d56dbb0a1e0f7e7e89a81f42)
* [How to check if curl was successful and print a message?](https://stackoverflow.com/questions/38905489/how-to-check-if-curl-was-successful-and-print-a-message)
* [Install MongoDB Community Edition on Ubuntu](https://docs.mongodb.com/manual/tutorial/install-mongodb-on-ubuntu/)
* [apt_repository module does not allow enabling 'universe' repository](https://github.com/ansible/ansible/issues/48714)
* [Graylog -Ubuntu installation](https://docs.graylog.org/en/3.3/pages/installation/os/ubuntu.html)
* [How to Install MongoDB on Ubuntu 20.04](https://linuxhint.com/install_mongodb_ubuntu/)
* [Mongo repo - multiverse](https://repo.mongodb.org/apt/ubuntu/dists/focal/mongodb-org/4.2/multiverse/)
* [Check MongoDB Version in Windows / Linux](https://www.configserverfirewall.com/mongodb/check-mongodb-version/)
* [Install Elasticsearch v7.10.0 with Docker](https://www.elastic.co/guide/en/elasticsearch/reference/current/docker.html)
* []()
* []()
* []()