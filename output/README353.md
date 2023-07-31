# Perfscale public cloud resources

## Building the AWS AMI

Hashicorp's Packer is required to build this AMI, you can download it from the [Packer website](https://www.packer.io/downloads)
Once you've got the binary, build the image with:

```shell
$ export aws_region=us-west-2                   # This is the region where our AMI will be created
$ export subnet_id=subnet-02b30be5f19619199     # This subnet should be public accesible in the selected region
$ packer build template.json
```

> Note: By default, Packer will use the configured AWS credentials on your system (you can configre then using `aws configure`), you can overwrite them through the env vars `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY`

Once packer finishes, the AMI should be available in our AWS account:

```shell
$ aws ec2 describe-images --filters Name=name,Values=perfscale-fedora
{
    "Images": [
        {
            "Architecture": "x86_64",
            "CreationDate": "2021-01-12T11:12:11.000Z",
            "ImageId": "ami-060e6ae19677ee7bf",
            "ImageLocation": "415909267177/perfscale-fedora",
            "ImageType": "machine",
            "Public": false,
            "OwnerId": "415909267177",
            "PlatformDetails": "Linux/UNIX",
            "UsageOperation": "RunInstances",
            "State": "available",
            "BlockDeviceMappings": [
                {
                    "DeviceName": "/dev/sda1",
                    "Ebs": {
                        "DeleteOnTermination": true,
                        "SnapshotId": "snap-0f9611fe7dfd9e9cc",
                        "VolumeSize": 6,
                        "VolumeType": "gp2",
                        "Encrypted": false
                    }
                }
            ],
            "Description": "Perfscale Team Fedora based AMI",
            "EnaSupport": true,
            "Hypervisor": "xen",
            "Name": "perfscale-fedora",
            "RootDeviceName": "/dev/sda1",
            "RootDeviceType": "ebs",
            "Tags": [
                {
                    "Key": "DO-NOT-DELETE",
                    "Value": "true"
                },
                {
                    "Key": "Name",
                    "Value": "perfscale-fedora"
                }
            ],
            "VirtualizationType": "hvm"
        }
    ]
}
```
