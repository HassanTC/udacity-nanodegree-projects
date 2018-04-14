
# Udacity - Linux Server Configuration

## Introduction

> This project is linked to the Configuring Linux Web Servers course, which teaches you to secure and set up a Linux server. By the end of this project, you will have one of your web applications running live on a secure web server.

> To complete this project, you'll need a Linux server instance. We recommend using Amazon Lightsail for this. If you don't already have an Amazon Web Services account, you'll need to set one up. Once you've done that, here are the steps to complete this project.

## Usage
1. Public IP Address : `http://35.159.16.104/`
2. SSH PORT : `2200`
3. Application URL: [http://35.159.16.104/](http://35.159.16.104/)

## Tasks

1.  Start a new Ubuntu Linux server instance on [Amazon Lightsail](https://lightsail.aws.amazon.com). There are full details on setting up your
	  1. create amazon account
	  2. wait 24 hours for activation
	  3. go to [Amazon Lightsail](https://lightsail.aws.amazon.com) and create new instance
2. ssh to your machine
	  1. create key using `ssh-keygen`
		2. put your public key inside `~/.ssh/authorized_keys` into your server
	  2. connect your server from your local machine
3. Update all currently installed packages
    1. `sudo apt-get update`
    2. `sudo apt-get upgrade`
4. Change the SSH port from 22 to 2200.
    1. change port from `22` to `2200`
    2. change `PermitRootLogin` to `no`
    3. change `PasswordAuthentication` to `no`
    4. `sudo service ssh restart`
    5. add custom port to networking tap at lightsail
5. Configure the Uncomplicated Firewall (UFW) to only allow incoming connections for SSH (port 2200), HTTP (port 80), and NTP (port 123).
    1. `sudo ufw default deny incoming`
    2. `sudo ufw default allow outgoing`
    3. `sudo ufw allow 2200/tcp`
    4. `sudo ufw allow 80/tcp`
    5. `sudo ufw allow 123/udp`
    6. `sudo ufw enable`
6. Create a new user account named grader.
    1. `sudo adduser grader`
    2. `sudo apt-get install finger`
    3. check userr exist `finger grader`
7. Give `grader` the permission to `sudo`
    1. `usermod -aG sudo grader`
		2. `AllowUsers username ubuntu` into `/etc/ssh/sshd_config`
		3. `sudo visudo` and add `grader ALL=(ALL:ALL) ALL`
		4. `sudo service ssh restart`
8. Create an SSH key pair for grader using the ssh-keygen tool.
		1. `ssh-keygen`
		2. add public key to `authorized_keys`
9. Configure the local timezone to UTC.
		1. `sudo dpkg-reconfigure tzdata`
		2. choose `none of the above`
		3. choose `UTC`
10. Install and configure Apache to serve a Python mod_wsgi application.
		1. `sudo apt-get install apache2`
		2. `sudo apt-get install python-setuptools libapache2-mod-wsgi`
		3. `sudo service apache2 restart`
11. Install and configure PostgreSQL
		1. `sudo apt-get install postgresql`
		2. check `sudo vim /etc/postgresql/9.3/main/pg_hba.conf` leave it as it as its already does not allow remote connections
		3. `sudo su - postgres`
		4. `psql`
		5. `CREATE DATABASE catalog;`
		6. `CREATE USER catalog;`
		7. `ALTER ROLE catalog WITH PASSWORD 'password';`
		8. `GRANT ALL PRIVILEGES ON DATABASE catalog TO catalog;`
		9. `exit`
12. install git [git installation](https://www.digitalocean.com/community/tutorials/how-to-install-git-on-ubuntu-14-04)
		1. `sudo apt-get update`
		2. `sudo apt-get install git`
		3. `sudo apt-get install build-essential libssl-dev libcurl4-gnutls-dev libexpat1-dev gettext unzip`
		4. `git config --global user.name "Hassan"`
		5. `git config --global user.email "hassan.mahmoud1@outlook.com"`
13. Clone and setup your Item Catalog project from the Github repository you created earlier in this Nanodegree program.
		> clone the repo and configure it at port `http://35.159.16.104/`
