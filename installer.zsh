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
if ! read -q; then
    exit
fi

echo
echo "Creating $HOME/.zconf/ if it doesn't already exist"
mkdir -p $HOME/.zconf

echo "Downloading zconf"
curl "https://raw.githubusercontent.com/varun-ramani/zconf/master/zconf.py" > $HOME/.zconf/zconf.py
echo "Downloading help module"
curl "https://raw.githubusercontent.com/varun-ramani/zconf/master/help.py" > $HOME/.zconf/help.py

echo "Making $HOME/bin directory if it doesn't already exist"
mkdir -p $HOME/bin

echo "Linking zconf into $HOME/bin/zconf"
ln -s $HOME/.zconf/zconf.py $HOME/bin/zconf

echo "Patching zconf for system installation of Python 3"
echo "#!$(command -v python3)" > $HOME/bin/this_is_a_temp_zconf_file && cat $HOME/bin/zconf >> $HOME/bin/this_is_a_temp_zconf_file && cat $HOME/bin/this_is_a_temp_zconf_file > $HOME/bin/zconf && rm $HOME/bin/this_is_a_temp_zconf_file

chmod +x $HOME/bin/zconf