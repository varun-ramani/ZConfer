from utils import colorprint

def overview():
    overview_string = """
ZConf by Varun Ramani
usage: zconf <command> [<args>]

Commands Available:
\thelp\t\tPrints this overview or a command's manpage
\tinit\t\tPost-installation step; initializes ZConf for first use
\tpath\t\tProvides path management functionality
\talias\t\tProvides alias management functionality
\tplugin\t\tProvides plugin management functionality
\ttheme\t\tProvides theme management functionality
    """
    print(overview_string)

def command(cmd):
    print(colorprint("Command-specific manpages have been disabled for the time being. Please consult the wiki available on GitHub.", "red"))
    return

    # TODO: Refactor this abomination using dictionaries instead of long strings.
    manpages = {
        "help": """
usage: zconf help OR zconf help <command>

When invoked without the optional command, help will print the default help overview. When a command is supplied, the manual for 
that particular command will be returned.
        """,
        "init": """
usage: zconf init

Initializes ZConfer by backing up the current .zshrc, generating all necessary components, and installing a new zsh configuration file.
        """,
        "path": """
usage: zconf path <subcommand> [<args>]

Provides comprehensive path management functionality in ZConfer.

{header}
\t\tview\t\t\t\tDisplays all the ZConfer-managed path segments and their statuses
\t\tset\t<segment> <value>\tSets a segment to a specified value
\t\tget\t<segment>\t\tGets a segment's value
\t\trm\t<segment>\t\tRemoves a specified PATH segment
\t\tload\t<segment>\t\tLoads the specified segment into the PATH
\t\tunload\t<segment>\t\tUnloads the specified segment from the PATH
        """,
        "alias": """
usage: zconf alias <subcommand> [<args>]

Provides comprehensive path management functionality in ZConfer.

{header}
\t\tview\t\t\t\tDisplays all the ZConfer-managed aliases and their statuses
\t\tset\t<alias> <value>\tSets an alias to a specified value
\t\tget\t<alias>\t\tGets the specified alias's value
\t\trm\t<alias>\t\tRemoves a specified alias
\t\tenable\t<alias>\t\tEnables the specified alias
\t\tdisable\t<segment>\t\tDisables the specified alias
        """,
        "plugin": """
usage: zconf plugin <subcommand> [<args>]

Provides plugin management functionality in ZConfer.

{header}
\t\tview\t{{all, local, remote}} \tLists plugins
\t\tall\t\tLists all plugins in the repository, whether they are installed or not.
\t\t  view local\t\tLists installed plugins
\t\t  view remote\t\tLists plugins that are not installed.
\t\tset\t<alias> <value>\tSets an alias to a specified value
\t\tget\t<alias>\t\tGets the specified alias's value
\t\trm\t<alias>\t\tRemoves a specified alias
\t\tenable\t<alias>\t\tEnables the specified alias
\t\tdisable\t<segment>\t\tDisables the specified alias
        """
    }

    for key in manpages:
        manpages[key] = manpages[key].format(header=colorprint("Subcommands:\tName\tArguments\t\tDescription", "bold"))

    print(manpages.get(cmd, "'{}' is an invalid command.".format(cmd)))