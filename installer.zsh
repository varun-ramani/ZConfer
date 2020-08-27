echo "\033[1;32mZConfer Installer\033[0m"
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

printf "\033[1;33mAll requirements met. Install ZConfer? (y/n) \033[0m"
if ! read -q; then
    exit
fi

echo
echo "Creating $HOME/.zconf/ if it doesn't already exist"
mkdir -p $HOME/.zconf

mods=('zconf' 'help' 'init' 'globals' 'utils' 'path' 'alias' 'plugin' 'theme' 'update')
for module in $mods; do
    echo "Downloading ${module} component"
    curl "https://raw.githubusercontent.com/varun-ramani/zconfer/master/${module}.py" -# > $HOME/.zconf/${module}.py
done

echo "Cloning ZConfer's repository"
git clone https://github.com/varun-ramani/zconfer_repo.git ~/.zconf/repo

echo "Making $HOME/bin directory if it doesn't already exist"
mkdir -p $HOME/bin

echo "Creating launcher"
echo 'python3 $HOME/.zconf/zconf.py $@' >> $HOME/bin/zconf
echo 'exec zsh' >> $HOME/bin/zconf
chmod +x $HOME/bin/zconf

export PATH="$PATH:$HOME/bin"

echo "\033[1;32mInstallation complete. Run zconf init now.\033[0m"
