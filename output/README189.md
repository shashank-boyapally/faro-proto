Deploy exporter to the node
===========================

This is Ansible role to deploy Prometheus exporter to a host. It downloads
provided exporter binary archive, unpacks it and creates, starts and enables
SystemD service file for it. It also opens firewall port for the exporter
and configures Prometheus server to scrape from the host (though Prometheus
configuration we are using is probably different to what you have, so this
part will need some work).

Variables
---------

We define this as part of the role, but can be overwritten if needed:

 * `exporters_dest` - where to extract/install exporters on the node

When calling the role, configure these variables:

 * `exporter_name` - name of the exporter
 * `exporter_url` - where to download the exporter tarball
 * `exporter_port` - port used by the exporter which will be opened on the node (also used by `add-prometheus-target` role)
 * `exporter_commandline` - how to start the exporter
 * `exporter_commandline_environment` - dict of environment for the exporter
 * `exporter_extra_roles` - list of roles to run after we have unpacked exporter archive - meant for config specific to one exporter
 * `prometheus_config` - file where to add new target to scrape (needed by `add-prometheus-target` role we use)

In inventory file, you also need `prometheus` group with one server (for `add-prometheus-target` role).

Example
-------

To deploy `node_exporter` and `process-exporter` to hosts in your `servers`
and `database` group, you can have a playbook like this:

    - hosts: servers database
      remote_user: root
      gather_facts: no
      tasks:
        - name: "Deploy Node exporter"
          include_role:
            name: deploy_exporter
          vars:
            exporter_name: node_exporter
            exporter_url: https://github.com/prometheus/node_exporter/releases/download/v1.0.1/node_exporter-1.0.1.linux-amd64.tar.gz
            exporter_port: 9100
            exporter_commandline: /usr/lib/node_exporter-1.0.1.linux-amd64/node_exporter
            prometheus_config: /root/prometheus/targets/cluster.yml

        - name: "Deploy Process exporter"
          include_role:
            name: deploy_exporter
          vars:
            exporter_name: process-exporter
            exporter_url: https://github.com/ncabatoff/process-exporter/releases/download/v0.7.5/process-exporter-0.7.5.linux-amd64.tar.gz
            exporter_port: 9256
            exporter_commandline: /usr/lib/process-exporter-0.7.5.linux-amd64/process-exporter -config.path /etc/process-exporter/config.yml -recheck -children=false
            exporter_extra_roles:
              - process_exporter_config
            prometheus_config: /root/prometheus/targets/cluster.yml

For process exporter you will need to create additional
`process_exporter_config` role that deploys `/etc/process-exporter/config.yml`
to the target host as well.

Make sure you are downloading only trusted content! Downloading random bits
from internet is bad for security at minimum.

Also note the versions above are probably already obsoleted, so make
sure to use recent versions.
