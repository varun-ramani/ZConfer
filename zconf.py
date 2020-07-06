import sys

from help import help_overview, help_command

if len(sys.argv) == 1:
    help_overview()

if len(sys.argv) == 2:
    if sys.argv[1] == "help":
        help_overview()
    else:
        print("{} is an invalid command.".format(sys.argv[1]))

if len(sys.argv) == 3:
    if sys.argv[1] == "help":
        help_command(sys.argv[2])