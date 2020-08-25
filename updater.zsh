echo "\033[1;32mUpdating ZConfer\033[0m"

mods=('zconf' 'help' 'init' 'globals' 'utils' 'path' 'alias' 'plugin' 'theme' 'update')
for module in $mods; do
    echo "Downloading ${module} component"
    curl "https://raw.githubusercontent.com/varun-ramani/zconfer/master/${module}.py" -# > $HOME/.zconf/${module}.py
done

echo "Checking for ZConfer repository update"
cd $HOME/.zconf/repo && git pull > /dev/null && echo "Successfully updated!" || echo "No update found."

rm -rf $HOME/bin/zconf
ln -s $HOME/.zconf/zconf.py $HOME/bin/zconf

echo "Patching ZConfer for system installation of Python 3"
echo "#!$(command -v python3)" > $HOME/bin/this_is_a_temp_zconf_file && cat $HOME/bin/zconf >> $HOME/bin/this_is_a_temp_zconf_file && cat $HOME/bin/this_is_a_temp_zconf_file > $HOME/bin/zconf && rm $HOME/bin/this_is_a_temp_zconf_file

chmod +x $HOME/bin/zconf

export PATH="$PATH:$HOME/bin"
