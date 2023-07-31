# Templates for deploying overcloud with R630 Node types

These templates can be used for deploying an overcloud with the following deploy
command:
```
 openstack overcloud deploy --templates -e
/usr/share/openstack-tripleo-heat-templates/environments/network-isolation.yaml
-e templates/network-environment.yaml -e templates/storage-environment.yaml
-e templates/deploy.yaml -r templates/roles_data.yaml --ntp-server clock.redhat.com
```

It is assumed that the command is executed from /home/stack and the
configuration files in this directory are all present in /home/stack/templates
on the undercloud.

These templates were built based on the assumption that the undercloud
provioning interface would be over em2. Be sure to set *local_interface = em2*
in the undercloud.conf when deploying the undercloud.

## Hardware Details

Each of the R630 node contains 4 NICs that can be used for an Overcloud
deployment: em1, em2, em3, and p2p1. All these NICs are 10G, em4 exists but is 1G
. We will make use of all the 10G NICs in our templates. Tenant, Internal API and
Storage ( along with Storage Management in the case of controllers) are all each
seperated out onto a different NIC. Note that we will still be using OVS brdiges
in some cases for compatibility and flexibility (to account for VLANed networks
in the case of tenant network).

## roles_data.yaml

This is the file where we define our composable *R630Compute* role. We have
basically just replaced the *Compute* role with *R630Compute* role. For ceph
nodes we replace *CephStorage* with *R630CephStorage*. Nothing else
changes here.

## network-environment.yaml

Since we defined a new role type *R630Compute*, we need to tell the installer
not only where it can find the nic-config templates for that role type, but also
how the ports on each of the networks in the role needs to be configured. The
section below is the one that does this magic of correctly linking the role to
its network configuration.

```
OS::TripleO::R630Compute::Net::SoftwareConfig: /home/stack/templates/nic-configs/r630-compute.yaml
OS::TripleO::R630Compute::Ports::ExternalPort: /usr/share/openstack-tripleo-heat-templates/network/ports/noop.yaml
OS::TripleO::R630Compute::Ports::InternalApiPort: /usr/share/openstack-tripleo-heat-templates/network/ports/internal_api.yaml
OS::TripleO::R630Compute::Ports::StoragePort: /usr/share/openstack-tripleo-heat-templates/network/ports/storage.yaml
OS::TripleO::R630Compute::Ports::StorageMgmtPort: /usr/share/openstack-tripleo-heat-templates/network/ports/noop.yaml
OS::TripleO::R630Compute::Ports::TenantPort: /usr/share/openstack-tripleo-heat-templates/network/ports/tenant.yaml
```
## storage-environment.yaml

This environment file is necessary for configuring the ceph nodes. */dev/sda* is
set as the root device using the serial number from the ironic introspection
data for each of the nodes desired to be ceph storage nodes. The NVME disk is
set as the journal and all others disks are configured to be OSDs. This template
also calls the *wipe-disks.yaml* template in *firstboot* folder to set the GPT
disk labels required by ceph.

## deploy.yaml

This sets the default parameters for node flavor and count. *R630ComputeCount*
sets the number of these composable compute nodes you want in your deplyoment.
*OvercloudR630ComputeFlavor* sets the falvor. We set it to compute in our
example but you could set it to anything you want as long as you have a
corresponding flavor already created and tagged to the nodes you want to use. We
set the flavor and count of the composable ceph nodes in a similar manner.

