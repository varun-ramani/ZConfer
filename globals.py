import os

home = os.environ['HOME']
zconf_home = home + "/.zconf"
zshrc = home + "/.zshrc"
zconf_main = zconf_home + "/managed_zshrc"
zshrc_backup = home + "/.zshrc.bak"

plugins_dir = zconf_home + "/plugins"
repo_dir = zconf_home + "/repo"
themes_dir = zconf_home + "/themes"

class jsondata:
    path = zconf_home + "/path.json"
    repo = repo_dir + "/repo.json"
    aliases = zconf_home + "/alias.json"
    plugins = zconf_home + "/plugin.json"
    themes = zconf_home + "/theme.json"

class modules:
    path = zconf_home + "/path.zsh"
    aliases = zconf_home + "/alias.zsh"
    plugins = zconf_home + "/plugin.zsh"
    themes = zconf_home = "/themes.zsh"
