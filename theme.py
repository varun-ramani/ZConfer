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

    write_file(globals.modules.themes, f"source {globals.themes_dir}/{selected_theme_name}/{selected_theme_entry}")

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
    list_text.append(colorprint("{:20}{:50}{:12}".format("Theme", "Description", "Installed"), "bold"))


    for key in repo_dict:
        theme = repo_dict[key]

        installed_text = "YES" if key in installed_dict['installed'] else "NO"

        description_arr = textwrap.wrap(theme['description'], 45)

        list_text.append("{:20}{:50}{:12}".format(key, description_arr[0], installed_text))

        for i in range(1, len(description_arr)):
            list_text.append("{:20}{:50}{:12}".format("", description_arr[i], ""))

        list_text.append("\n")

    print("\n".join(list_text))

def view_local():
    global repo_dict
    global installed_dict
    init_dict()

    list_text = []

    print()
    list_text.append(f"Selected theme: {installed_dict['enabled']}")
    list_text.append("\n")
    list_text.append(colorprint("{:20}{:50}".format("Theme", "Description"), "bold"))


    for key in installed_dict['installed']:
        if key in repo_dict:
            theme = repo_dict[key]
        else:
            continue

        description_arr = textwrap.wrap(theme['description'], 45)

        list_text.append("{:20}{:50}".format(key, description_arr[0]))

        for i in range(1, len(description_arr)):
            list_text.append("{:20}{:50}".format("", description_arr[i]))

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
        theme = repo_dict[key]

        if key in installed_dict['installed']:
            continue

        description_arr = textwrap.wrap(theme['description'], 45)

        list_text.append("{:20}{:50}".format(key, description_arr[0]))

        for i in range(1, len(description_arr)):
            list_text.append("{:20}{:50}".format("", description_arr[i]))

        list_text.append("\n")

    if len(list_text) == 1:
        print(colorprint("You have already installed all available themes.\n", "red"))
        return 

    print("\n".join(list_text))

def add(theme):
    global repo_dict
    global installed_dict

    init_dict()

    if theme in installed_dict['installed']:
        print(colorprint(f"Theme '{theme}' has already been added.", "red"))
        return False

    if theme not in repo_dict:
        print(colorprint(f"Theme '{theme}' is not available for installation.", "red"))
        return False

    if os.system(f"zsh {globals.repo_dir}/themes/{theme}/add.zsh") != 0:
        print(colorprint(f"Failed to add theme '{theme}'.", "red"))
        return False

    print(colorprint(f"Successfully added theme '{theme}'!", "green"))

    installed_dict['installed'][theme] = {
        "entry": repo_dict[theme]['entry']
    }

    dump_dict()
    generate()

    return True

def set(theme):
    global repo_dict 
    global installed_dict

    init_dict()

    if theme not in installed_dict['installed']:
        print(colorprint(f"Theme '{theme}' not present, attempting to add it.", "yellow"))
        if not add(theme):
            return False

    if installed_dict['enabled'] == theme:
        print(colorprint(f"'{theme}' is already the selected theme!", "red"))
        return

    installed_dict['enabled'] = theme

    dump_dict()
    generate()

    print(colorprint(f"Successfully enabled theme '{theme}' - restart ZSH to check it out!", "green"))

def remove(theme):
    global repo_dict 
    global installed_dict

    init_dict()

    if theme not in installed_dict['installed']:
        print(colorprint(f"Theme '{theme}' is not installed!", "red"))
        return

    if os.system(f"zsh {globals.repo_dir}/themes/{theme}/remove.zsh") != 0:
        print(colorprint(f"Removal of theme '{theme}' was unsuccessful.", "red"))

    del installed_dict['installed'][theme]
    installed_dict['enabled'] = "notatheme"

    dump_dict()
    generate()

    print(colorprint(f"Successfully removed theme '{theme}'", "green"))

def enable(theme):
    global installed_dict 
    init_dict()

    if theme not in installed_dict:
        print(colorprint(f"Theme {theme} is not installed!"))

    installed_dict[theme]['enabled'] = True

    dump_dict()
    generate()

def disable(theme):
    global installed_dict
    init_dict()

    if theme not in installed_dict:
        print(colorprint(f"Theme {theme} is not installed!"))

    installed_dict[theme]['enabled'] = False

    dump_dict()
    generate()
