import globals
from utils import download_progress_bar, break_to_size, read_file, colorprint, write_file
import time
from typing import Dict
import json
import textwrap
import os

# This is being declared globally in order to prevent the data file being read from disk every single time it is required
repo_dict : Dict = {"this_is_the_default_dictionary": ""}
installed_dict: Dict = {"this_is_the_default_dictionary": ""}

def dump_dict():
    write_file(globals.jsondata.themes, json.dumps(installed_dict, sort_keys=True))

def init_dict():
    global repo_dict
    global installed_dict
    if repo_dict.get('this_is_the_default_dictionary', 'already_init') != 'already_init':
        repo_dict = json.loads(read_file(globals.jsondata.repo))['themes']
        repo_dict = {key: repo_dict[key] for key in sorted(repo_dict)}

    if installed_dict.get('this_is_the_default_dictionary', 'already_init') != 'already_init':
        installed_dict = json.loads(read_file(globals.jsondata.themes))
        installed_dict = {key: installed_dict[key] for key in sorted(installed_dict)}

def generate():
    global installed_dict
    init_dict()

    selected_theme_name = installed_dict['enabled']
    selected_theme_entry = installed_dict['installed'][selected_theme_name]['entry']

    write_file(globals.modules.plugins, f"source {globals.themes_dir}/{selected_theme_name}/{selected_theme_entry}")

def update_repo():
    import urllib.request as req
    os.system(f'cd {globals.repo_dir} && git pull')
    print(colorprint("Updated local repository!", "green"))

def update():
    update_repo()

def view_all():
    global repo_dict
    global installed_dict
    init_dict()

    list_text = []

    print()
    list_text.append(f"Selected theme: {installed_dict['enabled']}")
    list_text.append("\n")
    list_text.append(colorprint("{:20}{:50}{:12}{:12}".format("Theme", "Description", "Installed"), "bold"))


    for key in repo_dict:
        theme = repo_dict[key]

        installed_text = "YES" if key in installed_dict else "NO"

        description_arr = textwrap.wrap(theme['description'], 45)

        list_text.append("{:20}{:50}{:12}".format(key, description_arr[0], installed_text))

        for i in range(1, len(description_arr)):
            list_text.append("{:20}{:50}{:12}".format("", description_arr[i], "", ""))

        list_text.append("\n")

    print("\n".join(list_text))

def view_local():
    global installed_dict
    global repo_dict

    init_dict()

    list_text = []

    print()
    if len(installed_dict) != 0:
        list_text.append(colorprint("{:20}{:50}{:12}".format("Theme", "Description", "Enabled"), "bold"))
    else:
        print(colorprint("You have no installed themes!\n", "red"))
        return


    for key in installed_dict:
        plugin = installed_dict[key]

        enabled_text = "YES" if plugin['enabled'] == True else "NO"

        description_arr = textwrap.wrap(repo_dict[key]['description'], 45)

        list_text.append("{:20}{:50}{:12}".format(key, description_arr[0], enabled_text))

        for i in range(1, len(description_arr)):
            list_text.append("{:20}{:50}{:12}".format("", description_arr[i], ""))

        list_text.append("\n")

    print("\n".join(list_text))

def view_remote():
    global installed_dict
    global repo_dict

    init_dict()

    list_text = []

    print()
    list_text.append(colorprint("{:20}{:50}".format("Theme", "Description"), "bold"))

    for key in repo_dict:
        plugin = repo_dict[key]

        if key in installed_dict:
            continue

        description_arr = textwrap.wrap(plugin['description'], 45)

        list_text.append("{:20}{:50}".format(key, description_arr[0]))

        for i in range(1, len(description_arr)):
            list_text.append("{:20}{:50}".format("", description_arr[i]))

        list_text.append("\n")

    if len(list_text) == 1:
        print(colorprint("You have already installed all available plugins.\n", "red"))
        return 

    print("\n".join(list_text))

def add(theme):
    global repo_dict
    global installed_dict

    init_dict()

    if theme in installed_dict:
        print(colorprint(f"Theme '{theme}' has already been added.", "red"))
        return

    if theme not in repo_dict:
        print(colorprint(f"Theme '{theme}' was not found.", "red"))
        return

    if os.system(f"zsh {globals.repo_dir}/themes/{theme}/add.zsh") != 0:
        print(colorprint(f"Failed to add theme '{theme}'.", "red"))
        return

    print(colorprint(f"Successfully added theme '{theme}'!", "green"))

    installed_dict[theme] = {
        "entry": repo_dict['themes'][theme]['entry']
    }

    dump_dict()
    generate()

def set(theme):
    global repo_dict 
    global installed_dict

    init_dict()

    if theme not in installed_dicts:
        print(colorprint(f"Theme '{theme}' not present, attempting to add it.", "yellow"))
        add(theme)

    if plugin not in repo_dict:
        print(colorprint(f"Plugin '{plugin}' was not found!", "red"))
        return

    dump_dict()
    generate()

    print(colorprint(f"Successfully installed plugin '{plugin}'", "green"))

def remove(plugin):
    global repo_dict 
    global installed_dict

    init_dict()

    if plugin not in installed_dict:
        print(colorprint(f"Plugin '{plugin}' is not installed!", "red"))
        return

    if os.system(f"zsh {globals.repo_dir}/plugins/{plugin}/remove.zsh") != 0:
        print(colorprint(f"Removal of plugin '{plugin}' was unsuccessful.", "red"))

    del installed_dict[plugin]

    dump_dict()
    generate()

    print(colorprint(f"Successfully removed plugin '{plugin}'", "green"))

def enable(plugin):
    global installed_dict 
    init_dict()

    if plugin not in installed_dict:
        print(colorprint(f"Plugin {plugin} is not installed!"))

    installed_dict[plugin]['enabled'] = True

    dump_dict()
    generate()

def disable(plugin):
    global installed_dict
    init_dict()

    if plugin not in installed_dict:
        print(colorprint(f"Plugin {plugin} is not installed!"))

    installed_dict[plugin]['enabled'] = False

    dump_dict()
    generate()
