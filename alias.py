import os
import globals
import json
from utils import read_file, write_file, colorprint
from typing import Dict

# This is being declared globally in order to prevent the data file being read from disk every single time it is required
aliasdict: Dict = {"please_dont_use_this_as_an_alias_it_is_required_by_zconfer": ""}

def init_aliasdict():
    global aliasdict 
    if aliasdict.get('please_dont_use_this_as_an_alias_it_is_required_by_zconfer', 'already_init') != 'already_init':
        aliasdict = json.loads(read_file(globals.jsondata.aliases))

def dump_aliasdict():
    global aliasdict
    write_file(globals.jsondata.aliases, json.dumps(aliasdict))


def check_alias_exists(alias):
    global aliasdict
    init_aliasdict()

    if alias not in aliasdict:
        print(colorprint("Alias {} was not found.".format(alias), "red"))
        return False

    return True


def generate():
    global aliasdict
    init_aliasdict()

    aliases_string = ""
    for alias in aliasdict:
        if aliasdict[alias]['enabled']:
            aliases_string = aliases_string + "alias {}='{}'\n".format(alias, aliasdict[alias]['value'])

    write_file(globals.modules.aliases, aliases_string)

def set(alias, value):
    global aliasdict
    init_aliasdict()

    aliasdict.setdefault(alias, {'value': "", 'enabled': True})
    aliasdict[alias]['value'] = value

    dump_aliasdict()
    generate()

    print(colorprint(f"Successfully aliased {alias} to '{value'}!", "green"))

def get(alias):
    global aliasdict
    init_aliasdict()

    if not check_alias_exists(alias):
        return
    
    print(aliasdict[alias]['value'])

def remove(alias):
    global aliasdict
    init_aliasdict()

    if not check_alias_exists(alias):
        return

    del aliasdict[alias]

    dump_aliasdict()
    generate()

    print(colorprint(f"Removed alias {alias}", "green"))

def enable(alias):
    global aliasdict
    init_aliasdict()

    if not check_alias_exists(alias):
        return

    aliasdict[alias]['enabled'] = True

    dump_aliasdict()
    generate()

    print(colorprint(f"Alias {alias} is now enabled."))

def disable(alias):
    global aliasdict
    init_aliasdict()

    if not check_alias_exists(alias):
        return

    aliasdict[alias]['enabled'] = False
    dump_aliasdict()
    generate()

    print(colorprint(f"Alias {alias} is now disabled."))

def view():
    global aliasdict
    init_aliasdict()

    if len(aliasdict) == 0:
        print(colorprint("No ZConf-created aliases available.", "red"))
        return

    print(colorprint("\n{:20}{:50}{:15}".format("Alias", "Value", "Enabled"), "bold"))
    for alias in aliasdict:
        print("{:20}{:50}{:15}".format(alias, aliasdict.get(alias)['value'], ("YES" if aliasdict[alias]['enabled'] else "NO")))
    print()
