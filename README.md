# Choose your own SIEM adventure
Repo of configs for the three major SIEMs. 

## Default password
<span style="color:red;">Default password is set to `Changem123!`, see instructions in `docs/`</span>

## Generate public cert and private key
1. `openssl req -x509 -nodes -days 3650 -newkey rsa:2048 -keyout conf/tls/docker.key -out conf/tls/docker.crt`

## Elasticsearch setting heap size
The Ansible playbooks will automatically set the heap size to half of total system memory allocated to a host. For example, if a machine has `16GB` of memory, the ES heap size will be set to `8GB`.

## Supported versions
* `Graylog v3.3`
* `Elastic v7.9`
* `Splunk v7.0.8`
* `Ansible v2.11+`
* `Ubuntu 20.04 64-bit`

## References
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
* []()
* []()

### NGINX 
* [Prevent port change on redirect in nginx](https://serverfault.com/questions/227742/prevent-port-change-on-redirect-in-nginx)
* []()
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

