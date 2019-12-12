title: HTML, CSS, and Others
slug: html-css-others
meta: Updates on what I am working on 
date: 2019-11-25 13:07
modified: 2019-11-25 13:07
tags: web development
note: 25

This post is an update on what I am working on. 

#### CSS Books

I recently re-read the online book [HTML/CSS Is Hard](https://internetingishard.com/) which 
is an excellent resource to learn CSS.  Jon Duckett’s *Web Design with HTML and CSS* 
book is a good introductory book, but it does not cover advanced CSS features.  This 
online book covers these topics very well. The illustrations in the book are wonderful.

I also read another CSS book *CSS In Depth* by Keith Grant which is also an excellent 
book.  The basic rules of CSS are straightforward, but it is not easy to layout 
a nice webpage for both mobile devices and desktops.  This book discusses many 
advanced topics in CSS.

#### Wget to Download Website

I searched and found an online article Q/A post 
“[How can I download an entire website](https://superuser.com/questions/14403/how-can-i-download-an-entire-website)”. The post has an answer which shows how to download a website to local hard drive
with Linux command line tool wget.  The command is shown below:

```
wget -m -p -E -k www.excample.com
```

* -m : --mirror recursion and time stamping
* -p : all images
* -E : adjust extension
* -k : convert links for local file

I tested the command on internetingishard.com and it worked well. 

#### VS Code

Vim has been my main text editor for some time.  But it is not ideal for 
coding HTML/CSS webpages.  VS code installed in Linux Mint works very well. 
It also has Emmet auto completion built in. It makes coding HTML/CSS 
much easier and faster. Youtube has [a nice tutorial on how to use Emmet](https://youtu.be/5BIAdWNcr8Y). 

The other nice feature of VS Code is that it is easy to install plugins. 
I installed Live Server Addon plugin with a few mouse clicks.  It takes efforts
to make plugins work in vim. 

#### Inkscape 1.0 Beta Testing 

Inkscape 1.0 Beta is out.  I test it out in Windows and it crashes often. 
It is not ready for production work yet.  The built in Python system has been 
upgraded to 3.7, which is long overdue.  One plugin I wrote (Draw Sign Arrow) for 
Inkscape 0.9.2 works fine in Inkscape 1.0 beta without any changes. 

I plan to upgrade all my Inkscape python programs to 3.7 in near future. 

