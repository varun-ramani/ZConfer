#!/usr/bin/python3

import sys

from help import overview as help_overview

if len(sys.argv) == 1:
    print(help_overview)