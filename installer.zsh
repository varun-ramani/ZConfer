echo "\033[1;32mZConf Installer\033[0m"
echo "\033[1;32m---------------\033[0m"

found_error=false
if ! command -v git &> /dev/null; then
    echo "\033[1;31mError: Git not found in PATH\033[0m"
    found_error=true
fi

if ! command -v python3 &> /dev/null; then
    echo "\033[1;31mError: Python 3 not found in PATH\033[0m"
    found_error=true
fi

if [[ $found_error == true ]]; then
    echo "Please correct the errors and try again."
    exit
fi

printf "\033[1;33mAll requirements met. Install ZConf? (y/n) \033[0m"
if read -q; then
    echo

    echo "Creating $HOME/.zconf if it doesn't already exist"
    mkdir -p $HOME/.zconf

    echo "Downloading zconf"
    curl "https://raw.githubusercontent.com/varun-ramani/zconf/master/zconf.py" > $HOME/.zconf/zconf.py
    echo "Downloading help module"
    curl "https://raw.githubusercontent.com/varun-ramani/zconf/master/help.py" > $HOME/.zconf/help.py
fi