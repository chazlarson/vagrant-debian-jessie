# FAQ

### What's wrong with installing Ruby on Rails directly on the host OS?

*  Manually installing or reinstalling Ruby on Rails directly on the host machine is a slow and bureaucratic process.  I have done it in Linux and in OS X, and it takes a few hours, even if you know exactly what you're doing.  
*  Installing Ruby on Rails in Windows requires jumping through even more hoops.  Very few Ruby on Rails developers use Windows (which is not based on Unix like OS X and Linux are), and this means there is much less help available for Windows users than is the case for OS X users and Linux users.
*  Because manually installing Ruby on Rails takes so long, it's not viable at events like Startup Weekend or 24-hour web site challenges.  In the time it would take you to install Ruby on Rails manually on a teammate's computer, competitors who use Drupal, PHP, Django, or other technologies can leave you choking on their dust.
*  There's something wrong when JUST GETTING STARTED requires lots of time and effort.

### Why would you need to reinstall Ruby on Rails?

*  If you believe your Ruby on Rails installation is broken, and you are unable to troubleshoot your problem, you have no choice but to reinstall Ruby on Rails.
*  There have been times when I had difficulty transferring a Ruby gem or Rails app that I was developing onto another machine.  I've learned to provide a test_gem.sh script in my Ruby gems and a test_app.sh script in my Rails apps to cover every step needed to set up and test the project.  The ability to reinstalling Ruby on Rails quickly is necessary for confirming that these scripts are complete.
*  It aids the troubleshooting process.  If you are having difficulty with your Rails app even in a fresh Ruby on Rails installation, then you know that your problem is app-specific and not due to problems related to the overall development environment.

### What's wrong with installing Ruby on Rails in VirtualBox but not using Vagrant?

I used Ruby on Rails in VirtualBox before I learned how to use Vagrant.  While this offered some of the benefits of using Vagrant (such as being cross-platform and offering on-demand access to a fresh version of Ruby on Rails), there were drawbacks:

*  I still had to manually install Ruby on Rails.
*  Being in the guest machine cut me off from the host machine, and being in the host machine cut me off from the guest machine.  This meant that I couldn't copy and paste text from the host machine into the virtual machine or vice versa.  While there are ways to enable this, it does take extra time and effort.
*  The virtual machine needed its own set of GUI tools, such as an editor, KeePassX, web browser, etc.  Installing these tools took extra time and effort.
*  I didn't like the experience of using Linux in VirtualBox on a Mac.  Linux has always been designed with PC users rather than Mac users in mind.  I found it disorienting to have a Linux GUI but a Mac keyboard.  Because Vagrant doesn't require ANY GUI tools on the virtual machine and allows me to stick with the convenience of the software on the host OS, I don't face this cognitive dissonance when I use Vagrant on a Mac.

### Why is the Vagrant way so much better?

*  My Vagrant solution allows me to set up Ruby on Rails on a computer in minutes instead of hours, because Ruby on Rails comes pre-installed on this portable virtual machine.  The process is nearly as quick and easy as getting started in Drupal, PHP, or Django.  Less time spent thrashing around means more time available to work on the project.
*  Vagrant works for Linux, OS X, and Windows machines.  Because Ruby on Rails is used in the uniform virtual environment, Vagrant eliminates the potential conflicts of having team members on different platforms.  Furthermore, running Ruby on Rails through Vagrant makes it much easier for Windows users to get started.
*  I can reinstall Ruby on Rails in just a few minutes simply by destroying and rebuilding the Vagrant box.  If I think that my Ruby on Rails installation is broken, or if I need to make sure that my test_gem.sh script in a Ruby gem or my test_app.sh script in a Rails app is complete, it only takes me a few minutes to restore my Ruby on Rails installation to its original base box state.
*  I still retain the convenience of using the software in my host OS, because files in the shared folder are accessible through both the host machine and virtual machine.  This means I can run my projects on the virtual machine but use my normal tools on the host machine to edit them.

### What's wrong with Vagrant boxes based on Ubuntu?

*  Ubuntu boxes require large, time-consuming, and frequent updates.  Every time you build or rebuild a Ubuntu-based Vagrant box, you must endure a long wait before you can use it again.  Given that I regard rebuilding a Vagrant box to be a routine task, this is not acceptable.
*  Most Ubuntu boxes are out-of-date, which is why so many updates are needed.  However, disabling the updates means using outdated software, which is a violation of best practices.  
*  To add insult to injury, many Ubuntu base boxes don't even come with Ruby on Rails pre-installed, and you must wait for a script to take care of this.

### Why is your Debian Stable Vagrant box so much better?

*  Debian Stable is much easier to maintain and keep up-to-date than Ubuntu.  Debian Stable requires only a few occasional and modest updates even over the course of weeks or months.  (I provide a new release every few weeks to ensure that the latest box is reasonably up-to-date.)  Complying with best practices is NOT an undue burden.
*  Some Vagrant setups install software through provisioning scripts that run during the "vagrant up" stage.  In contrast, software is pre-installed in my base box, which saves you time during the "vagrant up" stage, especially the first time you use my base box after downloading or rebuilding it.  Software pre-installed in my Debian Stable Vagrant base box includes:

  1.  rbenv, Ruby, and Rails
  2.  node.js
  3.  Ansible
  4.  Puppet
  5.  Chef
  6.  Redis server
  7.  SQLite3
  8.  PostgreSQL
  9.  Graphviz
  
*  This Vagrant repository on GitHub includes Bash scripts that consolidate routine multi-step tasks into one step.

### Why did you use rbenv instead of RVM?

*  rbenv can be installed more easily and in less time than RVM.
*  rbenv is faster than RVM.
*  The rbenv-communal-gems feature saves time and disk space by allowing multiple versions of Ruby to share the same gems.  When you install a gem in under one version of Ruby, it's available to certain other versions of Ruby as well.

### What process do you use to create your Vagrant base boxes?

I use a tool called Packer to create my Vagrant base boxes.  The source code I use for creating my Debian base boxes is available at https://github.com/jhsu802701/packer-debian-jessie .
