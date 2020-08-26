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
* To browse plugins that are not installed but available in the repository:
  ```
  zconf plugin view remote
  ```


* To browse locally installed plugins:
  ```
  zconf plugin view local
  ```

* To browse all plugins:
  ```
  zconf plugin view all
  ```

#### Adding and Removing Plugins
* To install a new plugin:
  ```
  zconf plugin add <plugin>
  ```
  Example: 
  ```
  zconf plugin add z
  ```
  
* To uninstall a plugin:
  ```
  zconf plugin rm <plugin>
  ```
  Example:
  ```
  zconf plugin rm z
  ```

#### Enabling and Disabling Plugins:
* To make a plugin load when you start ZSH:
  ```
  zconf plugin enable <plugin>
  ```
  Example:
  ```
  zconf plugin enable z
  ```
  
* To prevent a plugin from loading when you start ZSH:
  ```
  zconf plugin disable <plugin>
  ```
  Example:
  ```
  zconf plugin disable z
  ```


### The Theme System
#### Browsing and Listing Themes
* To browse themes that are not installed but available in the repository:
  ```
  zconf theme view remote
  ```


* To browse locally installed themes:
  ```
  zconf theme view local
  ```

* To browse all themes:
  ```
  zconf theme view all
  ```

#### Adding and Removing Themes
Themes are automatically added when they are set for the first time. You don't ever *need* to add them manually.
* To manually add a theme:
  ```
  zconf theme add <theme>
  ```
  Example: 
  ```
  zconf theme add dracula
  ```
* To remove a theme:
  ```
  zconf theme rm <theme>
  ```
  Example:
  ```
  zconf theme rm dracula
  ```
  
#### Setting Themes
Themes are automatically added when they are set for the first time. You don't need to ever add them manually.

* Setting a new theme
  ```
  zconf theme set <theme>
  ```
  Example:
  ```
  zconf theme set dracula
  ```
  
* Reverting back to no theme
  ```
  zconf theme set notatheme
  ```
  

### PATH Management
You can use ZConfer to create, update, and delete individual PATH segments. If you would prefer not to delete a segment entirely, you can also enable/disable it. 
ZConfer will handle the task of concatenating all the segments with the existing PATH variable in order to create a meaningful PATH string.
**Note that at the moment, ZConfer can only manage the PATH segments that it created.**

#### Viewing PATH Segments
To print out all the registered PATH segments and their values:
```
zconf path view
```

#### Creating, Updating, and Deleting PATH Segments
* To add a new segment to PATH:
  ```
  zconf path set <segment> <value>
  ```
  Example:
  ```
  zconf path set android_tools /Users/varun/Android/Sdk/platform_tools
  ```
* To update an existing segment in PATH:
  Ignore the fact that it exists, and set it like it was a new segment.

* To delete a PATH segment (gets rid of it entirely):
  ```
  zconf path rm <segment>
  ```
  Example:
  ```
  zconf path rm android_tools
  ```
  
#### Enabling and Disabling PATH Segments
You can make ZConfer "ignore" a specific PATH segment by disabling it. Although the segment will remain in ZConfer's registry, it will be removed from PATH.
This is useful when you want to temporarily remove a PATH segment and plan to add it back later. Segments are enabled by default.
* To disable a segment:
  ```
  zconf path disable <segment>
  ```
* To enable a disabled segment:
  ```
  zconf path enable <segment>
  ```
