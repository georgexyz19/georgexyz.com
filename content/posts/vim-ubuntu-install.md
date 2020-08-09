title: Vim Tips
slug: vim-tips
meta: Vim Installation And Vim Tips
tags: vim, tip, linux
date: 2019-04-01 12:45
modified: 2020-08-09 17:37


Ubuntu 18.04 comes with a stripped down version of Vim. If you want to use Vim for 
serious work, you want the full version. 

### Vim Installation

The default version is started via command `vi`. The `vi --version` command shows 
the version information. Note the Line 5 below shows "Small version without GUI". 
The output also contains the list of setting files Vim will load during startup. 

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
syntax enable   " or syntax off/on

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

*Source: [an article](https://vim.fandom.com/wiki/Maximize_or_set_initial_window_size) on fandom.com.*


#### Fuzzy Find

The following two settings help the `:find` command to do file fuzzy finding. 

```
set path+=**
set wildmenu
:find *cache # Press Tab key to find file name with cache
```

*Source: [a video talk](https://youtu.be/XA2WjJbmmoM) on youtube.*

#### Auto Complete

Vim itself has auto complete function built in. In the insert mode, you can type a 
few letters such as 'Com', and then press `^n` to bring up auto complete menu. It 
is very handy when you are programming because you often need to type variable and 
class names multiple times on a file. 

^x^n
: search in this file, ^ represents Ctrl key 

^x^f
: search filename

^x^]
: search tag

^n
: search by default

^n  ^p
: next prev on the menu

^y
: confirm selection, yes

^e
: exit menu

#### Current Filename

Command `^g` shows the name of the current file. Or you can type the following vim 
commands. 

```
:echo @%
:!ls %:p  # will show absolute path of file
```

#### Navigation

Keys `h j k l` are the basic navigation commands in normal mode. Commands `w b e` 
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

H, M, L
: move cursor to top, middle, and lower corner

^o
: go to old cursor position

^i
: go to next cursor position

#### Common Shortcuts

Vim is in a different league comparing to other text editors. It does not have 
some common shortcuts other editors have. But some of those shortcuts are so 
common, it is better to customize vim to support them. For example, the 
command `:saveas` is sometimes very convenient. 

The settings below add `Ctrl+s` shortcut for saving file.  Command `:update` is 
like `:write`, but only write when buffer has been modified.

```
noremap <silent> <C-S>  :update<CR>
vnoremap <silent> <C-S> :<C-C>:update<CR>
inoremap <silent> <C-S> <C-O>:update<CR>
```

This shortcut also needs a setting in `.bashrc` file to work. 

```
stty -ixon  # stop tele-typewriter, 
            # -ixon enable xon/xoff flow control -i
```

By default command `^s` freezes vim in Ubuntu Linux, and `^q` un-freeze it. 
This [stackoverflow Q&A]() 
explains it very well. 

> `Ctrl + s` is a common command to terminals to stop updating, it was a way to slow 
> the output so you could read it on terminals that did not have a scrollback 
> buffer. `Ctrl + q` command gets terminal going again. Put this line in .bashrc to 
> disable flow control for terminal entirely.


#### Spell Check

Vim has a built in spell checker. You use `set spell` to turn it on 
and `set nospell` to turn it off.  Here are some other commands on how to 
use it.

setlocal spell
: for current buffer only

]s
: move to next misspelled word

[s
: previous misspelled word

z=
: cursor on the word, list of suggested words

zg
: the word is correct, add it to personal dictionary

The `spelllang` settings is to specify the language, and the default is `en`. 
You can set it to `en_us` to specify American English. You can also use 
`spellfile` setting to specify a personal dictionary file for `zg` command. 

*Source: [an article](https://www.linux.com/training-tutorials/using-spell-checking-vim/) on linux.com & 
[a blog post](http://thejakeharding.com/tutorial/2012/06/13/using-spell-check-in-vim.html) by Jake Harding.*

#### GNOME Terminal Shortcuts

The Linux Mint comes with Gnome terminal. You can open additional tabs by pressing
shortcut `Ctrl + Shift + t`, and move to next tab by pressing `Ctrl + PageDown`. 
This does not necessarily relate to Vim, but I often use them so they are listed here. 

Another useful terminal shortcut is `Ctrl + z` which puts current application Vim 
in the background and suspended. After running some bash commands, you can type `fg` 
command to bring Vim back to foreground. Or you can use `:!` followed by a bash 
command to execute the command inside Vim. 

#### Copy and Paste via Clipboard

Copying texts to and from Vim using the `Ctrl + c` and `Ctrl + v` does not work. 
You could use Gnome terminal shortcuts `Ctrl + Shift + c` and `Ctrl + Shift + v`, 
but sometimes it does not work very well. 

I often use the *clipboard register* (`"+`) to copy and paste texts in and out of Vim. Here 
are the steps to copy texts into Vim, 

1. Copy texts in another program such as Firefox.
2. `Alt + Tab` switch focus to Vim.
3. Use command `"+p` to paste the texts.

Here are the steps to copy texts out of Vim to another program.

1. Use `v` command to visually select texts in Vim.
2. Type command `"+y` to copy the texts to clipboard.
3. In another program, use `Ctrl + v` to paste the texts. 

There is an 
[online Q&A](https://superuser.com/questions/61226/configure-vim-for-copy-and-paste-keyboard-shortcuts-from-system-buffer-in-ubuntu)
on how to map `Ctrl + c` and `Ctrl + v` to copy and paste behavior, but I have not 
set it up in my `.vimrc` file. 

#### Work Sessions

When you have 10 or more text files open in Vim and need to reboot your computer, you 
can use session commands to save the Vim work status and load them later.

:mksession ~/work1.session
: save the current work status

:source ~/work1.session
: load the saved session in Vim

vim -S ~/work1.session
: bash command to load vim and work session

#### Manage Buffers

Text files opened in Vim are called buffers. You can open multiple files with bash 
command like this `vim *.py`, and all python files in current directory will open 
in Vim as buffers. The command `:ls` shows all buffers in current vim session. Note 
that command `:!ls` will execute a single bash command `ls`. 

On the list generated by the `:ls` command, `%` represents current buffer and `#` 
represents alternate buffer. You can switch between the current buffer and 
alternate buffer. The `+` symbol on the list represents the file has been 
modified but not saved.  The commands listed below are for navigating between buffers.

When writting Python programs in Vim, you can run the command `:!python3 %` 
to run the current file. 

:bnext, bprevious, bfirst, blast
: next, previous, first, and last buffer

:b5
: open buffer number 5 

:bdelete 5, 6, 8
: close buffer numbers 5, 6, and 8

:5,7bdelete
: delete buffer numbers 5, 6, and 7

:edit file1
: open file1 as an additional buffer

:find file1
: open file1, this command also searches sub-directories

:b# or ^6
: switch between current buffer and alternate buffer

#### Map Caps Lock Key

Some people recommend to map Caps Lock key to Esc key when using Vim. Stackoverflow 
has a Q&A on how to do it. The following two lines of code in .vimrc file will 
do the trick. When leaving Vim, it will remap the key back to Caps Lock. The 
xmodmap software is already installed in Linux Mint, so no installation is 
needed. 

```
au VimEnter * silent! !xmodmap -e 'clear Lock' 
    -e 'keycode 0x42 = Escape'
au VimLeave * silent! !xmodmap -e 'clear Lock' 
    -e 'keycode 0x42 = Caps_Lock'
```

*Source: [an stackoverflow Q&A](https://stackoverflow.com/questions/2176532/how-to-map-caps-lock-key-in-vim)*

