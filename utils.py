def colorprint(string, color):
    colorcodes = {
        "red": "\033[1;31m",
        "green": "\033[1;32m",
        "yellow": "\033[1;33m",
        "blue": "\033[1;34m",
        "magenta": "\033[1;35m",
        "cyan": "\033[1;36m",
        "gray": "\033[1;37m",
    }

    return "{}{}\033[0m".format(colorcodes.get(color, "\033[0m"), string)

def confirm(prompt):
    user_input = input(prompt)
    return user_input == 'y' or user_input == 'yes'

def write_file(path, string):
    with open(path, 'w+') as file:
        file.write(string)
        file.close()