#import status properties defined in -env.xml file from status_params class
import params
import sys, os, pwd, signal, time
from resource_management import *
from resource_management.core.base import Fail
from resource_management.core.exceptions import ComponentIsNotRunning
from subprocess import call
import cPickle as pickle

class Master(Script):

  #Call setup.sh to install the service
  def install(self, env):
  
    # Install packages listed in metainfo.xml
    self.install_packages(env)

    #extract archive and symlink dirs
    cmd = '/bin/tar' + ' -zxf ' + params.tachyon_package_dir + 'files/' +  params.tachyon_archive_file + ' -C  /'
    Execute('echo "Running ' + cmd + '"')
    Execute(cmd)

    cmd = '/bin/ln' + ' -s ' + params.base_dir + '/tachyon' + ' /usr/hdp/current/'
    Execute('echo "Running ' + cmd + '"')
    # it doesn't matter if the link already exists
    try:
      Execute(cmd)
    except:
      pass

    self.configure(env)

  def configure(self, env):
    env.set_params(params)

    tachyon_config_dir = params.base_dir + '/conf/'
    tachyon_libexec_dir = params.base_dir + '/libexec/'

    File(format("{tachyon_config_dir}/tachyon-env.sh"),
          owner='root',
          group='root',
          content=Template('tachyon-env.sh.j2', conf_dir=tachyon_config_dir)
    )

    File(format("{tachyon_libexec_dir}/tachyon-config.sh"),
          owner='root',
          group='root',
          content=Template('tachyon-config.sh.j2', conf_dir=tachyon_libexec_dir)
    )


  #Call start.sh to start the service
  def start(self, env):
    #import status properties defined in -env.xml file from status_params class
    #import status_params
    
    #call format
    cmd = params.base_dir + '/bin/tachyon ' + 'format'
      
    Execute('echo "Running cmd: ' + cmd + '"')    
    Execute(cmd)
    
    #execute the startup script
    cmd = params.base_dir + '/bin/tachyon-start.sh ' + 'master'
      
    Execute('echo "Running cmd: ' + cmd + '"')    
    Execute(cmd)
    
    #mount ramfs local to master service
    cmd = params.base_dir + '/bin/tachyon-start.sh ' + 'worker' + ' Mount'
      
    Execute('echo "Running cmd: ' + cmd + '"')    
    Execute(cmd)


  #Called to stop the service using the pidfile
  def stop(self, env):
    #import status properties defined in -env.xml file from status_params class
    #import status_params
    
    #execure the startup script
    cmd = params.base_dir + '/bin/tachyon-stop.sh'
      
    Execute('echo "Running cmd: ' + cmd + '"')    
    Execute(cmd)
      	
  #Called to get status of the service using the pidfile
  def status(self, env):
  
    #call status
    cmd = params.base_dir + '/bin/tachyon status master'

    try:
      Execute(cmd)
    except Fail:
      raise ComponentIsNotRunning()

if __name__ == "__main__":
  Master().execute()
