# Choose your own SIEM adventure
Repo of configs for the three major SIEMs. 

## Security notes
* <span style="color:red;">Default password is set to `Changem123!`</span>
* <span style="color:red;">Docker stacks are for development ONLY and are NOT secure for production</span>

## Default credentials
<span style="color:red;">Default password is set to `Changem123!` or the value of `SIEM_PASSWORD` in `.env`, see instructions in `docs/`</span>

## Config direcotry: `conf/`
* `conf/ansible` - This directory contains all the configs for the Ansible playbooks and a manual install
* `conf/docker` - This directory contains all the configs for Docker

## Generate public cert and private key
1. `openssl req -x509 -nodes -days 3650 -newkey rsa:2048 -keyout conf/tls/docker.key -out conf/tls/docker.crt`

## Elasticsearch setting heap size
The Ansible playbooks will automatically set the heap size to half of total system memory allocated to a host. For example, if a machine has `16GB` of memory, the ES heap size will be set to `8GB`.

## Supported versions
* `Graylog v4.0.1`
* `Elastic v7.10`
* `Splunk v7.0.8`
* `Ansible v2.11+`
* `Ubuntu 20.04 64-bit`

## References
### Docker
* [RUN inside a conditional statement in Dockerfile](https://stackoverflow.com/questions/51518087/run-inside-a-conditional-statement-in-dockerfile)
* []()
* []()
* []()
* []()


### Ansible
* [ansible.builtin.reboot – Reboot a machine](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/reboot_module.html)
* [How to Set or Change the Time Zone in Linux](https://linuxize.com/post/how-to-set-or-change-timezone-in-linux/)
* [Ansible: get current target host's IP address](https://stackoverflow.com/questions/39819378/ansible-get-current-target-hosts-ip-address)
* [Register variable numerical comparisons](https://groups.google.com/g/ansible-project/c/kzzsYro1Z1c)
* [ansible.builtin.apt_repository – Add and remove APT repositories](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/apt_repository_module.html)
* [ansible.builtin.apt_key – Add or remove an apt key](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/apt_key_module.html)
* [ansible.builtin.set_fact – Set host facts from a task](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/set_fact_module.html)
* [How to split strings and join them in A​nsibl​e](https://www.mydailytutorials.com/how-to-split-strings-and-join-them-in-a%E2%80%8Bnsibl%E2%80%8Be/)
* [Ansible: Store command's stdout in new variable?](https://stackoverflow.com/questions/36059804/ansible-store-commands-stdout-in-new-variable)
* [ansible.builtin.lineinfile – Manage lines in text files](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/lineinfile_module.html)
* [Write variable to a file in Ansible](https://stackoverflow.com/questions/26638180/write-variable-to-a-file-in-ansible)
* [ansible.builtin.uri – Interacts with webservices](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/uri_module.html)
* [ansible.builtin.uri – Interacts with webservices](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/uri_module.html)
* [mikeifomin/wait_for_http.yml](https://gist.github.com/mikeifomin/67e233cd461331de16707ef59a07e372)
* [How can I check the available version of a package in the repositories?](https://askubuntu.com/questions/340530/how-can-i-check-the-available-version-of-a-package-in-the-repositories)
* [Ansible read JSON file – JSON file Parsing](https://www.middlewareinventory.com/blog/ansible-playbook-read-json-file/)
* [ansible.builtin.user – Manage user accounts](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/user_module.html)
* [Add a User to a Group (or Second Group) on Linux](https://www.howtogeek.com/50787/add-a-user-to-a-group-or-second-group-on-linux/)
* [ansible.builtin.replace – Replace all instances of a particular string in a file using a back-referenced regular expression](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/replace_module.html)
* [Setting hostname with Ansible](https://www.derpturkey.com/setting-host-with-ansible-in-ubuntu/)
* [ansible.builtin.password – retrieve or generate a random password, stored in a file](https://docs.ansible.com/ansible/devel/collections/ansible/builtin/password_lookup.html)
* []()
* []()
* []()
* []()

### NGINX 
* [Prevent port change on redirect in nginx](https://serverfault.com/questions/227742/prevent-port-change-on-redirect-in-nginx)
* [how to stop dockerized nginx in foreground from flooding logs?](https://stackoverflow.com/questions/37429017/how-to-stop-dockerized-nginx-in-foreground-from-flooding-logs)
* []()
* []()
* []()
* []()

### Python
* [stackoverflow- ISO time (ISO 8601) in Python](https://stackoverflow.com/questions/2150739/iso-time-iso-8601-in-python?rq=1)
* [How to transform a timestamp in ms to datetime format?](https://community.graylog.org/t/how-to-transform-a-timestamp-in-ms-to-datetime-format/4996/4)
* []()
* []()
* []()
* []()

### Elastic stack
* [CptOfEvilMinions/BlogProjects](https://github.com/CptOfEvilMinions/BlogProjects/tree/master/ElasticStackv7)
* [Dockerhub - Elasticsearch](https://hub.docker.com/_/elasticsearch)
* [Dockerhub - Logstash](https://hub.docker.com/_/logstash)
* [Dockerhub - Kibana](https://hub.docker.com/_/kibana)
* [Set Password and user with Docker-compose](https://discuss.elastic.co/t/set-password-and-user-with-docker-compose/225075/2)
* [We opened X-Pack](https://www.elastic.co/what-is/open-x-pack)
* [Install Kibana with Docker](https://www.elastic.co/guide/en/kibana/current/docker.html)
* [Configuring Security in Logstash](https://www.elastic.co/guide/en/logstash/current/ls-security.html)
* [How to config Single node for Single Cluster (Standalone Cluster) ElasticSearch](https://stackoverflow.com/questions/16432300/how-to-config-single-node-for-single-cluster-standalone-cluster-elasticsearch)
* [Configure security in Kibanaedit](https://www.elastic.co/guide/en/kibana/current/using-kibana-with-security.html)
* [elasticsearch-setup-passwords](https://www.elastic.co/guide/en/elasticsearch/reference/current/setup-passwords.html)
* [How to setup password for elasticsearch users?](https://stackoverflow.com/questions/59644348/how-to-setup-password-for-elasticsearch-users)
* [Security settings in Elasticsearch](https://www.elastic.co/guide/en/elasticsearch/reference/current/security-settings.html)
* [Built-in users](https://www.elastic.co/guide/en/elasticsearch/reference/current/built-in-users.html)
* [Running Logstash on Docker](https://www.elastic.co/guide/en/logstash/current/docker.html)
* [How to add Certificate Authority file in CentOS 7](https://stackoverflow.com/questions/37043442/how-to-add-certificate-authority-file-in-centos-7)
* [Install Elasticsearch with Docker](https://www.elastic.co/guide/en/elasticsearch/reference/current/docker.html)
* [Docker Kibana env vars](https://www.elastic.co/guide/en/kibana/current/settings.html)
* [Is there a Kibana health API for load balancer?](https://discuss.elastic.co/t/is-there-a-kibana-health-api-for-load-balancer/124862/2)
* [Cluster health API](https://www.elastic.co/guide/en/elasticsearch/reference/current/cluster-health.html)
* [Elastic - Create or update users API - Request body](https://www.elastic.co/guide/en/elasticsearch/reference/current/security-api-put-user.html#security-api-put-user-request-body)
* [Elastic - Configuring Logstash to use Basic Authentication](https://www.elastic.co/guide/en/logstash/current/ls-security.html#ls-http-auth-basic)
* [Logstash - Mutate filter plugin](https://www.elastic.co/guide/en/logstash/current/plugins-filters-mutate.html#plugins-filters-mutate-lowercase)
* [If/else within Logstash output plugin](https://discuss.elastic.co/t/if-else-within-logstash-output-plugin/185965)
* []()
* []()

### Graylog 
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
* [Echo newline in Bash prints literal \n](https://stackoverflow.com/questions/8467424/echo-newline-in-bash-prints-literal-n)
* [Linux script to prompt for password](https://www.cyberciti.biz/faq/linux-script-to-prompt-for-password/)
* [BASH Programming - How to compare strings in Bash](https://linuxhint.com/compare_strings_bash/)
* [Why does the docker-compose healthcheck of my mongo container always fail?](https://stackoverflow.com/questions/54384042/why-does-the-docker-compose-healthcheck-of-my-mongo-container-always-fail)
* [ansible.builtin.pip – Manages Python library dependencies](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/pip_module.html)
* [community.mongodb.mongodb_user – Adds or removes a user from a MongoDB database](https://docs.ansible.com/ansible/latest/collections/community/mongodb/mongodb_user_module.html)
* [Localhost exception in MongoDB](https://dba.stackexchange.com/questions/184696/localhost-exception-in-mongodb)
* [StackOverFLow - I cannot login to mongodb after adding admin user and enabling authentication with ansible](https://stackoverflow.com/questions/56119867/i-cannot-login-to-mongodb-after-adding-admin-user-and-enabling-authentication-wi)
* [Only check whether a line present in a file (ansible)](https://stackoverflow.com/questions/30786263/only-check-whether-a-line-present-in-a-file-ansible/30788277)
* [Ansible - Using filters to manipulate data](https://docs.ansible.com/ansible/latest/user_guide/playbooks_filters.html)
* [ansible.builtin.password – retrieve or generate a random password, stored in a file](https://docs.ansible.com/ansible/devel/collections/ansible/builtin/password_lookup.html)
* [ElasticSearch crashing due to auto_create_index problem](https://community.graylog.org/t/elasticsearch-crashing-due-to-auto-create-index-problem/12600)
* [Elasticsearch - Create or update roles API](https://www.elastic.co/guide/en/elasticsearch/reference/current/security-api-put-role.html)
* [Elasticsearch - [security_exception] action [indices:data/read/search] is unauthorized for user [user]](https://discuss.elastic.co/t/security-exception-action-indices-data-read-search-is-unauthorized-for-user-user/164848/3)
* []()
* []()
* []()


### Splunk
* [Dockerhub - splunk/splunk](https://hub.docker.com/r/splunk/splunk/tags)
* [CptOfEvilMinions/MyLoggingPipeline](https://github.com/CptOfEvilMinions/MyLoggingPipeline/blob/master/conf/nginx/splunk_web.conf)
* [docker-splunk](https://splunk.github.io/docker-splunk/STORAGE_OPTIONS.html)
* [docker-splunk](https://splunk.github.io/docker-splunk/EXAMPLES.html#create-standalone-from-compose)
* [Repositories for APT and YUM](https://www.elastic.co/guide/en/apm/server/current/setup-repositories.html)
* [How to return exit code 0 from a failed command](https://stackoverflow.com/questions/36130299/how-to-return-exit-code-0-from-a-failed-command)
* [I want to pass credentials for a Splunk search](https://community.splunk.com/t5/Security/I-want-to-pass-credentials-for-a-Splunk-search/m-p/354345)
* [Set up and use HTTP Event Collector from the CLI](https://docs.splunk.com/Documentation/Splunk/7.3.2/Data/UseHECfromtheCLI)
* [Centos User account nologin but possible to su into account](https://serverfault.com/questions/337362/centos-user-account-nologin-but-possible-to-su-into-account/337379)
* [How To Install Elasticsearch, Logstash, and Kibana (Elastic Stack) on Ubuntu 20.04](https://www.digitalocean.com/community/tutorials/how-to-install-elasticsearch-logstash-and-kibana-elastic-stack-on-ubuntu-20-04)
* [https://docs.splunk.com/Documentation/Splunk/8.1.0/Admin/GethelpwiththeCLI](https://docs.splunk.com/Documentation/Splunk/8.1.0/Admin/GethelpwiththeCLI)
* [Splunk-docer: Valid Universal Forwarder Environment Variables](https://github.com/outcoldman/docker-splunk-splunk/blob/master/documentation/ADVANCED.md#valid-universal-forwarder-environment-variables)
* [Logstash - tcp output plugin does not send newlines #1650](https://github.com/elastic/logstash/issues/1650)
* [How to forward events from logstash to Splunk](https://medium.com/ibm-garage/how-to-forward-events-from-logstash-to-splunk-4f2608041feb)
* [Convert pkcs1 and pkcs8 format RSA private key to each other under linux command line](https://www.programmersought.com/article/8489444974/)
* [Mutate filter plugin](https://www.elastic.co/guide/en/logstash/current/plugins-filters-mutate.html)
* [Splunk Add-on for NetApp Data ONTAP](https://docs.splunk.com/Documentation/AddOns/released/NetApp/Configureinputs)
* [Github issue - Not able to disable XPack from Docker Compose #127](https://github.com/elastic/elasticsearch-docker/issues/127)
* []()
* []()
* []()