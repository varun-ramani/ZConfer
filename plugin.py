import globals
from utils import download_progress_bar, break_to_size, read_file, colorprint, write_file
import time
import pydoc
from typing import Dict
import json
import textwrap
import os

# This is being declared globally in order to prevent the data file being read from disk every single time it is required
plugins_dict : Dict = {"this_is_the_default_dictionary": ""}
installed_dict: Dict = {"this_is_the_default_dictionary": ""}

def generate():
    global plugins_dict
    global installed_dict
    init_dict()

    write_file(globals.modules.plugins, "\n".join([f"source {installed_dict[plugin]['entry']}" for plugin in installed_dict]))

def dump_dict():
    write_file(globals.jsondata.plugins, json.dumps(installed_dict))

def init_dict():
    global plugins_dict
    global installed_dict
    if plugins_dict.get('this_is_the_default_dictionary', 'already_init') != 'already_init':
        plugins_dict = json.loads(read_file(globals.jsondata.repo))['plugins']

    if installed_dict.get('this_is_the_default_dictionary', 'already_init') != 'already_init':
        installed_dict = json.loads(read_file(globals.jsondata.plugins))

def update_repo():
    import urllib.request as req
    print("Downloading latest repository...", end="")
    req.urlretrieve('https://raw.githubusercontent.com/varun-ramani/zconfer/master/repo.json', globals.jsondata.repo)
    print("done")

def update():
    update_repo()

def list_all():
    global plugins_dict
    global installed_dict
    init_dict()

    list_text = []

    list_text.append(colorprint("{:20}{:50}{:12}{:12}".format("Plugin", "Description", "Installed", "Loaded"), "bold"))


    for key in plugins_dict:
        plugin = plugins_dict[key]

        installed_text = "YES" if key in installed_dict else "NO"
        loaded_text = "YES" if installed_text == "YES" and installed_dict[key]['loaded'] == True else "NO"

        description_arr = textwrap.wrap(plugin['description'], 45)

        list_text.append("{:20}{:50}{:12}{:12}".format(key, description_arr[0], installed_text, loaded_text))

        for i in range(1, len(description_arr)):
            list_text.append("{:20}{:50}{:12}{:12}".format("", description_arr[i], "", ""))

    print("\n".join(list_text))

def add(plugin):
    global plugins_dict 
    global installed_dict

    init_dict()

    if plugin in installed_dict:
        print(colorprint(f"Plugin '{plugin}' is already installed!", "red"))
        return

    if plugin not in plugins_dict:
        print(colorprint(f"Plugin '{plugin}' was not found!", "red"))
        return

    if plugins_dict[plugin]['type'] == "repository":
        os.system(f"git clone {plugins_dict[plugin]['source']} {globals.plugins_dir}/{plugin}")

        installed_dict[plugin] = {
            "loaded": True,
            "entry": f"{globals.plugins_dir}/{plugin}/{plugins_dict[plugin]['entry']}"
        }

        dump_dict()
        generate()

        print(colorprint(f"Successfully installed plugin '{plugin}'", "green"))


def remove(plugin):
    global plugins_dict 
    global installed_dict

    init_dict()

    if plugin not in installed_dict:
        print(colorprint(f"Plugin '{plugin}' is not installed!", "red"))
        return

    os.system(f"rm -rf {globals.plugins_dir}/{plugin}")

    del installed_dict[plugin]

    dump_dict()
    generate()

    print(colorprint(f"Successfully removed plugin '{plugin}'", "green"))