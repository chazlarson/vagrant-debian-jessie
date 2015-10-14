#!/bin/bash
# Proper header for a Bash script.

# NOTE: This script is for use by the Packer setup at 
# https://github.com/jhsu802701/packer-debian-jessie .

# Check for regular user login
if [ ! $( id -u ) -ne 0 ]; then
  echo 'You must be a regular user to run this script.'
  exit 2
fi 

BOX_NAME='<BOX_NAME>'
LOCAL_BOX='<LOCAL_BOX>'

echo '---------------'
echo 'vagrant halt -f'
vagrant halt -f

echo '------------------'
echo 'vagrant destroy -f'
vagrant destroy -f

echo '------------------------------------'
echo "vagrant box remove $BOX_NAME --force"
vagrant box remove $BOX_NAME --force

echo '------------------------------------'
echo "vagrant box add $BOX_NAME $LOCAL_BOX"
vagrant box add $BOX_NAME $LOCAL_BOX;

sh login.sh
