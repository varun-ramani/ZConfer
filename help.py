def help_overview():
    overview = """
ZConf by Varun Ramani
usage: zconf <command> [<args>]

Commands Available:
    help            Prints this overview or a command's manpage
    init            Post-installation step; initializes ZConf for first use
    path            Invokes the path management tool
    install         Installs a plugin
    uninstall       Uninstalls a plugin
    enable          Load a plugin on shell startup
    disable         Prevent plugin from loading on shell startup
    load            Sources a plugin in-place; may not work properly
    """
    print(overview)

def help_command(command):
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
    print(manpages.get(command, "'{}' is an invalid command.".format(command)))