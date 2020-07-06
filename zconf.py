import sys

from init import initialize
from utils import colorprint
import help
import os
import globals

def cli_main():
    if not os.path.exists(globals.zconf_home):
        print(colorprint("ZConf directory not found. This could be the result of a botched installation/uninstallation - \nplease follow the installation instructions at https://github.com/varun-ramani/zconf to reinstall ZConf.", "red"))
        return

    if len(sys.argv) == 1:
        help.overview()

    if len(sys.argv) == 2:
        if sys.argv[1] == "help":
            help.overview()
        elif sys.argv[1] == "init":
            initialize()
        else:
            print("'{}' is an invalid command.".format(sys.argv[1]))

    if len(sys.argv) == 3:
        if sys.argv[1] == "help":
            help.command(sys.argv[2])

cli_main()