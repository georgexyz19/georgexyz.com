title: Vim Tips
slug: vim-tips
meta: Vim Installation And Vim Tips
tags: vim, linux
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
......
Small version without GUI.  Features included (+) or not (-):
......
   system vimrc file: "$VIM/vimrc"
     user vimrc file: "$HOME/.vimrc"
   ......
```

If you type command `vim` in bash, it will tell you that "command vim not found". 
Those three commands remove the existing vim-tiny and install the full version with GUI
vim-gtk3 in Ubuntu/Linux Mint. 

```
sudo apt-get remove vim-tiny
sudo apt-get update
sudo apt-get install vim-gtk3
```

You can then check the vim version by command `vim --version`. 

### Basic Vim Settings

Vim automatically loads `~/.vimrc` file during startup. Some default settings of vim 
do not make sense. Below are some basic vim settings. I am using those settings under
Linux Mint.  Other OS settings may differ slightly. 

```
" ~/.vimrc file, keep it short and neat

set nocompatible              " required
filetype plugin on
syntax enable

"path and find, fuzzy file finder
set path+=**  " search subdir recursively, find ...
set wildmenu
set wildignore+=**/node_modules/**
set wildignore+=**/venv/**

set number

" Set ignore case, highlight, and incremental searches
set ignorecase
set hlsearch
set incsearch

set lines=38
set columns=140

" Ctrl + s to save file
noremap <silent> <C-S>  :update<CR>
vnoremap <silent> <C-S> :<C-C>:update<CR>
inoremap <silent> <C-S> <C-O>:update<CR>

"shortcut ^l to mute highlighting
nnoremap <silent> <C-l> :<C-u>nohlsearch<CR><C-l>

autocmd BufEnter * let &titlestring = ' ' . expand("%:p")
set title

" show tab char as >---
set list
set listchars=tab:>-

" create command :Showspace for double spaces before line end
command Showspace highlight ExtraWhitespace ctermbg=red guibg=red | 
        \ match ExtraWhitespace /\s\s$/
command Shownospace match none 

" spell check command type :Spellcheck to turn on, :set nospell to turn off
command Spellcheck setlocal spell spelllang=en_us 
```

I try to keep the `.vimrc` file simple so people can easily understand the script and 
modify it. Some contents are removed (such as mapping `Esc` key to `CapsLock`) if they 
are not used in an extended period of time. 

### Vim Tips

#### Startup

Vim loads `~/.vimrc` by default, and you can change the behavior by using `-u` option on 
command line.

```
$vim -u ~/.simple.vimrc filename
$vim -u NONE  # do not load any config file
```

#### Set Initial Console Window Size

On Linux Mint terminal, you can use `set lines=50 columns=100` to set initial console size. 
I have those lines in my `~/.vimrc` file. Those numbers seem to work well in Linux Mint.

```
set lines=38
set columns=140
```

*Source: [an article](https://vim.fandom.com/wiki/Maximize_or_set_initial_window_size) on fandom.com.*


#### Fuzzy Find

The following two settings help the `:find` command to do file fuzzy finding. 

```
set path+=**
set wildmenu
:find *cache # Press Tab key to find file name with cache
```

To exclude a directory from the search, use this setting. 

```
set wildignore+=**/node_modules/**
set wildignore+=**/venv/**
```

Source: [a video talk](https://youtu.be/XA2WjJbmmoM) on youtube, 
Source #2: [Stackexchange Q&A](https://vi.stackexchange.com/questions/11644/ignore-folders-when-performing-find-command). 

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

The two lines of code below show the file path and name as the title of Gnome 
Terminal window (under Linux Mint).  Source is this online 
[Q&A post](https://askubuntu.com/questions/438401/how-to-display-the-name-of-file-which-i-am-currently-editing-with-vim-on-termina). 

```
autocmd BufEnter * let &titlestring = ' ' . expand("%:p")
set title
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
: matching `( { or [`

H, M, L
: move cursor to top, middle, and lower corner

^o
: go to old cursor position

^i
: go to next cursor position

gj
: move down one displayed line when a long line is auto wrapped

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

This is one of those things that turn people off, especially new Vim users. 

#### Spell Check

Vim has a built in spell checker. You use `set spell` to turn it on 
and `set nospell` to turn it off.  Here are some other commands on how to 
use it.

setlocal spell
: for current buffer only

setlocal spell spelllang=en_us
: check current buffer for US English

]s
: move to next misspelled word

`[s`
: previous misspelled word

z=
: cursor on the word, list of suggested words

zg
: the word is correct, add it to personal dictionary

The `spelllang` settings is to specify the language, and the default is `en`. 
You can set it to `en_us` to specify American English. You can also use 
`spellfile` setting to specify a personal dictionary file for `zg` command. 

English is my second language, and I often rely on the spell checker. It is 
one of those Vim features that some people do not need but other people use it 
all the time.

*Source: [an article](https://www.linux.com/training-tutorials/using-spell-checking-vim/) on linux.com & 
[a blog post](http://thejakeharding.com/tutorial/2012/06/13/using-spell-check-in-vim.html) by Jake Harding.*

#### GNOME Terminal Shortcuts

The Linux Mint comes with Gnome Terminal (`Ctrl + Alt + t` to launch). You can open additional 
tabs by pressing
shortcut `Ctrl + Shift + t`, and move to next tab by pressing `Ctrl + PageDown`. 
This does not necessarily relate to Vim, but I often use them so they are listed here. 

Another useful terminal shortcut is `Ctrl + z` which puts current application Vim 
in the background and suspended. After running some bash commands, you can type `fg` 
command to bring Vim back to foreground. Or you can use `:!` followed by a bash 
command to execute the command inside Vim. 

#### Copy and Paste via Clipboard

Copying texts to and from Vim using the `Ctrl + c` and `Ctrl + v` does not work.
The command `^c` is to generate a signal which tells the current process to
terminate, and command `^v` invokes "verbatim insert" in bash (see [an online
article](https://www.howtogeek.com/440558/how-to-copy-and-paste-text-at-linuxs-bash-shell/)) .
You could use Gnome terminal shortcuts `Ctrl + Shift + c` and `Ctrl + Shift +
v`, but sometimes it does not work very well. 

I often use the *clipboard register* (`"+`) to copy and paste texts in and out of Vim. Here 
are the steps to copy texts into Vim, 

1. Copy texts in another program such as Firefox.
2. `Alt + Tab` switch focus to Vim.
3. Use command `"+p` to paste the texts.

Here are the steps to copy texts out of Vim to another program.

1. Use `v` command to visually select texts in Vim.
2. Type command `"+y` to copy the texts to clipboard.
3. In another program, use `^v` to paste the texts. 

There is an 
[online Q&A](https://superuser.com/questions/61226/configure-vim-for-copy-and-paste-keyboard-shortcuts-from-system-buffer-in-ubuntu)
on how to map `^c` and `^v` to copy and paste behavior, but I have not 
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

When writing Python programs in Vim, you can run the command `:!python3 %` 
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

#### Vim Command to Reflow Texts to 80 Columns. 

When writting articles in Vim, I often need to reflow texts after some editing. To
reflow texts, the first step is to set the `textwidth` and the second step is
to select texts and reflow with command `gq`. 

You can set the `textwidth` to 80 (:set textwidth=80 or :set tw=80), then use
`gg` to move cursor to the start of the file and type `gqG` to reflow 
the whole article. The command `gq` also works with visual selection.  You
can use command `vipgq` to select the paragraph first and then reflow. Or you
can use `gqap` to reflow current paragraph, and `gq}` reflow texts from current
cursor to end of the paragraph. Note you can select a paragraph by typing `vip` or
`vap` 

Command `gw` is similar to `gq`.  Here is the quote from help page. 

> gw: Format the lines that {motion} moves over. Similar to 
> gq but puts the cursor back at the same position in the text. 

*Source: [an stackoverflow Q&A](https://stackoverflow.com/questions/3033423/vim-command-to-restructure-force-text-to-80-columns)*

#### Run Commands on Multiple Lines

If you want to run a normal mode command on a range of lines, you can use the
`normal` command.  For example if you want to comment out line 4 to 6 of
.bashrc file, you can use `V` to select those lines and apply command
`:'<,'>normal i# ` to insert a character (#) in font of each line. 

```
# Load pyenv automatically by adding
# the following to ~/.bashrc:

export PATH="/home/george/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"

```

*Source: Practical Vim Second Edition by Drew Neil Page 63, Tip 30*

#### Save Readonly File

Here is an online post about 
[how to save read only files in vim](https://catonmat.net/sudo-vim). 

This is the command to save a readonly file in Vim. 

```
w !sudo tee % >/dev/null
```

The bash command `tee` is itself somewhat magical, and I do not fully understand how
the above command works. 

#### Auto Indent

The `>>` command is to indent a line in normal mode.  The operator `>` is for an 
object or visual selection.  When indenting or un-indenting, lines are shifted 
one `shiftwidth` to the right or left (e.g., :set shiftwidth=4).

The `==` command is auto indent, and `4==` command will auto indent 4 lines. 

#### Convert Tabs to Spaces

If you want to convert tabs to spaces for copied text, the simple answer is 
to use those two commands. 

```
:set tabstop=4
:retab
```
If the `expandtab` option is set, vim will insert space when the tab 
key is pressed (:set expandtab). The option `tabstop` controls the 
number of spaces that will be inserted when the tab key is pressed 
(:set tabstop=4). The `shiftwidth` option is for indent command `>>`. 
Yes, those option names are confusing. 

Source: [fandom.com article](https://vim.fandom.com/wiki/Converting_tabs_to_spaces)

#### Show Tabs As Visible Characters

To show tabs as visible characters in Vim, use those two settings. 

```
set list
set listchars=tab:>-
```
The second line will set tabs as something like this `>---`. 

To highlight two trailing spaces before the line end, use those two commands. 

```
:highlight ExtraWhitespace ctermbg=red guibg=red
:match ExtraWhitespace /\s\s$/
```
Or add this line to the `.vimrc` file. This is mainly for markdown (`.md`) files. 
Enter command `:Showspace` to display double spaces before line end, and `:Shownospace` 
to clear the highlight. 

```
command Showspace highlight ExtraWhitespace ctermbg=red guibg=red | 
             \ match ExtraWhitespace /\s\s$/
command Shownospace match none 
```


Source: [Stackexchange.com Q&A](https://vi.stackexchange.com/questions/422/displaying-tabs-as-characters), [SO Q&A for Trailing Space](https://stackoverflow.com/questions/4617059/showing-trailing-spaces-in-vim)

#### Find and Search

The command to scan line for a character is `f{char}`, and `F{char}` reverse the order 
and scan backward. Press `;` for repeat and `,` for reverse.  The command `t{char}` stops
the cursor before the character. Command `f` is for find and `t` is for til. 

The command `/pattern<CR>` is to search a word pattern. Press `n` for next and `N` for 
reverse search. Command `*` is to search the word that is under the cursor. 

Substitution command is `:s/target/replacement`. Press `&` for repeat. Command `:%s/...`
is to search all lines. Add an option `/g` to the end `:s/tar/rep/g` to replace multiple 
matches on a line. 

Source: Page 9 of Drew Neil's *Practical Vim* Book


#### Change Letter Case

The command `U` is to change visually selected text to uppercase, and `u` to lowercase. 
Tilde `~` command is to swap cases in a visual selection. 

Without using a visual selection, `gU` is the command to make characters uppercase, and 
`gu` for lowercase. 

Source: [Stackoverflow Q&A](https://stackoverflow.com/questions/2946051/changing-case-in-vim)


#### Bash Tree Command

I often use `tree` command to list files in a directory (need apt install in Linux Mint). 
If you want to exclude a sub directory such as `venv`, the command looks like this. 

```
$tree -I venv
$tree -I 'venv|__pycache__'   # note the quote(') around two sub dirs
$tree -L 2        # -L is for levels down
$tree -I venv -v  # sort by name, or --sort=name
```

This is not necessary a Vim tip, but I have not found a good place to put it. 

Source: [zaiste.net blog post](https://zaiste.net/posts/tree-ignore-directories-patterns/)


#### Nerdtree Plugin

Vim has a built in file/directory management tool, but it is not very good.  Nerdtree plugin 
is nice when you are working on a large project. Here are the steps for managing plugins 
with Vundle.

- Use git to download Vundle. 
<div class="ml-5">
```
$ git clone https://github.com/gmarik/Vundle.vim.git \ 
            ~/.vim/bundle/Vundle.vim
```
</div>
- Setup a new .plugin.vimrc file and add those statements. Note at the end of this file 
it loads `.vimrc` file, so you do not need to keep two copies of `.vimrc`. 

<div class="ml-5">
```
" ~/.vimrc file

set nocompatible              " required
filetype off

set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()

Plugin 'gmarik/Vundle.vim'

" add all your plugins here

Plugin 'scrooloose/nerdtree'
Plugin 'jistr/vim-nerdtree-tabs'

Plugin 'mattn/emmet-vim'
Plugin 'nvie/vim-flake8'

" plugin add ends here

call vundle#end()            " required
filetype plugin on    " required

" for Nerdtree
let NERDTreeIgnore=['\.pyc$', '\~$'] "ignore files in NERDTree
nnoremap <C-N> :NERDTree<CR>
autocmd VimEnter * NERDTree

noremap <C-H><C-H> <C-W><C-H>
noremap <C-L><C-L> <C-W><C-L>
noremap <C-J><C-J> <C-W><C-J>
noremap <C-K><C-K> <C-W><C-K>

let g:user_emmet_mode='n'    "only enable normal mode functions.
let g:user_emmet_leader_key=',' "activate two ,

source ~/.vimrc
```
</div>

-  Inside Vim, run command `:PluginInstall`.  Vundle will download and setup the 
plugins listed in .plugin.vimrc file. Run command `:NERDTree` to bring up 
Nerdtree window on the left. 
-  Setup a bash alias for `vimplugin` in `.bashrc` file.
<div class="ml-5">
```
alias pytree="tree -I 'venv|__pycache__' --sort=name "  # for tree
alias vimplugin="vim -u ~/.plugin.vimrc "
```
</div>

Source: [realpython.com article](https://realpython.com/vim-and-python-a-match-made-in-heaven/),
<span class="ml-2"></span>[Nerdtree github repo](https://github.com/preservim/nerdtree)

#### Nerdtree Shortcuts

Here are some shortcuts in Nerdtree. Once you become familiar with them, it is 
faster to navigate than a GUI file browser. 

- Press `m` to modify dir, `a` to add dir or file 
- `o` to open, `O` recursively open
- `x` to close open dir, `X` recursively close
- `C-W` + `h j k l` to move between windows
- Map `C-H` to move cursor to left side and `C-L C-L` to right side
<div class="ml-5">
```
noremap <C-H> <C-W><C-H>
noremap <C-L><C-L> <C-W><C-L>
```
</div>


#### Emmet Vim Plugin

The other Vim plugin I use is the [emmet-vim](https://github.com/mattn/emmet-vim). 
It is tedious to type html tags like `<div></div>` when coding web pages.

If you follow above steps and install Vundle to manage plugins, you can add this line to 
the `.plugin.vimrc` file. 

```
Plugin 'mattn/emmet-vim'
```

I also added those two settings in the same file as suggested in a youtube tutorial video.

```
let g:user_emmet_mode='n'    "only enable normal mode functions.
let g:user_emmet_leader_key=',' "activate two commas  
```

Here is the link to [the youtube tutorial](https://youtu.be/ha7oyvhgP04).

Link to the Github [emmet-vim source code repo](https://github.com/mattn/emmet-vim). 


#### Vim-Flake8 Plugin

I am adding a Python linter to my Vim setup. Below are the steps to set it up. 

* Add this line to `.plugin.vimrc` file.
<div class="ml-5">
```
Plugin 'nvie/vim-flake8'
```
</div>

* Install `flake8` to global Python interpreter.
<div class="ml-5">
```
pip install flake8
```
</div>

* Config flake8 to change max line lengths, add those two lines to `~/.config/flake8` file.
<div class="ml-5">
```
[flake8]
max-line-length = 120
```
</div>

* Run `:PluginInstall` vim command to install `vim-flake8`.

* When a Python file is open, press `<F7>` to run the linter.

References: [vim-flake8 repo](https://github.com/nvie/vim-flake8)


#### Links and References

[Vim Cheat Sheet](https://vim.rtorr.com/) 
is a nice single web page which includes common vim commands.


