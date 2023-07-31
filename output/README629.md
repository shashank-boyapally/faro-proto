# redhat_chaos.kraken
This collection will contain content for automating kraken workloads

At this time, it is only a skeleton and we are working on a proof of concept for specifying kraken scenarios to run.

How to run current example:
```
$ ansible-playbook example.yaml -v

PLAY [localhost] *********************************************************************************************************************************************

TASK [Summon the kraken] *************************************************************************************************************************************
changed: [localhost] => {"changed": true, "module_args": {"exec_mode": "parallel", "fail_mode": "fast", "scenarios": [{"cmd": "podman run blah", "name": "foo"}, {"cmd": "stress 1000", "name": "bar"}]}, "ravi": true}

PLAY RECAP ***************************************************************************************************************************************************
localhost                  : ok=1    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
```

