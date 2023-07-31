# RDU-Scale Nic-Configs

Given the Scale lab has multiple system types, each connected different (some the same), we need to have customized templates per-node to give us greater flexibility and interface utilization.

## Configuration Details

### R730xd
The R730xds have 4 interfaces attached, our templates will deploy the following config:

#### Controller

|   Bridge   |  Interface     |   Networks                         |
|------------|:--------------:|-----------------------------------:|
| br-storage | em1            | StorageNetwork, StorageMgmtNetwork |
| br-tenant  | p4p1           | TenantNetwork                      |
| br-ex      | em2            | ControlPlane, ExternalNetwork      |                       
|            | p4p2           | InternalAPISubnet                  |

#### Compute

|   Bridge   |  Interface     |   Networks        |
|------------|:--------------:|------------------:|
| br-storage | em1            | StorageNetwork    |
| br-tenant  | p4p1           | TenantNetwork     |
| br-ex      | em2            | ControlPlane      |
|            | p4p2           | InternalAPISubnet |

#### Ceph

|   Bridge   |  Interface     |   Networks                            |
|------------|:--------------:|----------------------------------- --:|
| br-storage | em1            | StorageNetwork, StorageMgmtNetwork    |
| br-ex      | em2            | ControlPlane                          |
