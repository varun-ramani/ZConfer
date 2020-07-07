def overview():
    overview_string = """
ZConf by Varun Ramani
usage: zconf <command> [<args>]

Commands Available:
\thelp\t\tPrints this overview or a command's manpage
\tinit\t\tPost-installation step; initializes ZConf for first use
\tpath\t\tProvides path management functionality
\tplugin\t\tProvides plugin management functionality
\talias\t\tProvides alias management functionality
    """
    print(overview_string)

def command(cmd):
    manpages = {
        "help": """
usage: zconf help OR zconf help <command>

When invoked without the optional command, help will print the default help overview. When a command is supplied, the manual for 
that particular command will be returned.
        """,
        "init": """
usage: zconf init

Initializes ZConf by backing up the current .zshrc, generating all necessary components, and installing a new zsh configuration file.
        """,
    }
    print(manpages.get(cmd, "'{}' is an invalid command.".format(cmd)))