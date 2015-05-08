#!/usr/bin/env python
from resource_management import *

# config object that holds the configurations declared in the -config.xml file
config = Script.get_config()

# tachyon stach directory
tachyon_archive = config['configurations']['tachyon-env']['tachyon.archive']

# tachyon stach directory
tachyon_stack_dir = config['configurations']['tachyon-env']['tachyon.stack.dir']

# tachyon underfs address
tachyon_master = config['configurations']['tachyon-env']['tachyon.master.address']

# tachyon underfs address
underfs_addr = config['configurations']['tachyon-env']['tachyon.underfs.address']

# tachyon worker memory alotment 
worker_mem = config['configurations']['tachyon-env']['tachyon.worker.memory']

# HDP install dir
base_dir = config['configurations']['tachyon-env']['hdp.install.path'] 

# tachyon log dir
log_dir = config['configurations']['tachyon-env']['tachyon.log.dir']


