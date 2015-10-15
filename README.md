# Vagrant Boxes - Debian Jessie

This repository makes it easy to get started with Vagrant and Ruby on Rails and allows you to run multiple Vagrant boxes simultaneously.  All Vagrant boxes used here are based on Debian Jessie, which is Debian's current stable branch.  Debian Stable is lighter, faster, and lower maintenance than Ubuntu.  When you boot up any of the Vagrant boxes featured here, you have an up-to-date system.  The boxes designed for Ruby on Rails come with it pre-installed.

## WARNING 1
Unless otherwise instructed, do NOT execute commands or perform actions as sudo/root/admin UNLESS you are installing software (such as Git, Python, VirtualBox, Vagrant, SQLite database browser, pgAdmin, etc.).  Using sudo/root/admin inappropriately can lead to "permission denied" messages later.

## WARNING 2
When you start the Rails 4.2 server from an app in your Vagrant box, enter the command "rails s -b 0.0.0.0".  The "-b 0.0.0.0" is ESSENTIAL for viewing your app from the web browser on your host machine.  If you simply enter "rails s" or "rails server", you will NOT be able to view your app from the web browser on your host machine.

## WARNING 3
PAY ATTENTION to the port numbers when you use your web browser or pgAdmin to view the Rails apps running on your Vagrant boxes.  No two apps may share the same port number.  As a result, the port number to use in your web browser will NOT always be 3000, and the port number to use in pgAdmin will NOT always be 5432 or 15432.

## Getting started

### Step 1 - Install Git, Python, VirtualBox, and Vagrant.

* Git: If your host OS is Debian Linux, Ubuntu Linux, or one of their derivatives, the shell command is "sudo apt-get install -y git".  If your host OS is OS X or Windows, go to the [Git](http://git-scm.com) web site, click on Downloads, choose the appropriate Operating System specific package to download, and follow the normal procedure for installing software.

* Python: If your host OS is Debian Linux, Ubuntu Linux, or one of their derivatives, the shell command is "sudo apt-get install -y python".  If your host OS is OS X or Windows, and you don't have Python already installed, go to the [Python](https://www.python.org/) web site, click on Downloads, choose the appropriate Operating System specific package to download, and follow the normal procedure for installing software.

* VirtualBox: If your host OS is based on Debian Jessie or a newer branch of Debian, the shell command is "sudo apt-get install -y virtualbox".  If your host OS is OS X or Windows, go to the [VirtualBox](https://www.virtualbox.org) web site, click on Downloads, and get the appropriate package for your host OS, and follow the normal procedure for installing software.  WARNING: If you're using certain older versions of VirtualBox (such as 4.1.18), the file syncing may not work.  If you're still using Debian Wheezy as your host OS, this will be an issue.

* Vagrant: If your host OS is based on Debian Jessie or a newer branch of Debian, the shell command is "sudo apt-get install -y vagrant".  If your host OS is OS X or Windows, go to the [Vagrant](http://vagrantup.com) web site, click on Downloads, and get the appropriate package for your host OS.  WARNING: The configuration file in this repository is NOT compatible with Vagrant 1.0.x.  If you're still using Debian Wheezy as your host OS, this will be an issue.

### Step 2 - Download this repository.

* In the terminal application, enter the following commands:

    git clone https://github.com/jhsu802701/vagrant-debian-jessie.git
    cd vagrant-debian-jessie

### Step 3 - Build the Vagrant setup.

* To use the minimal Vagrant box, enter the command "sh min.sh".

* To use the Vagrant box with pre-installed rbenv, enter the command "sh rbenv.sh".

* To use the Vagrant box with pre-installed rbenv for the [Ruby.MN web site](http://www.ruby.mn/), enter the command "sh rbenv-rubymn.sh".

* Each of the above commands builds a Vagrant setup from the files in the template_files and template_shared_files directories and fills in the appropriate parameters.  At the end of the process, you will see the on the screen the name of the directory created.

### Step 4 - Build and SSH into the Vagrant box.

* In the terminal application, use the "cd" command to enter the appropriate Vagrant setup directory created at the end of the previous step.  Then enter the command "sh login.sh" to acquire and then log into the Vagrant box.
   
* If you are asked to provide a password, enter "vagrant".  There should be a README-host.txt file in the /home/vagrant/shared directory, which is the same README-host.txt file in the shared directory in this repository.

### Step 5 - View information on the Vagrant box.
Use your SSH connection to cd your way into the /home/vagrant/shared directory in your virtual machine, and run the info.sh script with the command "sh info.sh".  This displays the time stamp of the Vagrant box and the versions of Ruby, Rails, rbenv, node.js, SQLite, PostgreSQL, and other software included in the box.

### Step 6 - Test the Ruby on Rails Installation (SQLite)

* NOTE: Ruby on Rails is NOT included in the minimal (min) version of the Vagrant box, and this step does not apply.

* Use your SSH connection to cd your way into the /home/vagrant/shared directory in your virtual machine, and run the test_sq.sh script with the command "sh test_sq.sh".  NOTE: This command will take a few minutes to complete.  At its conclusion, you will see a message ending in "Ctrl-C to shutdown server".

* When the test_sq.sh script has finished its work, open your browser on your host machine, and go to the appropriate URL, which may or may not be at port 3000.  The School App should appear.

### Step 7 - Test the Ruby on Rails Installation (PostgreSQL)

* NOTE: Ruby on Rails is NOT included in the minimal (min) version of the Vagrant box, and this step does not apply.

* Go to your SSH connection from the previous step, press Ctrl-C to turn off the server from the Rails app in Step 4, cd your way into the /home/vagrant/shared directory, and run the test_pg.sh script with the command "sh test_pg.sh".  NOTE: This command will take a few minutes to complete.  At its conclusion, you will see a message ending in "Ctrl-C to shutdown server".

* When the test_pg.sh script has finished its work, open your browser on your host machine, and go to the appropriate URL, which may or may not be at port 3000.  The School App should appear.

## Port Numbers

You may run multiple Vagrant boxes simultaneously ONLY if they are all using different ports.  This table shows you which port is in use for each of the available Vagrant boxes provided by this repository.

| Vagrant Box                           | General Port | Rails Port | PostgreSQL Port |
| ------------------------------------- | -------------|------------| ----------------|
| jhsu802701/debian-jessie              | 79           | 2999       | 15431           |
| jhsu802701/debian-jessie-rbenv        | 80           | 3000       | 15432           |
| jhsu802701/debian-jessie-rbenv-rubymn | 81           | 3001       | 15433           |

## Virtual Machine Management

To __exit__ SSH connection to Vagrant Virtual Machine, 

    exit        # option 1

    # press ^D  # option 2


To reboot and log back in,

    # from your host OS
    
    sh reboot.sh # Executes "vagrant halt", "vagrant up", and "vagrant ssh".
    

To __suspend__ virtual machine,  
    
    # from your host OS

    vagrant suspend


To __resume__ virtual machine,  
    
    # From your host OS

    vagrant resume


To __shutdown/halt__ virtual machine,  
    
    # From your host OS

    vagrant halt


To __resume__ virtual machine,  

   # From your host OS  

   vagrant up


To get __status__ of virtual machine,  

    # From your host OS

    vagrant status


To completely delete virtual machine,  

    # From your host OS

    vagrant destroy   # DANGER: all is gone
    
To delete, rebuild, and log back into the virtual machine,

    # From your host OS
    
    sh rebuild.sh # Executes "vagrant halt", "vagrant destroy", "vagrant up", and "vagrant ssh"

Please check the [Vagrant documentation](http://vagrantup.com/v1/docs/index.html) for more information on Vagrant.

## Credits 

*  Thanks to Derek Rockwell for paving the way with his Vagrant setup at https://github.com/railsmn/railsmn-dev-box .
*  Thanks to Kevin Bullock for recommending that I try rbenv.
