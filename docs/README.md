![Zconfer Logo](./images/banner.png)

## Introduction
**Hey look! It's a package manager for ZSH! (And it can do a ton of other stuff too!)**

Managing your ZSH configuration can be tedious, thankless toil. Solutions like Oh My Zsh address this problem admirably, but *you still have to spend time messsing around with configuration files!* ZConfer abstracts away the task of configuration behind an easily usable command line interface, so you can get back to focusing on what actually matters.

* ZConfer is a comprehensive plugin manager capable of adding, deleting, enabling, and disabling plugins.
* ZConfer can download new themes and enable them.
* ZConfer breaks your PATH into individual "segments", which can then be managed individually. ZConfer can also add new segments.
* ZConfer is an alias manager capable of adding, removing, and changing aliases.

## Table of Contents
* [Demo](#demo)
* [Setting Up](#setting-up)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
  * [The Init Step](#the-init-step)
* [Usage](#usage)
  * [Updating ZConfer](#updating-zconfer)
  * [The Plugin System](#the-plugin-system)
	* [Browsing and Listing Plugins](#browsing-and-listing-plugins)
	* [Adding and Removing Plugins](#adding-and-removing-plugins)
	* [Enabling and Disabling Plugins](#enabling-and-disabling-plugins)
  * [The Theme System](#the-theme-system)
	* [Browsing and Listing Themes](#browsing-and-listing-themes)
	* [Adding and Removing Themes](#adding-and-removing-themes)
	* [Setting Themes](#setting-themes)
  * [PATH Management](#path-management)
	* [Viewing PATH Segments](#viewing-path-segments)
	* [Creating, Updating, and Deleting PATH Segments](#creating-updating-and-deleting-path-segments)
	* [Enabling and Disabling PATH Segments](#enabling-and-disabling-path-segments)
  * [Alias Management](#alias-management)
	* [Viewing Aliases](#viewing-aliases)
	* [Creaing, Updating, and Deleting Aliases](#creating-updating-and-deleting-aliases)
	* [Enabling and Disabling Aliases](#enabling-and-disabling-aliases)
		

## Demo
*Installing Z, a plugin for quickly jumping to previously visited directories*:
![pluginstall](./images/pluginstall.gif)

*Aliasing 'ls' to 'ls -G'*:
![aliases](./images/aliases.gif)

## Setting Up
### Prerequisites
* `curl`
* `git`
* `python3`

### Installation
First, install ZConfer by piping the installer to a new ZSH session:
```
curl https://raw.githubusercontent.com/varun-ramani/zconfer/master/installer.zsh | zsh
```
Then run the init step.

### The Init Step
Run `$HOME/bin/zconf init` and respond to any prompts. Pretty simple, really.

## Usage
### Updating ZConfer
In its current state, this module just wraps a shell command that runs the updater script on this repository.
```
zconf update
```

### The Plugin System
Through ZConfer's plugin system, you can download new plugins, remove existing ones, and select which to load on startup. You can also view both locally installed and remotely available plugins.

#### Browsing and Listing Plugins
* Browse plugins that are not installed with `view remote`.
  ```
  zconf plugin view remote
  ```

* Browse installed plugins with `view local`.
  ```
  zconf plugin view local
  ```

* You can also `view all` plugins.
  ```
  zconf plugin view all
  ```

#### Adding and Removing Plugins
* ZConfer can easily `add` new plugins.
  Example: 
  ```
  zconf plugin add z
  ```
  
* To delete plugins, use `rm`.
  Example:
  ```
  zconf plugin rm z
  ```

#### Enabling and Disabling Plugins:
* Use `enable` to make a plugin load when you start ZSH.
  Example:
  ```
  zconf plugin enable z
  ```
  
* Plugins won't load if you `disable` them.
  Example:
  ```
  zconf plugin disable z
  ```


### The Theme System
#### Browsing and Listing Themes
* Browse themes that aren't installed with `view remote`.
  ```
  zconf theme view remote
  ```


* Browse installed themes with `view local`.
  ```
  zconf theme view local
  ```

* To browse all themes, use `view all`.
  ```
  zconf theme view all
  ```

#### Adding and Removing Themes
Themes are automatically added when they are set for the first time. You don't ever *need* to add them manually.
* However, you can `add` themes manually if you want.
  Example: 
  ```
  zconf theme add dracula
  ```
* To remove a theme, use `rm`.
  Example:
  ```
  zconf theme rm dracula
  ```
  
#### Setting Themes
* It's easy to `set` themes.
  Example:
  ```
  zconf theme set dracula
  ```
  
* You can also revert to no theme:
  ```
  zconf theme set notatheme
  ```
  

### PATH Management
You can use ZConfer to create, update, and delete individual PATH segments. If you would prefer not to delete a segment entirely, you can also enable/disable it. 
ZConfer will handle the task of concatenating all the segments with the existing PATH variable in order to create a meaningful PATH string.
**Note that at the moment, ZConfer can only manage the PATH segments that it created.**

#### Viewing PATH Segments
* You can `view` all registered PATH segments and their values.
  ```
  zconf path view
  ```

#### Creating, Updating, and Deleting PATH Segments
* The `set` command can both add and update PATH segments.
  ```
  zconf path set <segment> <value>
  ```
  Example:
  ```
  zconf path set android_tools /Users/varun/Android/Sdk/platform_tools
  ```
  
* Using `rm` deletes a segment.
    Example:
  ```
  zconf path rm android_tools
  ```
  
#### Enabling and Disabling PATH Segments
* If you might need a segment later, then `disable` it.
  Example:
  ```
  zconf path disable android_tools
  ```
  
* Recover disabled segments with `enable`.
  Example:
  ```
  zconf path enable android_tools
  ```

### Alias Management
#### Viewing Aliases
* The `view` command lists your aliases for you.
  ```
  zconf alias view
  ```
  
#### Creating, Updating, and Deleting Aliases
* You can use `set` to create and update aliases.
  ```
  zconf alias set <alias> '<value>'
  ```
  Example:
  ```
  zconf alias set ls 'ls -G'
  ```

* To delete aliases, use `rm`.
  Example:
  ```
  zconf alias rm ls
  ```
  
#### Enabling and Disabling Aliases
* The `disable` command is like `rm`, but it's reversible.
  Example:
  ```
  zconf alias disable ls
  ```

* Use `enable` to undo the disable operation.
  Example:
  ```
  zconf alias enable ls
  ```
