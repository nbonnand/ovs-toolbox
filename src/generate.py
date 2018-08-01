#!/usr/bin/python3

# git $Id$ 

from datetime import datetime
import subprocess
import re
import sys


#--------------------------

def loadfile(filename,whandler):
  print("reading: "+filename)
  with open(filename) as fh:
      line='enter loop'
      while line:
        line = fh.readline()
        if(not pattern_header.search(filename)):
          if(pattern.search(line)):
            continue
          if(pattern_import_01.search(line)):
            continue
          if(pattern_import_02.search(line)):
            continue

        whandler.write(line)
      if(pattern_header.search(filename)):
        whandler.write("\nbuildtime='{}'\nproject_release='{}'\n".format(buildtime,project_release))

#--------------------------
#--------- MAIN -----------
#--------------------------
print(len(sys.argv))
        
if(len(sys.argv)<2):
  print ('Error: please specify version number !!!')
  exit(0)

project_release=str(sys.argv[1])
print ("project_release="+project_release)
                
buildtime=datetime.now().isoformat(timespec='seconds')
pattern=re.compile(r'import\sproject_ressource')
pattern_import_01=re.compile(r'from\sPyQt5\simport')
pattern_import_02=re.compile(r'from\smyclickablelabel')
pattern_header=re.compile(r'header\.py')

print("generating ressource file: tmp/project_ressource.py")
subprocess.check_output(['pyrcc5','project_ressource.qrc','-o','tmp/project_ressource.py'])

for uifile in (
    'about',
    'dockerif_dialog',
    'dockernet_dialog',
    'if_dialog',
    'iso_dialog',
    'iterate_dialog',
    'kvm_virt_disk_dialog',
    'kvm_virt_net_dialog',
    'mgmt_dialog',
    'misc_dialog',
    'of_delete_dialog',
    'of_dialog',
    'of_group',
    'of_trace',
    'output',
    'pg_dialog',
    'port_dock',
    'pt_dialog',
    'qos_qos_dialog',
    'qos_queue_dialog',
    'qos_queue_link',
    'stats_dialog',
    'splash_dialog',
):
    print("generating: tmp/{}.py".format(uifile))
    subprocess.check_output(['pyuic5',"UI/{}.ui".format(uifile),'-o',"tmp/{}.py".format(uifile)])

print("generating tmp/ovs-toolbox-guionly.py")
subprocess.check_output(["pyuic5","UI/ovs-toolbox.ui","-o","tmp/ovs-toolbox-guionly.py"])

#start_pdb()
with open('../ovs-toolbox.py','w') as filename_whandler:
    for sourcefile in ('header.py',
                       'tmp/ovs-toolbox-guionly.py',
                       'tmp/if_dialog.py',
                       'tmp/pt_dialog.py',
                       'tmp/kvm_virt_net_dialog.py',
                       'tmp/kvm_virt_disk_dialog.py',
                       'tmp/misc_dialog.py',
                       'tmp/iso_dialog.py',
                       'tmp/pg_dialog.py',
                       'tmp/qos_queue_dialog.py',
                       'tmp/qos_qos_dialog.py',
                       'tmp/qos_queue_link.py',
                       'tmp/port_dock.py',
                       'tmp/of_dialog.py',
                       'tmp/of_delete_dialog.py',
                       'tmp/output.py',
                       'tmp/of_trace.py',
                       'tmp/of_group.py',
                       'tmp/mgmt_dialog.py',
                       'tmp/dockernet_dialog.py',
                       'tmp/dockerif_dialog.py',
                       'tmp/iterate_dialog.py',
                       'tmp/stats_dialog.py',
                       'tmp/about.py',
                       'tmp/splash_dialog.py',
                       'tmp/project_ressource.py',
                       'footer.py'):
        loadfile(sourcefile,filename_whandler)
    filename_whandler.close()
    print("\ngenerating: ovs-toolbox.py")

subprocess.check_output(['chmod','700','../ovs-toolbox.py'])

with open("../ovs-toolbox.py.sha512sum","w") as out:
     subprocess.run(['sha512sum','../ovs-toolbox.py'],stdout=out)
