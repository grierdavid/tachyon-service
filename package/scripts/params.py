#!/usr/bin/env python
from resource_management import *

# config object that holds the configurations declared in the -config.xml file
config = Script.get_config()

# tachyon underfs address
underfs_addr = config['configurations']['tachyon-env']['tachyon.underfs.address']

# tachyon worker memory alotment 
worker_mem = config['configurations']['tachyon-env']['tachyon.worker.memory']

# tachyon base dir
base_dir = config['configurations']['tachyon-env']['tachyon.base.dir'] 

# tachyon log dir
log_dir = config['configurations']['tachyon-env']['tachyon.log.dir']

# tachyon environment file
tachyon_env = config['configurations']['tachyon-env']['tachyon.environment']
