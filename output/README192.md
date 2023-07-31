Create and Destroy IBM Cloud Instances
=======================================

This repo includes playbooks to provision and deprovision instances on IBM Cloud.

Additionally, it can install component of the Ansible Automation Platform on those instances.
Currently, that is limited to Automation Controller, but this framework can be extended.

The original motiviation of this automation was to provision hosts for and install Automation Controller, as increased
disk IOPs requirements for Automation Controller 4.0+ motivated us to migrate from in-house VMs.

We believe there are two use cases associated with this repo
1. Looking for plain virtual cloud instances (OR)
2. Looking for Tower/Automation Platform deployment on faster disks

Looking for plain virtual cloud instances ??
------------------------------------

Install Ansible modules collection for IBM cloud

    ansible-galaxy collection install ibm.cloudcollection

Install IBM Cloud CLI tool to see the available instance-profiles(m4.large, m4.xlarge), OS-images, and etc...

    curl -sL https://raw.githubusercontent.com/IBM-Cloud/ibm-cloud-developer-tools/master/linux-installer/idt-installer | bash

    ibmcloud plugin install vpc-infrastructure

Make sure you have IBM Cloud API key to authenticate with the IBM Cloud platform.

Create an `IC_API_KEY` env variable

    export IC_API_KEY="<your-api-key>"

Login to IBM cloud and list the available geographical regions under your account

      ibmcloud login

      ibmcloud regions

      ibmcloud target -r jp-tok #point to new targeted region

```
[cmusali@cmusali ibm_cloud_tower_deploy]$ ibmcloud login
API endpoint: https://cloud.ibm.com
Region: jp-tok
Authenticating...
OK

Targeted account Performance-Scale (XXXXXXXXXXXXXXXXX)


API endpoint:      https://cloud.ibm.com
Region:            jp-tok
User:              ServiceId-XXXXXXXXXXXXXXXXXXxx
Account:           Performance-Scale (XXXXXXXXXXXXXXXXXX)
Resource group:    No resource group targeted, use 'ibmcloud target -g RESOURCE_GROUP'
CF API endpoint:
Org:
Space:

[cmusali@cmusali ibm_cloud_tower_deploy]$ ibmcloud regions
Listing regions...

Name       Display name
au-syd     Sydney
in-che     Chennai
jp-osa     Osaka
jp-tok     Tokyo
kr-seo     Seoul
eu-de      Frankfurt
eu-gb      London
ca-tor     Toronto
us-south   Dallas
us-east    Washington DC
br-sao     Sao Paulo
```

List instance profiles in the region `jp-tok`

    ibmcloud is instance-profiles

```
Listing instance profiles in region jp-tok under account Performance-Scale as user ServiceId-XXXXXXXXXXXXXXXXX...
Name            Architecture   Family     vCPUs   Memory(GiB)   Bandwidth(Mbps)   Volume bandwidth(Mbps)   GPUs   Storage(GB)
bx2-2x8         amd64          balanced   2       8             4000              1000                     -      -
bx2d-2x8        amd64          balanced   2       8             4000              1000                     -      1x75
bx2-4x16        amd64          balanced   4       16            8000              2000                     -      -
bx2d-4x16       amd64          balanced   4       16            4000              1000                     -      1x150
bx2-8x32        amd64          balanced   8       32            16000             4000                     -      -
bx2d-8x32       amd64          balanced   8       32            16000             4000                     -      1x300
bx2-16x64       amd64          balanced   16      64            32000             8000                     -      -
bx2d-16x64      amd64          balanced   16      64            32000             8000                     -      1x600
bx2-32x128      amd64          balanced   32      128           64000             16000                    -      -
bx2d-32x128     amd64          balanced   32      128           64000             16000                    -      2x600
```

List all the available images in the region `jp-tok`

    ibmcloud is images


```
Listing images in all resource groups and region jp-tok under account Performance-Scale as user ServiceId-8cd111e5-14e8-4f45-897b-27d440a90012...
ID                                          Name                                               Status       Arch    OS name                              OS version                                File size(GB)   Visibility   Owner type   Encryption   Resource group
r022-f10e4ea0-1f0b-4fb6-8cfd-1c9aad475046   ibm-centos-7-9-minimal-amd64-3                     available    amd64   centos-7-amd64                       7.x - Minimal Install                     1               public       provider     none         -
r022-95e7a9a1-8707-49ea-bdef-693311570ce0   ibm-centos-8-3-minimal-amd64-3                     available    amd64   centos-8-amd64                       8.x - Minimal Install                     1               public       provider     none         -
r022-0fd54b16-2f03-4f8c-8045-38f9781e9071   ibm-debian-10-8-minimal-amd64-1                    available    amd64   debian-10-amd64                      10.x Buster/Stable - Minimal Install      1               public       provider     none         -
r022-54098fbc-4285-4fc3-aa20-d9da85781fa5   ibm-debian-9-13-minimal-amd64-4                    available    amd64   debian-9-amd64                       9.x Stretch/Stable - Minimal Install      1               public       provider     none         -
r022-f5387730-7a4b-4f71-9a85-13b05b137953   ibm-redhat-7-6-amd64-sap-applications-1            available    amd64   red-7-amd64-sap-applications         7.x for Applications                      2               public       provider     none         -
r022-60d279a0-b328-40eb-a379-595ca53bee18   ibm-redhat-7-6-amd64-sap-hana-1                    available    amd64   red-7-amd64-sap-hana                 7.6 for SAP HANA                          2               public       provider     none         -
r022-71ecd746-b847-4fc4-8144-1ad5ca7095fc   ibm-redhat-7-9-minimal-amd64-3                     available    amd64   red-7-amd64                          7.x - Minimal Install                     1               public       provider     none         -
```

Launch Plain IBM Cloud Instances
---------------------------------

Run the `ansible-playbook` command with following `EXTRA` cmdline arguments

    ansible-playbook create.yml -e ibmcloud_vsi_count=2 \
                                -e ibmcloud_vpc_name_prefix='perf-scale-test'
```
TASK [Print IBM Cloud Instance Floating IPs] ***************************************************************************************************************************************
ok: [localhost] => {
    "msg": [
        "IC instance Floating IP: ",
        [
            "169.63.178.143",
            "169.59.164.19"
        ]
    ]
}
```
```
[cmusali@cmusali ibm_cloud_tower_deploy]$ cat > ic_instance_inventory.ini
[ic_servers]
ic1 ansible_host=169.63.178.143
ic2 ansible_host=169.59.164.19


[ic_servers:vars]
ansible_user = 'root'
ansible_ssh_private_key_file=conf/towerperf_id_rsa
^C
```

Destroy IBM Cloud Instances
----------------------------

Run the `ansible-playbook` command with following `EXTRA` cmdline arguments

    ansible-playbook cleanup.yml -e ibmcloud_vsi_count=2 \
                                 -e ibmcloud_vpc_name_prefix='perf-scale-test'

Looking for 3.8.z Tower deployment on faster disks
---------------------------------------------

Run the `ansible-playbook` command with following `EXTRA` cmdline arguments

    ansible-playbook create.yml -e ibmcloud_vpc_name_prefix='perf-scale-test'
                                -e scenario=legacy-38-cluster-with-isolated-nodes # or legacy-38-cluster if no isolated nodes desired

Looking for 4.0.z Automation Controller deployment on faster disks
---------------------------------------------

Run the `ansible-playbook` command with following `EXTRA` cmdline arguments

    ansible-playbook create.yml -e ibmcloud_vsi_count=2 \
                                -e ibmcloud_vpc_name_prefix='perf-scale-test'
                                -e scenario=legacy-40-cluster

Looking for 4.1+ Automation Controller deployment on faster disks
---------------------------------------------

Automation Controller 4.1 introduces a number of new node types, being:

hybrid nodes -- have control and execution capabilities
execution nodes -- have execuiton capabilities
control nodes -- have only control capabilities
hop nodes -- serve as a bastion host in the receptor network, have neither control nor execution capabilities

In order to encapsulate the number of different topologies one might want to deploy, named "scenarios" have been
introduced. Scenarios are described and can be edited/added to in "deploy_aap_vars.yml".

For example, two simple toplogies are,

    "single-hybrid":
      hybrid_nodes: 1
      inventory_template: "inventory_cluster_4.1.j2"
      install_aap: True
    "single-control-single-execution":
      control_nodes: 1
      execution_nodes: 1
      inventory_template: "inventory_cluster_4.1.j2"
      install_aap: True

To deploy the single-control-single-execution scenario, Run the `ansible-playbook` command with following `EXTRA` cmdline arguments

    ansible-playbook create.yml -e ibmcloud_vpc_name_prefix='perf-scale-test'
                                -e scenario=single-contorl-single-execution


Destroy IBM Cloud Instances If Tower/Controller is Deployed
------------------------------------------------

Run the `ansible-playbook` command with following `EXTRA` cmdline arguments

    ansible-playbook cleanup.yml  -e ibmcloud_vpc_name_prefix='perf-scale-test' \
                                  -e scenario=single-contorl-single-execution # same scenario you used to deploy

To Take Control Over the Default Configuration Values
------------------------------------------------------

If the `scenarios` do not meet your use cases, and you want to set everything yourself -- you can do so with the `scenario=custom`
or just not defining `scenario`. (In jenkins, `scenario` is always defined, hence the `custom` scenario.
Default confing file `vars.yml`

    ibmcloud_vpc_region: 'jp-tok'  # Region for creating IBM cloud instances
    ibmcloud_vpc_name_prefix: 'perf-scale-test'  # Used as prefix when creating various resources
    ibmcloud_vsi_profile: 'bx2-4x16'   # Type of IBM cloud instance, balanced 2 vCPUs and 16 GiB Memory
    ibmcloud_image: 'rhel_8.3' # OS image name, see vars.yml for mapping to ID in each region
    ibmcloud_vsi_count: 3 # Number of required IBM cloud instances
    list_of_ports: [22, 80, 443] # List of ports to open on the IBM cloud instances
