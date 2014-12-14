from cmd3.shell import command
from cloudmesh_common.logger import LOGGER
from cloudmesh.config.cm_config import cm_config
from cloudmesh_docker.api.docker import Docker
from cloudmesh.cm_mongo import cm_mongo
import cloudmesh

log = LOGGER(__file__)


class cm_shell_docker:
    """Creating a virtual docker"""

    def activate_cm_shell_docker(self):
        self.register_command_topic('cloud', 'docker')
        pass

    @command
    def do_docker(self, args, arguments):
        """
        Usage:
            docker service start CLOUD
            docker service cloud list
            docker service cloud delete
            docker container create NAME IMAGE
            docker container start NAME
            docker container stop NAME
            docker container list
            docker container delete NAME
            docker container attach NAME
            docker container pause NAME
            docker container unpause NAME
            docker images list

        Manages a virtual docker on a cloud

        Arguments:

          NAME     The name of the docker
          CLOUD    The name of the cloud on which the virtual docker
                   is to be deployed
          IMAGE    Docker server images

        Options:

           -v       verbose mode

        """
        log.info(arguments)

        if arguments["service"] and arguments["start"] and arguments["CLOUD"]:
            Docker().docker_service_start("{CLOUD}".format(**arguments))
            return

        if arguments["service"] and arguments["cloud"] and arguments["list"]:
            Docker().docker_service_cloud_list()
            return

        if arguments["service"] and arguments["cloud"] and arguments["delete"]:
            Docker().docker_service_cloud_delete()
            return

        if arguments["container"] and arguments["create"] and arguments["NAME"] and arguments["IMAGE"]:
            Docker().docker_container_create("{IMAGE}".format(**arguments),"{NAME}".format(**arguments))
            return

        if arguments["container"] and arguments["start"] and arguments["NAME"]:
            status = "start"
            Docker().docker_container_status_change(status,"{NAME}".format(**arguments))
            return

        if arguments["container"] and arguments["stop"] and arguments["NAME"]:
            status = "stop"
            Docker().docker_container_status_change(status,"{NAME}".format(**arguments))
            return

        if arguments["container"] and arguments["list"]:
            Docker().docker_container_list()
            return

        if arguments["container"] and arguments["delete"] and arguments["NAME"]:
            Docker().docker_container_delete("{NAME}".format(**arguments))
            return

        if arguments["container"] and arguments["attach"] and arguments["NAME"]:
            Docker().docker_container_attach("{NAME}".format(**arguments))
            return

        if arguments["container"] and arguments["pause"] and arguments["NAME"]:
            status = "pause"
            Docker().docker_container_status_change(status,"{NAME}".format(**arguments))
            return

        if arguments["container"] and arguments["unpause"] and arguments["NAME"]:
            status = "unpause"
            Docker().docker_container_status_change(status,"{NAME}".format(**arguments))
            return

        if arguments["container"] and arguments["restart"] and arguments["NAME"]:
            status = "restart"
            Docker().docker_container_status_change("{NAME}".format(**arguments))
            return

        if arguments["images"] and arguments["list"]:
            Docker().docker_images_list()
            return

        return
