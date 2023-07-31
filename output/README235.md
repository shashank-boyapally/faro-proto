Container images to be used as a fake Red Hat Satellite 6 clients
=================================================================

Disclamer: These images are strictly meant for testing and are altered
(see below about renaming) in a way that subscriptions does not work
the way they are supposed to in them (normally containers should inherit
subscriptions from the host running the container). Also security is
a concern here (e.g. allowing root ssh login via password might be
questionable).

Usage
-----

Because while the container starts, files `/etc/rhsm-host`
and `/etc/pki/entitlement-host` are renamed, you can easilly register
the container to Red Hat Satellite using `subscription-manager register`
and work with subscriptions in a same way you would do on a regular machine.

Container also starts `sshd` so it can be accessed in a same way as
a regular machine (e.g. via Ansible or Satellite's remote execution feature).

Setting up a networking in a way that you have container IP available
from external network is a different story. E.g. see https://jhutar.blogspot.com/2016/05/running-dockerd-on-vm-co-containers-can.html

Building and running
--------------------

When building the container image, you can specify root password
and root public key (that will be placed into `/root/.ssh/authorized_keys`).
See `build.sh` file for specific commands.

To start the container:

    sudo podman run -d -p 22 --privileged=true <image>

Then you can get its IP with:

    sudo podman inspect <image> | grep IPAddress

Tested on RHEL7 with `docker-1.10.3-59.el7.x86_64`.

Note: I was not able to run ubi7 based containers on my Fedora 33 system.
Asking about that in https://lists.podman.io/archives/list/podman@lists.podman.io/thread/A3JKWAHCB4P2EDQC5XGXJQXKSRBPZJ7D/

Flavors
-------

| Containerfile                        | OS    | base image | description |
| ------------------------------------ | ----- | ---------- | ----------- |
| `rhel8-ubi-init-smallest.Containerfile` | RHEL8 | ubi8/ubi-init | Just basic set of packages to run `sshd` and `subscription-manager` |
| `rhel8-ubi-init-smallest-foreman_ygg_worker.Containerfile` | RHEL8 | rhel8-ubi-init-smallest | This adds foreman_ygg_worker related client packages (as of now, it's `foreman_ygg_worker` and its dependencies) to the mix |
| `rhel8-ubi-init-smallest-RHC.Containerfile` | RHEL8 | rhel8-ubi-init-smallest | Adds RHC (i.e. `rhc` and `rhc-worker-playbook` packages) to the mix to be able to remediate from ConsoleDot |
| `rhel8-ubi-init-big_updated.Containerfile` | RHEL8 | rhel8-ubi-init-smallest | Added extra repository with fake packages and used it to install packages so total number of packages installed is 1000 |
| `rhel8-ubi-init-big_outdated.Containerfile` | RHEL8 | rhel8-ubi-init-smallest | Added extra repository with fake packages and install quite some outdated packages from it so total number of packages is 1000 and it have around 815 applicable updates |
| `rhel8-ubi-init-utils.Containerfile` | RHEL8 | rhel8-ubi-init-smallest | Small image which, besides other, contain various helper tools handy when debugging the setup we are using |
| `rhel8-ubi-init-big_outdated-katello_agent611.Containerfile` | RHEL8 | rhel8-ubi-init-big_outdated | This adds katello related client packages (as of now, it's `katello-agent` and its dependencies) to the mix |
| `rhel8-ubi-init-big_outdated-satellite_client.Containerfile` | RHEL8 | rhel8-ubi-init-big_outdated | Added Satellite client packages (as of now, it's `foreman_ygg_worker`, `katello-agent` and their dependencies) to the mix |
| `rhel7-ubi-init-smallest.Containerfile` | RHEL7 | ubi7/ubi-init | Just basic set of packages to run `sshd` and `subscription-manager` |
| `rhel7-ubi-init-big_updated.Containerfile` | RHEL7 | rhel7-ubi-init-smallest | Added extra repository with fake packages and used it to install packages so total number of packages installed is 1000 |
| `rhel7-ubi-init-big_outdated.Containerfile` | RHEL7 | rhel7-ubi-init-smallest | Added extra repository with fake packages and install quite some outdated packages from it so total number of packages is 1000 and it have around 815 applicable updates |

Links
-----

Some random links about the topic of runninng systemd in a container:

* [blog with example of systemd container](https://www.redhat.com/sysadmin/session-recording-tlog)
* [infor about UBI8 images](https://developers.redhat.com/blog/2019/05/31/working-with-red-hat-enterprise-linux-universal-base-images-ubi/)
* [UBI yum repositories CDN](https://cdn-ubi.redhat.com/content/public/ubi/dist/)
* [how to run systemd in container](https://developers.redhat.com/blog/2019/04/24/how-to-run-systemd-in-a-container/)
* [getting ubi8/ubi-init image](https://catalog.redhat.com/software/containers/ubi8/ubi-init/5c359b97d70cc534b3a378c8?container-tabs=gti&gti-tabs=unauthenticated)
* [getting ubi7/ubi-init image](https://catalog.redhat.com/software/containers/ubi7/ubi-init/5c3596d7dd19c775cddfa784?container-tabs=gti&gti-tabs=unauthenticated)
* [getting rhel6-init image](https://catalog.redhat.com/software/containers/rhel6-init/59b6be2029373872cf9bfa8e?container-tabs=gti&gti-tabs=unauthenticated)
