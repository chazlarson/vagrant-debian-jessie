#!/bin/bash

# This script creates a basic Rails app that uses an SQLite database.
# PURPOSE: Provide confirmation that Ruby on Rails is properly set up.

# Just making sure Ruby, Rails, and Node are working as expected.
sh /home/vagrant/shared/info.sh

# This is the same test app as the one at http://elinux.org/RPi_Ruby_on_Rails .
cd /home/vagrant/shared && rails new school_sq --skip-spring
cd /home/vagrant/shared/school_sq && rails g scaffold Pupil name:string form:string
cd /home/vagrant/shared/school_sq && rake db:migrate
echo '**********************'
echo 'OPEN YOUR WEB BROWSER.'
echo 'GO TO THE FOLLOWING URL:'
echo 'http://localhost:<PORT_RAILS_HOST>/pupils'
echo '*************************************************************************'
echo "You can use access the database in this app's db/development.sqlite3 file"
echo 'by using SQLite database browser.'
echo '*********************************'
cd /home/vagrant/shared/school_sq && rails s -b 0.0.0.0
