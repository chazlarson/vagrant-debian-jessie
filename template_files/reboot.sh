#!/bin/bash

echo '---------------'
echo 'vagrant halt -f'
vagrant halt -f

echo '----------'
echo 'vagrant up'
vagrant up

echo '-----------'
echo 'vagrant ssh'
vagrant ssh
