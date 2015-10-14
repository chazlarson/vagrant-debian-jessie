#!/bin/bash

echo

TIME_STAMP="$(cat /home/vagrant/timestamp.txt)"
echo "Timestamp: ${TIME_STAMP}"

echo
echo 'Ruby versions'
rbenv versions

echo
rails -v
gem list "^rails$"

echo
echo "Version of node.js:"
nodejs -v

echo
echo "Heroku Toolbelt:"
heroku version

echo
python --version

echo
ansible --version

echo
VERSION_PUPPET="$(puppet master --version)"
echo "Version of Puppet: ${VERSION_PUPPET}"

echo
chef-solo -v

echo
redis-server -v

echo
echo "Version of SQLite:"
sqlite3 -version

echo
psql --version

echo
