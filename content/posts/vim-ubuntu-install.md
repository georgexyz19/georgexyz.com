title: Vim Full Version Installation in Ubuntu
slug: vim-ubuntu-install
meta: Vim Ubuntu Installation Guide
tags: vim, ubuntu, linux
date: 2019-04-01 12:45
modified: 2019-04-01 12:45


Ubuntu 18.04 comes with a stripped down version of Vim. If you want to use Vim for 
serious work, you need the full version. 

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
-autocmd           -file_in_path      -mouse_sysmouse    -tcl
-autoservername    -find_in_path      -mouse_urxvt       -termguicolors
-balloon_eval      -float             -mouse_xterm       -terminal
-balloon_eval_term -folding           +multi_byte        +terminfo
-browse            -footer            -multi_lang        -termresponse
+builtin_terms     +fork()            -mzscheme          -textobjects
-byte_offset       -gettext           -netbeans_intg     -timers
-channel           -hangul_input      -num64             -title
-cindent           +iconv             +packages          -toolbar
-clientserver      -insert_expand     -path_extra        -user_commands
-clipboard         -job               -perl              +vertsplit
-cmdline_compl     +jumplist          -persistent_undo   -virtualedit
+cmdline_hist      -keymap            -printer           +visual
-cmdline_info      -lambda            -profile           -visualextra
-comments          -langmap           -python            -viminfo
-conceal           -libcall           -python3           -vreplace
-cryptv            -linebreak         -quickfix          +wildignore
-cscope            -lispindent        -reltime           -wildmenu
-cursorbind        -listcmds          -rightleft         +windows
-cursorshape       -localmap          -ruby              +writebackup
-dialog            -lua               -scrollbind        -X11
-diff              -menu              -signs             +xfontset
-digraphs          -mksession         -smartindent       -xim
-dnd               -modify_fname      -startuptime       -xpm
-ebcdic            -mouse             -statusline        -xsmp
-emacs_tags        -mouse_dec         -sun_workshop      -xterm_clipboard
-eval              -mouse_gpm         -syntax            -xterm_save
+ex_extra          -mouse_jsbterm     +tag_binary 
   system vimrc file: "$VIM/vimrc"
     user vimrc file: "$HOME/.vimrc"
 2nd user vimrc file: "~/.vim/vimrc"
      user exrc file: "$HOME/.exrc"
       defaults file: "$VIMRUNTIME/defaults.vim"
  fall-back for $VIM: "/usr/share/vim"
Compilation: gcc -c -I. -Iproto -DHAVE_CONFIG_H   -Wdate-time  -g -O2 
-fdebug-prefix-map=/build/vim-NQEcoP/vim-8.0.1453=. -fstack-protector-strong 
-Wformat -Werror=format-security -DTINY_VIMRC -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=1 
Linking: gcc   -Wl,-Bsymbolic-functions -Wl,-z,relro -Wl,-z,now -Wl,--as-needed 
-o vim    -lSM -lICE -lXpm -lXt -lX11 -lXdmcp -lSM -lICE  -lm -ltinfo  -lselinux 
-lacl -lattr -ldl 

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

