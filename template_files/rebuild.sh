#!/bin/bash

echo '----------------'
echo 'vagrant halt  -f'
vagrant halt -f

echo '------------------'
echo 'vagrant destroy -f'
vagrant destroy -f

sh login.sh
