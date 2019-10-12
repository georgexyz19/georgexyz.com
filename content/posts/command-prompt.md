title: Linux Mint Default Command Prompt String
slug: linux-command-prompt
meta: Explain default command prompt string in Ubuntu and Linux Mint
date: 2019-09-07 01:31
modified: 2019-09-07 01:31
tags: linux, linux mint, bash
note: 23
 

William Shotts' *The Linux Command Line* is an excellent book. It is written 
in a tutorial style and very easy to understand. The PDF file of the whole book is 
[freely available online](http://linuxcommand.org/tlcl.php). 

Chapter 13 of the book discusses how to customize linux command prompt. The default 
command prompt is defined by an environment variable named `PS1`. The `PS1` is 
defined as a long string in Linux Mint (or Ubuntu). See the screenshot below:

<img class="img-fluid pb-3" src="/images/command-prompt.png" alt="command-prompt">

The `PS1` string can be divided into three parts:

```
\[\e]0;\u@\h: \w\a\]
${debian_chroot:+($debian_chroot)}
\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\$
```

It is a little hard to understand the `PS1` string even after reading the book chapter. 
A few Google searches find other people are also asking the meaning of the string, 
and it has already been answered by someone. 

* `\[\e]0;\u@\h: \w\a\]` sets the title bar of terminal
    * `\[` starts a series of one or more non-printing characters
    * `\e]0;` is for setting terminal title, `\e` is the same as `\033`
    * `\u@\h \w` means username@hostname and working directory
    * `\a` marks the end of the title
    * `\]` ends non-printing characters
* `${var:+value}` means if `$var` is defined; then use `value`; else do nothing. The 
  `debian_chroot` on the second line is defined in the `/etc/bash.bashrc` file (discussed
   later in this article).
* `\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\$` is the actual
  command prompt
    * `\033[01;32m` is for color light green (Table 13-2 in the book)
    * `\033[00m` turns off color
    * `\033[01;34m` is for color light blue

The variable `debian_chroot` is defined in the `/etc/bash.bashrc` file as:

```
if [ -z "${debian_chroot:-}" ] && [ -r /etc/debian_chroot ]; then
    debian_chroot=$(cat /etc/debian_chroot)
```

It means that if the variable `$debian_chroot` is empty and the file `/etc/debian_chroot` 
is readable, the variable is assigned the content of the file.

Most explanations above are from two askubuntu web pages: 
[question 404341](https://askubuntu.com/questions/404341/where-can-i-find-a-complete-reference-for-the-ps1-variable) 
and 
[question 372849](https://askubuntu.com/questions/372849/what-does-debian-chrootdebian-chroot-do-in-my-terminal-prompt). 
