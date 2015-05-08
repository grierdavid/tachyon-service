import sys, os, pwd, signal, time
from resource_management import *
from subprocess import call
import cPickle as pickle

class Master(Script):

  #Call setup.sh to install the service
  def install(self, env):
  
    # Install packages listed in metainfo.xml
    self.install_packages(env)
    self.configure(env)
    
    #import properties defined in -config.xml file from params class
    import params

        
    #extract archive and symlink dirs
    #cmd = params.tachyon_stack_dir + '/package/scripts/setup.sh ' + params.tachyon_dir + ' ' + params.tachyon_downloadlocation ' >> ' + params.stack_log
    cmd = '/usr/bin/wget' + ' -qO- ' + params.tachyon_archive_url + params.tachyon_archive_file + '?raw=true' + ' | ' + '/bin/tar' + ' -zx -C' ' /'
    Execute('echo "Running ' + cmd + '"')
    Execute(cmd)

    cmd = '/bin/ln' + ' -s ' + params.base_dir + '/tachyon' + ' /usr/hdp/current/'
    Execute('echo "Running ' + cmd + '"')
# add conditional if not exists    Execute(cmd)

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
          content=Template('tachyon-conf.sh.j2', conf_dir=tachyon_libexec_dir)
    )

  def configure(self, env):
    import params
    env.set_params(params)


  #Call start.sh to start the service
  def start(self, env):

    #import properties defined in -config.xml file from params class
    import params

    #import status properties defined in -env.xml file from status_params class
    #import status_params
    
    #call format
    cmd = params.base_dir + '/bin/tachyon ' + 'format'
      
    Execute('echo "Running cmd: ' + cmd + '"')    
    Execute(cmd)
    
    #mount ramfs
    cmd = params.base_dir + '/bin/tachyon-start.sh ' + 'worker' + ' Mount'
      
    Execute('echo "Running cmd: ' + cmd + '"')    
    Execute(cmd)

  #Called to stop the service using the pidfile
  def stop(self, env):
  
    #import status properties defined in -env.xml file from status_params class  
    import params

    #import status properties defined in -env.xml file from status_params class  
    #import status_params
    
    #execure the startup script
    cmd = params.base_dir + '/bin/tachyon-stop.sh'
      
    Execute('echo "Running cmd: ' + cmd + '"')    
    Execute(cmd)
      	
  #Called to get status of the service using the pidfile
  def status(self, env):
  
    #import status properties defined in -env.xml file from status_params class
    import status_params
    env.set_params(status_params)  
    
    #use built-in method to check status using pidfile
    check_process_status(status_params.stack_pidfile)  


if __name__ == "__main__":
  Master().execute()
