import os

home = os.environ['HOME']
zconf_home = home + "/.zconf"
zshrc = home + "/.zshrc"
zconf_main = zconf_home + "/managed_zshrc"
zshrc_backup = home + "/.zshrc.bak"

class jsondata:
    path = zconf_home + "/path.json"
    aliases = zconf_home + "/alises.json"

class modules:
    path = zconf_home + "/path.zsh"
    aliases = zconf_home + "/aliases.zsh"