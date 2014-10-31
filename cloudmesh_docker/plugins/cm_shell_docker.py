from cmd3.shell import command
from cloudmesh_common.logger import LOGGER
from cloudmesh.config.cm_config import cm_config

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
            docker create NAME WORKERS CLOUD [--image=IMAGE] [--flavor=FLAVOR]
            docker info [NAME]
            docker status [NAME]            
            docker delete [-f] [NAME]
            docker clean
            docker checkpoint NAME
            docker restore NAME
            docker list

        Manages a virttual docker on a cloud

        Arguments:

          NAME     The name of the docker
          WORKERS  The number of workers in the virtual docker
          CLOUD    The name of the cloud on which the virtual docker
                   is to be deployed

        Options:

           -v       verbose mode

        """
        log.info(arguments)

        username = cm_config().username()

        print username
                
        if arguments["clean"]:
            log.info("clean the vm")
            return

        if arguments["delete"] and arguments["NAME"]:
            log.info("delete the docker '{NAME}'".format(**arguments))
            return
        elif arguments["delete"]:
            log.info("delete all the docker vms")
            return

        if arguments["info"] and arguments["NAME"]:
            log.info("info of docker {NAME}".format(**arguments))
            return
        elif arguments["info"]:
            log.info("info of all docker vms")
            return

        if arguments["list"] and arguments["NAME"]:
            log.info("list of docker {NAME}".format(**arguments))
            
            return
        elif arguments["list"]:
            log.info("list of all docker vms")
            return

        return
