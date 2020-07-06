echo "\033[1;31mZConf Uninstaller :(\033[0m"
echo "\033[1;31m--------------------\033[0m"

printf "\033[1;33mThe following will be removed:\n\t$HOME/.zconf/\n\t$HOME/bin/zconf\nContinue? (y/n) \033[0m"
if ! read -q; then
    exit
fi

echo
echo "Deleting $HOME/.zconf/"
rm -rf $HOME/.zconf
echo "Deleting $HOME/bin/zconf"
rm -rf $HOME/bin/zconf