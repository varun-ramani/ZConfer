def colorprint(string, color):
    colorcodes = {
        "red": "\033[1;31m",
        "green": "\033[1;32m",
        "yellow": "\033[1;33m",
        "blue": "\033[1;34m",
        "magenta": "\033[1;35m",
        "cyan": "\033[1;36m",
        "gray": "\033[1;37m",
        "bold": "\033[1;1m",
        "bold_red": "\033[1;91m",
        "bold_green": "\033[1;92m",
        "bold_yellow": "\033[1;93m",
        "bold_blue": "\033[1;94m",
        "bold_magenta": "\033[1;95m",
        "bold_cyan": "\033[1;96m",
        "bold_gray": "\033[1;97m",
    }

    return "{}{}\033[0m".format(colorcodes.get(color, "\033[0m"), string)

def confirm(prompt):
    user_input = input(prompt)
    return user_input == 'y' or user_input == 'yes'

def write_file(path, string):
    with open(path, 'w+') as file:
        file.write(string)

def read_file(path):
    with open(path, 'r') as file:
        toreturn = file.read()
        return toreturn