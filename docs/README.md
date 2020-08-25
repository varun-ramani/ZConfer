![Zconfer Logo](./images/banner.png)

## Introduction
**Hey! It's a package manager for ZSH! (And it's a bunch of other stuff too)**

Managing your ZSH configuration can be tedious, thankless toil. Solutions like Oh My Zsh address this problem admirably, but *you still have to spend time messsing around with configuration files!* ZConfer abstracts away the task of configuration behind a easily usable command line interface, so you can get back to focusing on what actually matters.

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
  * [The Plugin System](#the-plugin-system)
	* [Browsing and Listing Plugins](#browsing-and-listing-plugins)
	* [Adding and Removing Plugins](#adding-and-removing-plugins)
	* [Enabling and Disabling Plugins](#enabling-and-disabling-plugins)

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

