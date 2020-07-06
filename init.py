from utils import colorprint, confirm, write_file
import os
import globals

boiler_zshrc = """
# Load zconf 
source {}

# ZConf won't write to this file, so feel free to append any additional configuration you may need.

""".format(globals.zconf_main)

boiler_zconf_main = """

source {0}/path.zsh
source {0}/alias.zsh

""".format(globals.zconf_home)

def initialize():
    if os.path.exists(globals.zshrc_backup):
        print(colorprint("There exists a backup of .zshrc at {} - running init will overwrite it.".format(globals.zshrc_backup), "red"))
        if not confirm(colorprint("\nContinue? (y/n) ", "yellow")):
            return
    
    if os.path.exists(globals.zshrc):
        print("Backing up existing configuration at {} to {}".format(globals.zshrc, globals.zshrc_backup))
        os.rename(globals.zshrc, globals.zshrc_backup)

    print("Creating new configuration at {}".format(globals.zshrc))
    write_file(globals.zshrc, boiler_zshrc)

    if os.path.exists(globals.zconf_main):
        print(colorprint("ZConf has already been initialized on this system - running init will destroy your existing configuration.", "red"))
        if not confirm(colorprint("\nDestroy your existing configuration and start fresh? (y/n) ", "yellow")):
            return

    write_file(globals.zconf_main, boiler_zconf_main)

