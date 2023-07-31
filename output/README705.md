# Containerized DNS server using dnsmasq

## Build Image from Containerfile
```
podman build -t container-dnsmasq .
```

## Run container
```
podman run -it -p 53:53/tcp -p 53:53/udp -v $( pwd )/hosts_dir/:/hosts_dir/:z container-dnsmasq
```

## Concept
Host files are contained in hosts_dir and all records are read by dnsmasq by using --hostsdir option as seen in Containerfile.
```
--hostsdir=<path>
Read all the hosts files contained  in  the  directory.  New  or changed  files  are  read automatically. 
```

## Usage
```
$ dig  +short my-cool-host.example.com @<server-name/IP>
10.x.x.x
```

## DNS Manager API
```
Refer to dns manager API at github.com/Microservices-perfscale/tiny-ddns-manager
```
