# Cerberus API Client

A Python package to scrape OpenShift/Kubernetes cluster failures stored in SQLite database. It can be used with the [Cerberus](https://github.com/openshift-scale/cerberus) tool.

### Installation
To install the lastest release:

`pip3 install cerberus-api-client`


### Submodules

#### cerberus_api_client.client.custom_query_loopback module
`custom_query_loopback(database, loopback=60, issue="", name="", component="")`

Retrieve the failures satisfying the criteria specified by parameters in the past `loopback` minutes in the json format.

Parameters:
- database: (str) Path where cerberus database is stored.
- loopback: (int) Time in minutes.
- issue: (list) A list of issue types.
- name: (list) A list of component names (e.g. pod names, node names).
- component: (list) A list of component types.

#### cerberus_api_client.client.custom_query_interval module
`custom_query_interval(database, start_time="", finish_time="", issue="", name="", component="")`

Retrieve the failures between `start_time` and `finish_time` that satisfy the criteria specified by parameters in the json format.

Parameters:
- database: (str) Path where cerberus database is stored.
- start_time: (timestamp) Timestamp in `%Y-%m-%d %H:%M:%S` format.
- finish_time: (timestamp) Timestamp in `%Y-%m-%d %H:%M:%S` format.
- issue: (list) A list of issue types.
- name: (list) A list of component names (e.g. pod names, node names).
- component: (list) A list of component types.
