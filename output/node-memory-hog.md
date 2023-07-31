### Node Memory hog scenario
This scenario hogs the memory on the specified node on a Kubernetes/OpenShift cluster for a specified duration. For more information refer the following [documentation](https://github.com/redhat-chaos/krkn/blob/main/docs/arcaflow_scenarios/memory_hog.md).

#### Run
If enabling [Cerberus](https://github.com/redhat-chaos/krkn#kraken-scenario-passfail-criteria-and-report) to monitor the cluster and pass/fail the scenario post chaos, refer [docs](https://github.com/redhat-chaos/krkn-hub/tree/main/docs/cerberus.md). Make sure to start it before injecting the chaos and set `CERBERUS_ENABLED` environment variable for the chaos injection container to autoconnect.

```
$ podman run --name=<container_name> --net=host --env-host=true -v <path-to-kube-config>:/root/.kube/config:Z -d quay.io/redhat-chaos/krkn-hub:node-memory-hog
$ podman logs -f <container_name or container_id> # Streams Kraken logs
$ podman inspect <container-name or container-id> --format "{{.State.ExitCode}}" # Outputs exit code which can considered as pass/fail for the scenario
```

```
$ docker run $(./get_docker_params.sh) --name=<container_name> --net=host -v <path-to-kube-config>:/root/.kube/config:Z -d quay.io/redhat-chaos/krkn-hub:node-memory-hog
OR 
$ docker run -e <VARIABLE>=<value> --net=host -v <path-to-kube-config>:/root/.kube/config:Z -d quay.io/redhat-chaos/krkn-hub:node-memory-hog

$ docker logs -f <container_name or container_id> # Streams Kraken logs
$ docker inspect <container-name or container-id> --format "{{.State.ExitCode}}" # Outputs exit code which can considered as pass/fail for the scenario
```

#### Supported parameters

The following environment variables can be set on the host running the container to tweak the scenario/faults being injected:

ex.) 
`export <parameter_name>=<value>`


See list of variables that apply to all scenarios [here](all_scenarios_env.md) that can be used/set in addition to these scenario specific variables

Parameter               | Description                                                           | Default
----------------------- | -----------------------------------------------------------------     | ------------------------------------ |
TOTAL_CHAOS_DURATION    | Set chaos duration (in sec) as desired                                | 60                                  |
MEMORY_CONSUMPTION_PERCENTAGE | percentage  (expressed with the suffix %) or amount (expressed with the suffix b, k, m or g) of memory to be consumed by the scenario | 90% |
NUMBER_OF_WORKERS       | Total number of workers (stress-ng threads)   | 1    |
NAMESPACE | Namespace where the scenario container will be deployed | default |
NODE_SELECTORS | Node selectors where the scenario containers will be scheduled in the format "`<selector>=<value>`". __NOTE__: This value can be specified as a list of node selectors separated by "`;`". Will be instantiated a container per each node selector with the same scenario options. This option is meant to run one or more stress scenarios simultaneously on different nodes, kubernetes will schedule the pods on the target node accordingly with the selector specified. Specifying the same selector multiple times will  instantiate as many scenario container as the number of times the selector is specified on the same node| "" |                              


**NOTE** In case of using custom metrics profile or alerts profile when `CAPTURE_METRICS` or `ENABLE_ALERTS` is enabled, mount the metrics profile from the host on which the container is run using podman/docker under `/root/kraken/config/metrics-aggregated.yaml` and `/root/kraken/config/alerts`. For example:
```
$ podman run --name=<container_name> --net=host --env-host=true -v <path-to-custom-metrics-profile>:/root/kraken/config/metrics-aggregated.yaml -v <path-to-custom-alerts-profile>:/root/kraken/config/alerts -v <path-to-kube-config>:/root/.kube/config:Z -d quay.io/redhat-chaos/krkn-hub:container-scenarios
```

#### Demo
You can find a link to a demo of the scenario [here](https://asciinema.org/a/452742?speed=3&theme=solarized-dark)
