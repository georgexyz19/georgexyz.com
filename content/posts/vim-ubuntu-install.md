title: Vim Full Version Installation in Ubuntu and Tips
slug: vim-ubuntu-install
meta: Vim Ubuntu Installation Guide
tags: vim, ubuntu, linux
date: 2019-04-01 12:45
modified: 2020-06-02 16:24


Ubuntu 18.04 comes with a stripped down version of Vim. If you want to use Vim for 
serious work, you want the full version. 

### Vim Installation

The default version is started via command `vi`. The `vi --version` command shows 
the version information. Note the Line 5 below shows "Small version without GUI". 

```
VIM - Vi IMproved 8.0 (2016 Sep 12, compiled Apr 10 2018 21:31:58)
Included patches: 1-1453
Modified by pkg-vim-maintainers@lists.alioth.debian.org
Compiled by pkg-vim-maintainers@lists.alioth.debian.org
Small version without GUI.  Features included (+) or not (-):
+acl               -extra_search      -mouse_netterm     -tag_old_static
-arabic            -farsi             -mouse_sgr         -tag_any_white
...
+ex_extra          -mouse_jsbterm     +tag_binary 
   system vimrc file: "$VIM/vimrc"
     user vimrc file: "$HOME/.vimrc"
 2nd user vimrc file: "~/.vim/vimrc"
      user exrc file: "$HOME/.exrc"
       defaults file: "$VIMRUNTIME/defaults.vim"
  fall-back for $VIM: "/usr/share/vim"
Compilation: gcc -c -I. -Iproto -DHAVE_CONFIG_H   -Wdate-time  -g -O2 
-fdebug-prefix-map=/build/vim-NQEcoP/vim-8.0.1453=. -fstack-...

```

If you type command `vim` in bash, it will tell you that "command vim not found". 

```
george@X250:~$ vim
Command 'vim' not found, but can be installed with:
sudo apt install vim
sudo apt install vim-gtk3
sudo apt install vim-tiny
sudo apt install neovim
sudo apt install vim-athena
sudo apt install vim-gtk
sudo apt install vim-nox
```

Those three commands remove the existing vim-tiny and install the full version with GUI
vim-gtk3 in Ubuntu 18.04 or Xubuntu. 

```
sudo apt-get remove vim-tiny
sudo apt-get update
sudo apt-get install vim-gtk3
```

You can then check the vim version by command `vim --version`. 

### Basic Vim Settings

Vim automatically loads `~/.vimrc` file during startup. Some default settings of vim 
do not make sense. Below are some most basic vim settings. 

```
" ~/.simple.vimrc file; $vim -u ~/.simple.vimrc to load
set nocompatible              " required
filetype plugin on
syntax enable

"path and find, fuzzy file finder
set path+=**  " search subdir recursively, find ...
set wildmenu

set number " show line numbers

" Set ignore case, highlight, and incremental searches
set ignorecase
set hlsearch
set incsearch

```

### Vim Tips

#### Startup

Vim loads `~/.vimrc` by default, and you can change the behavior by using `-u` option on 
command line.

```
$vim -u ~/.simple.vimrc filename
$vim -u NONE  # do not load any config file
```

#### Set Initial Console Window Size

On Linux terminal, you can use `set lines=50 columns=100` to set initial console size. 
I have those lines in my `~/.vimrc` file. 

```
if exists("+lines")
  set lines=80
endif
if exists("+columns")
  set columns=120
endif
```

Source: [an article](https://vim.fandom.com/wiki/Maximize_or_set_initial_window_size) on fandom.com


#### Fuzzy Find

The following two settings help the `:find` command to do file fuzzy finding. 

```
set path+=**
set wildmenu
:find *cache # Press Tab key to find file name with cache
```

Source: [a video talk](https://youtu.be/XA2WjJbmmoM) on youtube

#### Auto Complete

Vim itself has auto complete function built in. In the insert mode, you can type a 
few letters such as 'Com', and then press `^n` to bring up auto complete menu. It 
is very handy when you are programming because you often need to type variable and 
class names multiple times on a file. 

^x^n
: Search in this file, ^ represents Ctrl key 

^x^f
: Search filename

^x^]
: Search tag

^n
: search by default

^n  ^p
: next prev on the menu

#### Current Filename

Command `^g` shows the name of the current file. Or you can type the following vim 
commands. 

```
:echo @%
:!ls %:p  # will show absolute path of file
```

#### Navigation

Keys `h j k l` are the basic navigation commands in noraml mode. Commands `w b e` 
jump cursor to next word, begin of word, or end of word. Other common navigation 
commands are listed below. 

gg
: move cursor to top

G
: move cursor to bottom

:`<n>`
: jump cursor to line number n, or `<n>G`

^e
: show an extra line

^y
: opposite of ^e

^d
: move down half screen

^u
: move up half screen

%
: matching ( { or [

H
: move cursor to top

M
: move cursor to middle

L
: move cursor to low corner


