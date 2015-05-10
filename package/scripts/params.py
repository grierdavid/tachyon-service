#!/usr/bin/config python
from resource_management import *

# config object that holds the configurations declared in the -config.xml file
config = Script.get_config()


# ambari-agent package
tachyon_package_dir = config['configurations']['tachyon-config']['tachyon.package.dir']

# identify archive file
tachyon_archive_file = config['configurations']['tachyon-config']['tachyon.archive.file']

# tachyon master address
tachyon_master = config['configurations']['tachyon-config']['tachyon.master.address']

# tachyon underfs address
underfs_addr = config['configurations']['tachyon-config']['tachyon.underfs.address']

# tachyon worker memory alotment 
worker_mem = config['configurations']['tachyon-config']['tachyon.worker.memory']

# HDP install dir
base_dir = config['configurations']['tachyon-config']['hdp.install.path'] 

# tachyon log dir
log_dir = config['configurations']['tachyon-config']['tachyon.log.dir']
