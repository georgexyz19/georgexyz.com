title: Linux Mint Applications
slug: linux-mint-applications
date: 2020-09-11 10:01
modified: 2020-09-11 10:01
tags: linux, linux mint, software utility
note: discuss linux mint applications
no: 54

I have been using Linux Mint for over a year.  It is the time to get more
serious and examine applications that are popular in Linux Mint. Below is
*System Info* app screen which shows the OS version and other related info.  I
will keep updating this post to add more contents. 

<div style="max-width:800px">
  <img class="img-fluid pb-3" src="/images/lm-apps/sysinfo.png" alt="Sys Info">
</div>

###GNOME Terminal

Linux Mint comes with *GNOME Terminal* emulator. It is called *Terminal* on the
desktop menu. Most of my work in Linux Mint are conducted through this program.
One nice thing about the *Terminal* program is the integration with the desktop 
system, and it can be launched through the context menu *Open in Terminal*. 

<div style="max-width:800px">
  <img class="img-fluid pb-3" src="/images/lm-apps/context-menu.png"
alt="Context Menu">
</div>


Below is a *Terminal* window in default size 80 * 24.

<div style="max-width:800px">
  <img class="img-fluid pb-3" src="/images/lm-apps/terminal.png"
alt="Terminal window">
</div>

The version in Linux Mint 20 is 3.26.1.1. Here is the About window when you
choose menu Help -> About.  

<div style="max-width:800px">
  <img class="img-fluid pb-3" src="/images/lm-apps/terminal-about.png"
alt="Terminal About">
</div>

The program has a better than average help system when you choose the menu Help
-> Contents.  The "Overview of a terminal" section has definitions for terms
such as *Terminal*, *Shell*, *Prompt*. 

<div style="max-width:800px">
  <img class="img-fluid pb-3" src="/images/lm-apps/help-contents.png"
alt="Help Contents">
</div>

The *Use tabs* section explains that *Ctrl + Shift + t* shortcut is to open new
tab and *Ctrl + Shift + w* shortcut is to close a tab. 

<hr/>

###GNOME Screenshot

The Linux Mint 20 comes with a screenshot app which is actually part of GNOME
desktop system. The official name is *gnome-screenshot*. Below is the version
info under the Terminal. 

```
george@george-desktop:~$ gnome-screenshot --version
gnome-screenshot 3.36.0
george@george-desktop:~$ ls -la $(which gnome-screenshot)
-rwxr-xr-x 1 root root 88824 Apr 27 06:21 /usr/bin/gnome-screenshot

george@george-desktop:~$ gnome-screenshot --help
Usage:
  gnome-screenshot [OPTION…]
...

``` 

When I am researching this app online, I find an online article saying that
GIMP also has a screenshot funtion built in.  You can open the screenshot
window by clicking menu item File -> Create -> Screenshot.  The first figure below
is *gnome-screenshot* window and the second figure is GIMP screenshot window. 
 
<div style="max-width:800px">
  <img class="img-fluid pb-3" src="/images/lm-apps/lm-screenshot.png"
alt="LM screenshot app">
</div>

<div style="max-width:800px">
  <img class="img-fluid pb-3" src="/images/lm-apps/Gimp-screenshot.png"
alt="Gimp screenshot">
</div>
