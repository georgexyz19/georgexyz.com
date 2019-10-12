title: Bash Command Line Editing Shortcuts
slug: bash-shortcuts
meta: This post summarize 8 bash shortcuts that should be memorized. 
date: 2019-10-12 13:19
modified: 2019-10-12 13:19
tags: linux, bash
note: None
no: 25


I recently spent sometime reading two Linux command line books.  The first is William Shotts' 
*The Linux Command Line (2e)*, and the second one is *Learning the Bash Shell* 
by Cameron Newbam and Bill Rosenblatt. Both books are good.  The first book is 
written in a tutorial style and easy to understand.  The second one is on 
Bash shell only and is more thorough. 

<div style="max-width:800px">
  <img class="img-fluid pb-3" src="/images/bash-books-crop.jpg" alt="bash-books"> 
</div>

The *Learning the Bash Shell* book is in its third edition, and the book was 
published in April 2005.  The first edition was published in 1995, so it is an 
old book.  The third edition covers Bash 3.0.  Bash 5.0 has already been 
released. However, most contents in the book still apply to current release. 

Chapter 2 of the book describes that Bash has two editing mode: emacs and vi. 
The default is emacs mode. When you open a Terminal window (Ctrl + Alt + T) in 
Ubuntu, the command line is in emacs editing mode.  You can change it to vi mode 
by command `set -o vi` and change it back by `set -o emacs`.  The emacs mode 
is adequate for most situations. The mode has some useful shortcuts (listed
below) in addition to common ones like Tab, Arrow Up, Arrow Down. 

1. `Ctrl + a` : Move cursor to the beginning of the line
2. `Ctrl + e` : Move cursor to the end
3. `Ctrl + r` : Search command history
4. `Ctrl + k` : Delete from cursor to the end of the line
5. `Ctrl + u` : Delete from the beginning of the line to cursor
6. `Ctrl + l` : Clear the screen
7. `Ctrl + t` : Transpose two character
8. `Ctrl + o` : Return, bring next line in history to command line

A reddit post 
"[do you use bash vi mode](https://www.reddit.com/r/vim/comments/a65qfe/do_you_use_bash_vi_mode/)" 
has some interesting discussion on 
whether to use vi mode.  I personally think emacs mode with the above shortcuts 
is good enough. 

