# Deprecated. Please see https://github.com/openshift-scale/scale-ci-upgrade

# scale-ci-upgrade

Automate the upgrade of an OpenShift cluster between minor versions.

## Usage

To run the upgrade follow these steps:  

* Clone the repository https://github.com/redhat-performance/scale-ci-upgrade.git

```
git cloine https://github.com/redhat-performance/scale-ci-upgrade
cd scale-ci-upgrade
```

* Copy the inventory to the current directory (because it will be modified).

```
cp /path/to/inventory ./upgrade-inventory
```

* Set some environment variables:
  * Cluster loader configuration directory:  `export cluster_loader_base_directory=cm`
  * Cluster loader configuration file:  `export cluster_loader_configuration=cm_01` (notice no extension provided)
  * The registry authentication user:  `export REG_AUTH_USER=username`
  * The registry authentication password:  `export REG_AUTH_PASSWORD=password`
  * See [all.yml](group_vars/all.yml) for more environment variables.

Then run the upgrade playbook.

```
ansible-playbook -vv -i upgrade-inventory upgrade.yml
```

The upgrade will take a working cluster install the new software repository and
the new openshift-ansible software. Edit the inventory file and start the
upgrade process.
