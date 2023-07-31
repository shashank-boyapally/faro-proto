# managed-services-deploy

This repository hosts playbooks to install and uninstall OpenShift Dedicated clusters using OCM. It also supports installing hypershift operator on the installed OSD to make it the management cluster and install desired number of hosted clusters ( leverages https://github.com/cloud-bulldozer/e2e-benchmarking/tree/master/workloads/hyper-scale )


# OpenShift Dedicated and HyperShift install on AWS
Refer [docs](docs/openshift_on_aws.md)

## Quickstart Usage Example

```
- Clone the repo
- Create an inventory file with the intended orchestration host
- Configure the install variables
- Run the install playbook for the desired environment
- Run the uninstall playbook for the desired environment

$ git clone https://github.com/chaitanyaenr/managed-services-deploy.git
$ cd managed-services-deploy
$ cp inventory.example inventory
$ # Edit inventory and add your expected orchestration host
$ # Edit deployment variables (Ex vi vars/install-common-vars.yml and vi vars/install-on-aws.yml) or define env variables - the following shell script can be used as a reference to set the environment variables: $ source sample_env.sh
$ ansible-playbook -v -i inventory install.yml -e platform=aws
$ ansible-playbook -v -i inventory uninstall.yml

```
