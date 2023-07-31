# Template Files

The contents of this folder are intended to be used for launching the OpenBLAS benchmark app in OpenShift on AWS, but you may also use it for a non-AWS OpenShift instance.

The "standard" folder contains templates necessary for launching a basic OpenBLAS image and build job, while the "nfd" folder contains necessary templates for launching an OpenBLAS image and build job using [Node Feature Discovery](https://github.com/kubernetes-sigs/node-feature-discovery). To install Node Feature Discovery (NFD) on your OpenShift cluster, see https://github.com/openshift/cluster-nfd-operator.

## "Standard" Folder Files

### openblas-buildconfig\_rhel7.yaml and openblas-buildconfig\_rhel8.yaml

These yaml files contain templates used for creating a BuildConfig and ImageStream in RHEL 7 and 8, respectively. Both yaml files have parameters `IMAGESTREAM_NAME`, which will be the name of the OpenBLAS image when it is saved to your OpenShift instance, and `REGISTRY`, which is the name fo your Docker/CRI-O registry.

### openblas-build-job.yaml

This yaml file contains a template used for calling S2I. It has two parameters: (1.) `IMAGESTREAM_NAME`, (2.) `REGISTRY`, (3.) `APP_NAME`, and (4.) `NAMESPACE`. The first two parameters in this template are the same as the two parameters in the previous template. The third parameter is the name of your app (e.g., `openblas-gemm-s2i-app`) and the fourth parameter is the OpenShift namespace/project you're working on (see `oc project`).

## "NFD" Folder Files

### openblas-nfd-buildconfig\_rhel7.yaml and openblas-nfd-buildconfig\_rhel8.yaml

These files are the same as `standard/openblas-buildconfig_rhel7.yaml` and `standard/openblas-buildconfig_rhel8.yaml`, except they have an added `nodeSelectorTerms` feature to choose whether to build on a node with AVX/AVX2/AVX512. (Note: requires NFD to be installed on your cluster!) There are `openblas-buildconfig_rhel7.yaml` and `openblas-buildconfig_rhel8.yaml` for each AVX instruction set, including "No AVX."


### openblas-nfd-build-job.yaml

This file is the same as `standard/openblas-build-job.yaml`, except with the added `nodeSelectorTerms` feature, much like `nfd/openblas-nfd-buildconfig_rhel7.yaml` and `nfd/openblas-nfd-buildconfig_rhel8.yaml`. Similar to above, this file exists for each AVX instruction set, including "No AVX."
