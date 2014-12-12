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

*  Cloudmesh server is configured on Linux Ubuntu box.

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

Github repository:
------------------

https://github.com/cloudmesh/docker
