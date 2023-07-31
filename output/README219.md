# Jetstack

Jetstack is used for deploying OSP using director on IBM cloud

Pre-requisites:
===============

* Required OS should be installed based on OSP release on the undercloud
* The playbooks are intended to run from a RH VM as ansible jumphost
* Ansible >= 2.9
* Python 3.6+
* RHEL >= 7.8
* Passwordless sudo for user running the playbook on the ansible control node (host where the playbooks are being run from), since certain package installs are done

  Passwordless sudo can be setup as below:
  ```
  echo "username ALL=(root) NOPASSWD:ALL" | tee -a /etc/sudoers.d/username
  chmod 0440 /etc/sudoers.d/username
  ```
  The `username` should be the user that runs the playbook.

* Make sure the Baremetal servers on IBM cloud have admin privilege for IPMI
* Prepare the instackenv.json

Tested Hardware:
================

| Hardware             |
| -------------------- |
| Supermicro E5-2620   |

Note: Manually enable PXE on NIC3 on the overcloud nodes


Usage:
======

User needs to update the below vars in group_vars/all.yml

```
undercloud_ip: public ip of the undercloud
uc_ssh_pass: root password of the undercloud
registry_mirror: registry mirror
registry_namespace: registry namespace
```

To install undercloud

```
ansible-playbook undercloud.yml --ssh-extra-args '-R <port on the remote host>:<destination host which can be accessible from local host and traffic is forwarded to>:<destination host port>  <remote ssh user>@<remote source host>'
 -vvv --tags undercloud
```

To deploy overcloud

```
ansible-playbook overcloud.yml --ssh-extra-args '-R <port on the remote host>:<destination host which can be accessible from local host and traffic is forwarded to>:<destination host port>  <remote ssh user>@<remote source host>'
 -vvv --tags overcloud
```
