# perfscale-jupyter-notebooks

Jupyter Notebooks used by the Performance & Scale Organization

This page contains files to automate visualizations using jupyter notebooks using Touchstone.

There are 2 different function that can be called by Touchstone

1) Provides vast amounts of data that is mostly used for calling data with timestamps. This data can not use the aggregate function in the JSON file.

2) Retrieves data upto 10k records with aggregation function


Below is an example of how to use touchstone with jupyter notebooks

Provide the following details:

    uuid="aeed6306-b7e1-11eb-b313-e86a640406b2"
    database="elasticsearch"
    es_index = "ocm-requests"
    es_url = os.environ.get('ES_URL')
    benchmark = Benchmark(open("ocm-requests.json"), database)

Touchstone (original function call in jupyter):

  1) This is specified by calling the conn.emit_compute_dict function
  2) Can create aggregations and filter data through touchstone
  3) Limit of 10k records
  4) Returns nested dictionary

  example:

    for compute in benchmark.compute_map['ocm-requests'] :
        conn=databases.grab(database,es_url)
        result=conn.emit_compute_dict(uuid,
                                      compute,
                                      "ocm-requests",
                                      "uuid")
        mergedicts(result,main)


Touchstone (new function call in jupyter):

  1) This is specified by calling the database_instance.get_timeserices_results
  2) Does not have a limit of 10k
  3) return a dictionary
  4) JSON file must contain "timeseries": true statement

  example:

    for compute in benchmark.compute_map['ocm-requests'] :
      timeseries_result1 = database_instance.get_timeseries_results(uuid=uuid,
                                                                   compute_map = compute,
                                                                   index = "ocm-requests",
                                                                   identifier="uuid"
                                                                  )
      df = pd.DataFrame(timeseries_result1)

## Building contaioner image

To build the image

`podman build --tag quay.io/cloud-bulldozer/jupyterlab:v$(cat VERSION) -f ci/images/Dockerfile`

To run

`podman run --rm -p 8888:8888 localhost/jupyterlab:v$(cat VERSION)`
