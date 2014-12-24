-----------------
Cloudmesh Docker
-----------------

Objective:
----------

This project's objective is to develop docker client interface for
cloudmesh. Docker is an open source project that providies a layer of
abstraction and automation of operating system-level virtualization on
Linux. It automates the deployment of applications inside software
containers.


Project requirements:
---------------------

* Deploying docker server (Amazon EC2 instances used here)

* Developing commandline interface for docker client to integrate
   with existing cloudmesh shell.

Design:
-------

* Cloudmesh server is configured on Linux Ubuntu box.

* When we start the cloudmesh shell, the docker client is loaded and
   the data is stored in mongodb with three collections defined -
   Cloudmeshdocker, Images and Containers. The data is persistent
   throughout the connection.

* REST API calls are made for docker usage.

Usage:
------

* docker container create, docker container delete, etc.

Limitations/Issues:
-------------------

* Currently docker attach(docker run) doesn't work (Need to figure out
  how to use stdin,stdout for this). Other workaround can be to use
  remote ssh.

* Currently supports only one cloud

* Docker server needs to be configured on secure port. Currently, it
   is public for anyone to access it.

How to deploy/run:
------------------

* The cloud/docker server is specified in etc/cloudmesh_docker.yaml which is were it should be modified.
  Following scenarios are implemented/not implemented:
  (1) Docker server on local machine : Not implemented
  (2) Docker server on remote machine: Not implemented
  (3) Docker server on AWS: Implemented
  (4) Multiple docker machines: Not implemented

* Installing docker server on AWS/Cloudmesh:
  (1) Configure security groups on EC2 instance through AWS GUI (Tested: Security group open to the world which is not secure - tcp,icmp - Not recommended). For cloudmesh, create security group using following:
  nova secgroup-add-rule default tcp 4243 4243 0.0.0.0/0
  (2) Download certificate .pem file to ssh into the machine for AWS.
  (3) Run the following commands on the machine:
      (a) sudo apt-get update
      (b) sudo apt-get -y install docker.io
      (c) Modify /etc/init/docker.io.conf to add DOCKER_OPTS='-H tcp://<ip>:4243 -H unix:///var/run/docker.sock' where <ip> is eth0 ip (Tested but not recommended as <ip> is open to the world)
      (d) sudo service docker.io restart
      (e) sudo docker.io pull ubuntu (This downloads ubuntu images for docker containers)

* Start cloudmesh shell and run docker commands

Github repository:
------------------

https://github.com/cloudmesh/docker
