title: Geany Editor
slug: geany-editor
meta: This post discusses how to setup geany editor
date: 2019-07-19 15:45
modified: 2019-07-19 15:45
tags: software utility
status: draft
note: this note is based on a hard copy note
no: 21


Geany is a lightweight editor mainly for programmers.  I heard Geany 
editor from *Python Crash Book* and I liked it. The default settings of 
Geany in Ubuntu are not the best, and this post discusses my preferred 
settings. 

Here is the command to install Geany in Ubuntu. The current version in 
Ubuntu repo is 1.32.

```
$sudo apt-get install geany
```

The commands below install the latest version 1.35.

```
$sudo add-apt-repository ppa:geany-dev/ppa
$sudo apt-get update
$sudo apt-get install geany
```

Those two commands install some plugins for Geany. The addions is 
a must-have for a function I will discuss later in the post. 

```
$sudo apt-get install geany-plugins-common
$sudo apt-get install geany-plugin-addons
$sudo apt-get install geany-plugin-spellcheck
```

Here are my preferred settings for Geany after the installation. This is under 
menu item `Edit → Preferences`. 

* Editor → Features → Line breaking column : 80
* Editor → Indentation → Type: Spaces
* Editor → Display → Display: Long line marker : 80 

The menu item `Tools → Plugin Manager` has access to Plugins dialog, turn on 
Addons, File Browser, HTML Characters, and Spell Check options. Click menu item `Edit → 
Plugin Preference` and toggle on option *Mark all occurrences of a word when 
double-clicking it*. Windows text editor Notepad++ has this nice feature. 
Geany editor also has it, but it takes a little time to configure and turn on 
the feature. 

<div style="max-width:800px">
  <img class="img-fluid pb-3" src="/images/geany-screenshot.png" alt="Geany Editor"> 
</div>

