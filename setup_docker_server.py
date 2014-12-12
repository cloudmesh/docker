# THIS IS ONLY TESTED ON UBUNTU
#
# The following configuration is done on EC2 instance manually to setup docker server:
#
# Configuring Security groups (Security group here is open to the world which is not secure - tcp,icmp)
# Downloading certificate .pem file to ssh into the machine
# sudo apt-get update
# sudo apt-get -y install docker.io
# Modify /etc/init/docker.io.conf to add DOCKER_OPTS='-H tcp://<ip>:4243 -H unix:///var/run/docker.sock' where <ip> is eth0 ip (This is still unsecure but for our test it allows to use REST API)
# sudo service docker.io restart
# sudo docker.io pull ubuntu (Downloading ubuntu images)
