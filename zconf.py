import sys
import os

from utils import colorprint
import help
import globals
import init
import path
import alias
import argparse
import plugin
import theme

os.environ['ZCONFER_PLUGINS_DIR'] = globals.plugins_dir
os.environ['ZCONFER_THEMES_DIR'] = globals.themes_dir

def err_invalid_command(command):
    print(colorprint("Command '{}' is either invalid or is being used incorrectly.".format(command), "red"))

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
            init.initialize()
        else:
            err_invalid_command(sys.argv[1])

    if len(sys.argv) == 3:
        if sys.argv[1] == "help":
            help.command(sys.argv[2])

        elif sys.argv[1] == "path":
            if sys.argv[2] == "view":
                path.view()
            else:
                err_invalid_command("path " + sys.argv[2])

        elif sys.argv[1] == "alias":
            if sys.argv[2] == "view":
                alias.view()
            else:
                err_invalid_command("alias " + sys.argv[2])
        elif sys.argv[1] == "plugin":
            if sys.argv[2] == "update":
                plugin.update()
            else:
                err_invalid_command("plugin " + sys.argv[2])
        else:
            err_invalid_command(sys.argv[1])

    if len(sys.argv) == 4:
        if sys.argv[1] == "path":
            if sys.argv[2] == "rm":
                path.remove_segment(sys.argv[3])
            elif sys.argv[2] == "load":
                path.load_segment(sys.argv[3])
            elif sys.argv[2] == "unload":
                path.unload_segment(sys.argv[3])
            elif sys.argv[2] == "get":
                path.get_segment(sys.argv[3])
            else:
                err_invalid_command("path " + sys.argv[2])

        elif sys.argv[1] == "alias":
            if sys.argv[2] == "rm":
                alias.remove(sys.argv[3])
            elif sys.argv[2] == "enable":
                alias.enable(sys.argv[3])
            elif sys.argv[2] == "disable":
                alias.disable(sys.argv[3])
            elif sys.argv[2] == "get":
                alias.get(sys.argv[3])
            else:
                err_invalid_command("alias " + sys.argv[2])

        elif sys.argv[1] == "plugin":
            if sys.argv[2] == "view":
                if sys.argv[3] == "all":
                    plugin.view_all()
                elif sys.argv[3] == "local":
                    plugin.view_local()
                elif sys.argv[3] == "remote":
                    plugin.view_remote()
                else:
                    err_invalid_command("plugin view " + sys.argv[3])
            elif sys.argv[2] == "add":
                plugin.add(sys.argv[3])
            elif sys.argv[2] == "rm":
                plugin.remove(sys.argv[3])
            elif sys.argv[2] == "enable":
                plugin.enable(sys.argv[3])
            elif sys.argv[2] == "disable":
                plugin.disable(sys.argv[3])
            else:
                err_invalid_command("plugin " + sys.argv[2])

        elif sys.argv[1] == "theme":
            if sys.argv[2] == "view":
                if sys.argv[3] == "all":
                    theme.view_all()
                elif sys.argv[3] == "local":
                    theme.view_local()
                elif sys.argv[3] == "remote":
                    theme.view_remote()
                else:
                    err_invalid_command("theme view " + sys.argv[3])
            elif sys.argv[2] == "set":
                plugin.set(sys.argv[3])
            elif sys.argv[2] == "rm":
                plugin.remove(sys.argv[3])
            else:
                err_invalid_command("theme " + sys.argv[2])

        else:
            err_invalid_command(sys.argv[1])
    
    if len(sys.argv) == 5:
        if sys.argv[1] == "path":
            if sys.argv[2] == "set":
                path.set_segment(sys.argv[3], sys.argv[4])
        elif sys.argv[1] == "alias":
            if sys.argv[2] == "set":
                alias.set(sys.argv[3], sys.argv[4])
        else:
            err_invalid_command(sys.argv[1])

cli_main()
