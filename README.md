# Favorite Movies App

## Introduction ##
This Favorite Movies App is a web application that allows users to login in with their Google accounts and add their favorite movies to the database. Registered users will have the ability to post, edit and delete their own movies.

## Functionality ##
- Allows users to log into the system via their Google accounts.
- Authenticated users can add movie categories and movies in a particular category.
- Authenticated users can update/delete movie categories and movies that they created.
- All the data is stored in a local database file.

## Environment Requirement ##
- [VirtualBox(5.1+)](https://www.virtualbox.org/wiki/Downloads)
- [Vagrant(2.1.1+)](https://www.vagrantup.com/downloads.html)
- Python(3.6+)
- Git Bash
- [Vagrantfile](https://github.com/udacity/fullstack-nanodegree-vm)

## Python Modules ##
- sqlalchemy (1.2.9)
- flask(1.0.2)
- oauth2client(4.1.2)
- requests(2.19.1)
- pip(10.0.1)


## How to Use ##
1.Use the command below to download the VM files which will be in the directory `fullstack/vagrant/`.
   ```bash
   git clone https://github.com/udacity/fullstack-nanodegree-vm  fullstack
   ```
2.Download all files in this project into the directory `fullstack/vagrant/catalog`.

3.Change current directory to `fullstack/vagrant/`. Then use
   ```bash
   vagrant up
   ```
  Vagrant will download the Ubuntu operating system and install it. After it's finished, the VM will start.
4.After the VM started, type command below to connect to the VM.
   ```bash
   vagrant ssh
   ```
5.Type command below to change to the shared directory.
   ```bash
   cd /vagrant
   ```
6.Change the current directory to the `fullstack/vagrant/catalog`

7.Install and update **pip** module.
   ```bash
    curl https://bootstrap.pypa.io/get-pip.py | sudo python3.6
   ```
8.Install **sqlalchemy** module.
   ```bash
    sudo pip3 install sqlalchemy
   ```
9.Install **flask** module.   
   ```bash
    sudo pip3 install flask
   ```
10.Install **oauth2client** module.    
   ```bash
    sudo pip3 install oauth2client
   ```    
11.Run the command below to set up database.
   ```bash
    python database_setup.py
   ```     
12.Run the command below to populate the database.
   ```bash
    python database_populator.py
   ```
13.Run the command below to host a web server on our own computer.
   ```bash
    python app.py
   ```
14.Open terminal, and type url:`http://localhost:5000/` to use this app.


## Helpful Resources ##
* [Google OAuth Credentials](https://console.cloud.google.com/apis/credentials/oauthclient)
* [Bootstrap Chinese Documentation](http://www.bootcss.com/)
* [jquery Documentation](https://jquery.com/)
* [Flask Documentation](http://flask.pocoo.org/)

## Reference ##
* [BootCDN](https://v3.bootcss.com/getting-started/)
* [ Udacity course Full-Stack Foundations Code repository](https://github.com/udacity/ud330)

## Potential future updates
- Improve the styles of the web interface;
- Implement other third party logins and possibly a local registration and authentication system.

## Notice
- This application has a JSON endpoint: `localhost:5000/show/categories/JSON`.
- Some of the code are from previous projects.
- The version of Flask 1.x is necessary.
- The version of Python 3.6.x is necessary.
- The first time you run this project you must follow all 14 steps, but the next time you only need to run step 3/4/5/6/13/14.
- Use `vagrant halt` command when you need to close the VM .
