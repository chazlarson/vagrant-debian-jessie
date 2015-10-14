#!/bin/bash

# This script downloads the latest version of the original base box.

# Check for regular user login
if [ ! $( id -u ) -ne 0 ]; then
  echo 'You must be a regular user to run this script.'
  exit 2
fi

BOX_NAME='<BOX_NAME>'

git pull

echo '---------------'
echo 'vagrant halt -f'
vagrant halt -f

echo '------------------'
echo 'vagrant destroy -f'
vagrant destroy -f

echo '------------------------------------'
echo "vagrant box remove $BOX_NAME --force"
vagrant box remove $BOX_NAME --force

sh login.sh
