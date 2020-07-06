echo "\033[1;31mZConf Uninstaller :(\033[0m"
echo "\033[1;31m--------------------\033[0m"

printf "\033[1;33mThe following will be removed:\n\t$HOME/.zconf/\n\t$HOME/bin/zconf\n\t$HOME/.zshrc? (y/n) \033[0m"
if ! read -q; then
    exit
fi

echo
echo "Now deleting $HOME/.zconf/, $HOME/bin/zconf, and $HOME/.zshrc"
rm -rf $HOME/.zconf $HOME/bin/zconf