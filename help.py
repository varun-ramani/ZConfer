def overview():
    overview_string = """
ZConf by Varun Ramani
usage: zconf <command> [<args>]

Commands Available:
    help            Prints this overview or a command's manpage
    init            Post-installation step; initializes ZConf for first use
    path            Provides path management functionality
    plugin          Provides plugin management functionality
    alias           Provides alias management functionality
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