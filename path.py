import os
import globals
import json
from utils import read_file, write_file, colorprint
from typing import Dict

pathdict: Dict = json.loads(read_file(globals.jsondata.path))

def check_segment_exists(seg):
    if seg.upper() not in pathdict:
        print(colorprint("Segment {} was not found in PATH".format(seg), "red"))
        return False

    return True

def dump_pathdict():
    write_file(globals.jsondata.path, json.dumps(pathdict))

def generate():
    pathstring = "export PATH=$PATH:"
    for seg in pathdict:
        if pathdict[seg]['loaded']:
            pathstring = pathstring + pathdict[seg]['value'] + ":"

    write_file(globals.modules.path, pathstring[:-1])

def set_segment(seg, value):
    seg = seg.upper()
    pathdict.setdefault(seg, {'value': "", 'loaded': True})
    pathdict[seg]['value'] = value

    dump_pathdict()
    generate()

def get_segment(seg):
    seg = seg.upper()

    if not check_segment_exists(seg):
        return
    
    print(pathdict[seg]['value'])

def remove_segment(seg):
    seg = seg.upper()

    if not check_segment_exists(seg):
        return

    del pathdict[seg]

    dump_pathdict()
    generate()

def load_segment(seg):
    seg = seg.upper()

    if not check_segment_exists(seg):
        return

    pathdict[seg]['loaded'] = True
    dump_pathdict()
    generate()

def unload_segment(seg):
    seg = seg.upper()

    if not check_segment_exists(seg):
        return

    pathdict[seg]['loaded'] = False
    dump_pathdict()
    generate()

def view():
    if len(pathdict) == 0:
        print(colorprint("No ZConf-created segments in PATH", "red"))
        return

    print(colorprint("Segment\t\t\tValue\t\tLoaded", "bold"))
    for seg in pathdict:
        print("{}\t\t{}\t\t{}".format(seg, pathdict.get(seg)['value'], ("YES" if pathdict[seg]['loaded'] else "NO")))