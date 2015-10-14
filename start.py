#! /usr/bin/python

import os, shutil

print '*******************'
print 'Vagrant Box Options'
print '1. Base'
print '2. rbenv (general purpose)'
print '3. rbenv (rails.mn)'
print
box_option = input("Enter the name of the Vagrant box you wish to use:\n")
box_option = str(box_option)
box_str = 'rbenv'
if box_option == '1':
  box_str = 'base'
elif box_option == '3':
  box_str = 'ruby_mn'

def message_end(box_str_local):
  print "The %s directory already exists." % (box_str_local)
  print "Enter the %s directory" % (box_str_local)
  print 'And then run the desired script to get started.'

if not os.path.exists(box_str):
  os.makedirs(box_str)
  os.makedirs("%s/shared" % (box_str))
  message_end(box_str)
else:
  message_end(box_str)
  print
  print 'If the expected scripts and files are not in the %s directory,'
  print 'then delete that directory and run this script again.'
