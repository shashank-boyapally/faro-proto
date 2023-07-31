# OpenShift Dedicated on AWS
The variable file can be found at [vars/install-on-aws.yml](../vars/install-on-aws.yml) and [vars/install-common-vars.yml](../vars/install-common-vars.yml). It will configure the deployment playbook at install.yml to perform a cluster installation on AWS.


## Usage
```
$ cp inventory.example inventory
$ # Edit inventory and add your expected orchestration host
$ # Edit deployment variables or define env variables
$ ansible-playbook -vv -i inventory install.yml -e platform=aws
$ ansible-playbook -vv -i inventory uninstall.yml
```

## Environment variables
Vars in [vars/install-on-aws.yml](../vars/install-on-aws.yml) and [vars/install-common-vars.yml](../vars/install-common-vars.yml) can be defined as environment variables on the host that you will be running the playbooks. [vars/install-common-vars.yml](../vars/install-common-vars.yml) are generic to any cloud platform and [vars/install-on-aws.yml](../vars/install-on-aws.yml) vars are specific to the cloud provider to be able to talk to the respective API.


### AWS_ACCESS_KEY_ID
Default: No default.  
The AWS access key.

### AWS_SECRET_ACCESS_KEY
Default: No default.  
The AWS secret access key.

### AWS_REGION
Default: us-west-2  
The AWS region to install on to.

### AWS_ACCOUNT_ID
Default: No default.  
Account ID

### OPENSHIFT_CLEANUP
Default: false  
Cleans up the duplicate cluster matching the CLUSTER_NAME if exists

### OPENSHIFT_INSTALL
Default: true  
Installs cluster

### OCM_URL
Default: https://api.stage.openshift.com/  
OCM URL to connect to

### OCM_API_TOKEN
Default: No default.  
API token to login into your console.redhat.com or OCM account

### CCS_ENABLED
Default: true

### CLUSTER_NAME
Default: No default  
Name of the cluster

### MANAGED
Default: true

### MULTI_AZ
Default: true  
Sets up workers in multiple availability zones when enabled

### COMPUTE_COUNT
Default: 3  
Number of computer/worker nodes in the cluster

### COMPUTE_MACHINE_TYPE
Default: m5.2xlarge  
Machine type or flavor for the worker/compute nodes in AWS

### NETWORK_TYPE
Default: OVNKubernetes

### OPENSHIFT_VERSION
Default: openshift-v4.11.0-rc.5-x86_64-candidate
OpenShift version to install

### KUBECONFIG
Default: /root/.kube/config  
Location to copy the kubeconfig of the cluster

-----------------------------------------------
HYPERSHIFT VARIABLES
-----------------------------------------------
### HYPERSHIFT_INSTALL
Default: true

### HYPERSHIFT_CLEANUP
Default: false

### ROSA_ENVIRONMENT
Default: staging
Environment to use

### PULL_SECRET
Default: no default  
pull secret for cluster installs

### NUMBER_OF_HOSTED_CLUSTER
Default: 2  
Number of clusters to install on the management cluster

### COMPUTE_WORKERS_NUMBER
Default: 2  
Number of worker nodes per hosted cluster

### NETWORK_TYPE
Default: OVNKubernetes  
Network plugin to use for the hosted clusters

### REPLICA_TYPE
Default: HighlyAvailable  
This will setup replicas in different zones to be HA

### RELEASE_IMAGE
Default: quay.io/openshift-release-dev/ocp-release:4.11.0-rc.1-x86_64  
Hosted cluster version

### CPO_IMAGE
Default: quay.io/hypershift/hypershift:latest

### HYPERSHIFT_OPERATOR_IMAGE
Default: quay.io/hypershift/hypershift-operator:4.11

### HYPERSHIFT_CLI_INSTALL
Default: true  
Install hypershift client

### HYPERSHIFT_CLI_VERSION
Default: release-4.11

### HYPERSHIFT_CLI_FORK
Default: https://github.com/openshift/hypershift

------------------------------------
THANOS
------------------------------------

### THANOS_ENABLE
Default: false

### THANOS_RECEIVER_URL
Default: no default
