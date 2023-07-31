Configure Prometheus server to scrape the exporter
==================================================

Variables
---------

When calling the role, configure these variables:

 * `inventory_hostname` - this is Ansible built-in variable and will be used to specify host to scrape
 * `exporter_port` - port used by the exporter which will be opened on the node
 * `prometheus_config` - file where to add new target to scrape

In inventory file, you also need `prometheus` group with one server.

Example
-------

    - name: "Scrape Tower exporter"
      include_role:
        name: add-prometheus-target
      vars:
        prometheus_config: /root/prometheus/targets/tower.yml
        exporter_port: 443
