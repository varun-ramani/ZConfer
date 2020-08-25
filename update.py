from utils import colorprint
import os

def update():
    os.system('curl https://raw.githubusercontent.com/varun-ramani/zconfer/master/updater.zsh | zsh')
