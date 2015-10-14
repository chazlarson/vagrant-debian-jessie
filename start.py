#! /usr/bin/python

import os, sys, shutil
from shutil import copytree

abbrev = sys.argv[1]

# Basic parameters
distro = 'debian-jessie'
owner = 'jhsu802701'
hash_port_host = {'general':'8080', 'rails':'3000', 'pg':'15432'}

# If necessary, change the host port numbers
if abbrev == 'base':
  hash_port_host = {'general':'8079', 'rails':'2999', 'pg':'15431'}
elif abbrev == 'ruby_mn':
  hash_port_host = {'general':'8081', 'rails':'3001', 'pg':'15433'}

def message_end(box_str_local):
  print "Enter the %s directory" % (box_str_local)
  print 'And then run the desired script to get started.'

# From 
# http://stackoverflow.com/questions/17140886/how-to-search-and-replace-text-in-a-file-using-python
def replace_string_in_file(file_local, string1, string2):
  fname1 = file_local
  fname2 = "%s.temp" %file_local
  f1 = open(fname1, 'r')
  f2 = open(fname2, 'w')
  for line in f1:
    f2.write(line.replace(string1, string2))
  f1.close()
  f2.close()
  os.remove(fname1)
  os.rename(fname2, fname1)

if not os.path.exists(abbrev):
  # Copy files
  dest_shared = "%s/shared" %abbrev
  copytree('template_files', abbrev)
  copytree('template_shared_files', dest_shared)
  
  # Parameters to fill in
  config_vm_box = "%s/%s-%s" %(owner, distro, abbrev)
  local_box = "vagrant-%s-%s.box" %(distro, abbrev)
  if abbrev == 'base':
    config_vm_box = "%s/%s" %(owner, distro)
    local_box = "vagrant-%s.box" %(distro)
  port_g = hash_port_host['general']
  port_r = hash_port_host['rails']
  port_p = hash_port_host['pg']
  
  # Update files outside the shared directory
  replace_string_in_file("%s/Vagrantfile" %abbrev, '<BOX_NAME>', config_vm_box)
  replace_string_in_file("%s/Vagrantfile" %abbrev, '<PORT_GEN_HOST>', port_g)
  replace_string_in_file("%s/Vagrantfile" %abbrev, '<PORT_RAILS_HOST>', port_r)
  replace_string_in_file("%s/Vagrantfile" %abbrev, '<PORT_PG_HOST>', port_p)
  replace_string_in_file("%s/download_new_box.sh" %abbrev, '<BOX_NAME>', config_vm_box)
  replace_string_in_file("%s/install_local_box.sh" %abbrev, '<LOCAL_BOX>', local_box)
  
  # Update files inside the shared directory
  replace_string_in_file("%s/shared/test_pg.sh" %abbrev, '<PORT_RAILS_HOST>', port_r)
  replace_string_in_file("%s/shared/test_pg.sh" %abbrev, '<PORT_PG_HOST>', port_p)
  replace_string_in_file("%s/shared/test_sq.sh" %abbrev, '<PORT_RAILS_HOST>', port_r)
  
  # Remove irrelevant files; rename the info-*.sh file to info.sh
  if abbrev == 'base':
    os.remove("%s/shared/test_pg.sh" %abbrev)
    os.remove("%s/shared/test_sq.sh" %abbrev)
    os.remove("%s/shared/info-rbenv.sh" %abbrev)
    os.rename("%s/shared/info-base.sh" %abbrev, "%s/shared/info.sh" %abbrev)
  else:
    os.remove("%s/shared/info-base.sh" %abbrev)
    os.rename("%s/shared/info-rbenv.sh" %abbrev, "%s/shared/info.sh" %abbrev)
  
  # Update the shared/info.sh file  
  replace_string_in_file("%s/shared/info.sh" %abbrev, '<PORT_RAILS_HOST>', port_r)
  replace_string_in_file("%s/shared/info.sh" %abbrev, '<PORT_PG_HOST>', port_p)

  message_end(abbrev)
else:
  print "The %s directory already exists." % (abbrev)
  message_end(abbrev)
  print
  print 'If the expected scripts and files are not in the %s directory,'
  print 'then delete that directory and run this script again.'

