# Vdpod
The vdpod is a container-based IO workload generator that is used as a performance testing tool that can be deployed on the Openshift/Kubernetes Platforms and is currently used within Red Hat [benchmark-runner](https://github.com/redhat-performance/benchmark-runner) which also supports VMs & Kata containers, this is a simplified version that can be run as a standalone pod without any dependencies or special requirements.

# Usage:
The following variables will contain the tests list information separated by a comma, the tests entered here will run consecutively and return a CSV results file: </br>

**BLOCK_SIZES** - can be either an application pattern (see applications patterns paragraph),block size , or a cache test that can be defined by adding " _cache" after the block size e.g "64_cache".<br/>
**IO_OPERATION** - can be either read, write or an application pattern if one was used in the BLOCK_SIZES variables.<br/>
**IO_THREADS** - the number of IO threads to run for every workload , more threads = more IOPS , but it will also yield higher latency.<br/>
**FILES_IO** - can be either random, sequential or an application pattern if one was used in the BLOCK_SIZES variables.<br/>
**IO_RATE** - can be any integer value for limiting the amount of IOPS , or "max" for no limit.<br/>
**MIX_PRECENTAGE** - mix of read/write precentage, meaning if IO_OPERATION = write , and MIX_PRECENTAGE=30 , that will results in a workload that does 30% writes and 60% reads of the the selected BLOCK_SIZES,

### Tests settings:<br/>
        - name: BLOCK_SIZES
          value: "oltp1,64,8,4_cache"
        - name: IO_OPERATION
          value: "oltp1,write,read"
        - name: IO_THREADS
          value: "10,5,12,32"
        - name: FILES_IO
          value: "oltp1,random,sequential,random"
        - name: IO_RATE
          value: "max,2000,max"
        - name: MIX_PRECENTAGE
          value: ",,50,"

the above example will execute the following 4 tests:<br/>
1. OLTP1 workload with 10 concurrent threads.<br/>
2. 64KB block size - doing 100% random writes, running with 5 concurrent threads, and limited to 2000 IOPS.
3. 8KB block size - doing 50% sequential reads and 50% sequential writes, and running with 12 concurrent IO threads.<br/>
4. 4KB block size - doing 100% random cache reads and running with 32 concurrent IO threads <br/>


### Global settings:<br/>
**DURATION** - run time duration per test in seconds.<br/>
**PAUSE** - pause duration in seconds after every test.<br/>
**WARMUP** - warmup duration is an additive to the DURATION, and will be added to all tests, warmup time statistics will be excluded from the CSV results file.<br/>
**FILES_SELECTION** - #This parameter allows you to select directories and files for processing either sequentially or randomly - value can be either random or sequential<br/>
**COMPRESSION_RATIO** - this paramater will determine how compressible the generted IO will be ratio is 1:X e.g 2 = 50% compressible
**RUN_FILLUP** - will fill the workset with random data before starting the tests.

### Data set settings:
**DIRECTORIES** - how many directories to create.<br/>
**FILES_PER_DIRECTORY** - how many files create in each directory.<br/>
**SIZE_PER_FILE** - size in MB for each file created.<br/>
for example - when setting DIRECTORIES=10, FILES_PER_DIRECTORY=5, and SIZE_PER_FILE=20, the total work set size will be 30TB.

# Applications patterns:
**OLTP1** - mail applications, online transaction processing.<br/>
**OLTP2** - small Oracle applications, small weight transactions.<br/>
**OLTPHW** -large Oracle applications, heavy weight transactions.<br/>
**ODSS2** - data warehouse applications, backup applications.<br/>
**ODSS128** - streaming applications, backup applications.<br/>

more info about application patterns can be found [here](https://cloud.redhat.com/blog/software-design-pattern-benchmarking).<br/>

# How to run:.<br/>
if you have quay.io access all you need is the vdpod.yaml file, of course, you will need to set your wanted tests and storage class:.<br/>

```
spec:
  accessModes:
    - ReadWriteOnce
  storageClassName: ocs-storagecluster-ceph-rbd
  resources:
    requests:
      storage: 64Gi
```

note that in the above example I used the ceph storage class..<br/>
you may also run the pod locally with podman, here is an example of how to run it locally with podman with a few defined tests:.<br/>
```
podman run -v /workload:/workload -e BLOCK_SIZES=oltp1,oltp2,oltphw,odss2,odss128,4_cache,64_cache,4,64,4_cache,64_cache,4,64,64 -e IO_OPERATION=oltp1,oltp2,oltphw,odss2,odss128,read,read,read,read,write,write,write,write,read,write -e IO_THREADS=5,5,5,5,5,4,4,2,2,4,4,2,2,5,5 -e FILES_IO=oltp1,oltp2,oltphw,odss2,odss128,random,random,random,random,random,random,random,random,random,random -e IO_RATE=max,max,max,max,max,max,max,max,max,max,max,max,max,max,max -e MIX_PRECENTAGE= -e DURATION=20 -e PAUSE=0 -e WARMUP=0 -e FILES_SELECTION=random -e COMPRESSION_RATIO=2 -e RUN_FILLUP=no -e SIZE_PER_FILE=10 -e DIRECTORIES=10 -e FILES_PER_DIRECTORY=3 -v /root/vdpod:/vdpod/config -it quay.io/bbenshab/vdpod:latest
```
# Results:<br/>
The CSV results table will show on the pods logs once the all tests were completed - e.g ```oc logs pod_name```
