## Tachyon Service for Ambari

This is a work in progress, your milege may vary

Install, start/stop service functional

```
git clone https://github.com/seraphin/tachyon-service.git /var/lib/ambari-server/resources/stacks/HDP/2.2/services/tachyon-service

ambari-server restart

```

Add service via ambari ui 

Select a master server node and worker nodes 

set tachyon.master.address = to tachyon master servername

set tachyon.underfs.address = hdfs://namnode:8020

set tachyon.worker.memory = a resonable amount of ram per server. Master also runs a worker

Needs code for service status check
