##########################################################################################################
# DOCKER TEST PROCEDURE
# ---------------------
# Docker lifecycle test
# Covers:
# (1) docker service start CLOUD : Adds CLOUD to the docker service
# (2) docker service cloud list : Lists Docker serice CLOUD (Currently supports only one cloud)
# (3) docker images list : Lists images on the Docker server
# (4) docker container create NAME IMAGE : Creates a container on Docker with NAME and IMAGE
# (5) docker container start NAME : Starts container with NAME
# (6) docker container pause NAME : Pauses container with NAME
# (7) docker container unpause NAME : Unpauses container with NAME
# (8) docker container stop NAME : Stops container with NAME
# (9) docker container delete NAME : Delete/Remove container with NAME
# (10) docker container list : Lists all containers
# (11) docker service cloud delete : Deletes CLOUD from the docker service
#
# docker container attach NAME : This exists but currently there are some issues for login to the container
# DOCKER CLOUD SERVER created for test: Ubuntu Amazon EC2 instances - (a) 54.148.243.157 (b) 54.149.122.57
#
###########################################################################################################

import cloudmesh
from pprint import pprint

mesh = cloudmesh.mesh("mongo")

# Start docker service with CLOUD
print("Starting Docker service.....................")
print cloudmesh.shell("docker service start 54.148.243.157")

# List clouds
print("Listing clouds.........................")
print cloudmesh.shell("docker service cloud list")

# List images
print("Listing available images......................")
print cloudmesh.shell("docker images list")

# Create container
print("Creating container with name docker_cont_1 and image ubuntu:latest..........")
print cloudmesh.shell("docker container create docker_cont_1 ubuntu:latest")
print cloudmesh.shell("docker container create docker_cont_2 ubuntu:latest")
print cloudmesh.shell("docker container create docker_cont_3 ubuntu:latest")

# Start container
print("Starting container with name docker_cont_1................")
print cloudmesh.shell("docker container start docker_cont_1")

# List containers
print("Listing containers....................")
print cloudmesh.shell("docker container list")

# Pause container
print("Pausing container docker_cont_2...........")
print cloudmesh.shell("docker container pause docker_cont_2")
print cloudmesh.shell("docker container list")

# Unpause container
print("Unpausing container docker_cont_2...........")
print cloudmesh.shell("docker container unpause docker_cont_2")
print cloudmesh.shell("docker container list")

# Stop container
print("Stopping container docker_cont_1..............")
print cloudmesh.shell("docker container stop docker_cont_1")
print cloudmesh.shell("docker container list")

# Delete container
print("Delete containers.................")
print cloudmesh.shell("docker container delete docker_cont_1")
print cloudmesh.shell("docker container delete docker_cont_2")
print cloudmesh.shell("docker container delete docker_cont_3")
print cloudmesh.shell("docker container list")

# Remove cloud
print("Deleting cloud.................")
print cloudmesh.shell("docker service cloud delete") 

