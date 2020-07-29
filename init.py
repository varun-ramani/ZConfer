from utils import colorprint, confirm, write_file
import os
import shutil
import globals
import json
import path
import alias
import plugin
import theme

boiler_zshrc = """
# Load zconf 
source {}

# ZConf won't write to this file, so feel free to append any additional configuration you may need.

""".format(globals.zconf_main)

boiler_zconf_main = """

# ==> DON'T EDIT THIS FILE BY HAND <==
source {0}/path.zsh
source {0}/alias.zsh
source {0}/plugin.zsh
source {0}/theme.zsh

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

    print("Creating core config file at {}".format(globals.zconf_main))
    write_file(globals.zconf_main, boiler_zconf_main)

    print("JSON data files:")
    print("\tCreating {}".format(globals.jsondata.path))
    write_file(
        globals.jsondata.path, 
        json.dumps({
            "BIN": {
                "value": "{}/bin".format(globals.home),
                "loaded": True
            }
        }, indent=4)
    )
    print("\tCreating {}".format(globals.jsondata.aliases))
    write_file(
        globals.jsondata.aliases, 
        json.dumps({
            "gclone": {
                "value": "git clone",
                "enabled": True
            },
            "gpush": {
                "value": "git push",
                "enabled": True
            },
            "gpull": {
                "value": "git pull",
                "enabled": True
            },
            "gadd": {
                "value": "git add .",
                "enabled": True
            }
        }, indent=4)
    )
    print("\tCreating {}".format(globals.jsondata.plugins))
    write_file(
        globals.jsondata.plugins,
        json.dumps({})
    )
    print(f"\tCreating {globals.jsondata.themes}")
    write_file(
        globals.jsondata.themes,
        json.dumps({
            "installed": {
                "notatheme": {
                    "entry": "notatheme.zsh-theme"
                }
            },
            "enabled": "notatheme"
        })
    )

    print("Module files:")
    print("\tGenerating {} from {}".format(globals.modules.path, globals.jsondata.path))
    path.generate()
    print("\tGenerating {} from {}".format(globals.modules.aliases, globals.jsondata.aliases))
    alias.generate()
    print("\tGenerating {} from {}".format(globals.modules.plugins, globals.jsondata.plugins))
    plugin.generate()
    print("\tGenerating {} from {}".format(globals.modules.themes, globals.jsondata.themes))
    theme.generate()

    if os.path.exists(globals.plugins_dir):
        print("Erasing plugins directory")
        shutil.rmtree(globals.plugins_dir)

    os.mkdir(globals.plugins_dir)

    if os.path.exists(globals.themes_dir):
        print("Erasing themes directory")
        shutil.rmtree(globals.themes_dir)

    os.mkdir(globals.themes_dir)

    print("Installing default theme")
    os.mkdir(globals.themes_dir + "/notatheme")

    with open(globals.themes_dir + "/notatheme/notatheme.zsh-theme", "w+") as file:
        file.write("# This is not a theme at all!")

    print(colorprint("ZConfer has been fully installed. Restart ZSH to get started!", "green"))
