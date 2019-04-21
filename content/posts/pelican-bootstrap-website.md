title: Create Static Website With Pelican And Bootstrap 
slug: pelican-boostrap-website
meta: An article about how this website was created. 
date: 2019-04-14 19:34
modified: 2019-04-14 19:34
tags: pelican, bootstrap
note: none


This website is created with Pelican and Bootstrap, both of which are open-source
software.  When I am learning Django web framework, I want to create a blog site to 
write down some notes. A blog site with 50-500 articles does not need full scale 
Django back-end. My original plan is to write some python scripts calling Django Template 
system and python Markdown package.  Then I find Pelican which includes
Jinja2 Template system, Markdown, and many other functions.  It does what 
I want to do and much more. 

### Pelican

Pelican is a static website generator written in Python. When a web server is running Django or Flask 
framework, the server creates an html page and sends it back to client 
as the response to a request. If a developer chooses a static site generator like 
Pelican, html pages are created during development.  When a web request comes
to a server, the serve fetches pre-generated static html page and sends it back. 
The response cycle is simpler and faster.  The drawback is that the website is static. 
It does not receive or collect input from a user. 

This [full stack python article](https://www.fullstackpython.com/blog/generating-static-websites-pelican-jinja2-markdown.html) 
is an excellent tutorial on Pelican. 
[The Pelican documentation](https://docs.getpelican.com/en/stable/) 
site is a good reference. The fast way to learn Pelican is to look at code of 
two included themes "simple" and "notmyidea".  To get started, you can 
write a few blog posts in markdown format and utilize the built-in theme 
"simple" to generate a site. 

The figure below roughly describes how pelican works. Pelican reads markdown files and 
theme files into memory and produces html pages.  The theme files work as templates for html output. 
Some theme files correspond to multiple outputs, while others only relate to 
one output file. 

<div style="max-width:800px">
  <img class="img-fluid" src="/images/pelican-bootstrap/img-pelican-work.svg" alt="How Pelican Work"> 
</div>

[The Pelican source code](https://github.com/getpelican/pelican/tree/4.0.1/pelican)
consists of 14 python files (version 4.0.1).  The source files has 5,670 lines of 
code. It is a good median size code base to study if you are looking for python 
project to work on. I have not read all pelican source code yet. 

```
# bash command to tally pelican source code lines
find . -maxdepth 1 -name '*.py' -exec wc -l '{}' +
```

### Bootstrap 4

There is an excellent 
[*pelican-bootstrap3*](https://github.com/getpelican/pelican-themes/tree/master/pelican-bootstrap3) 
theme in the pelican-themes repo.  The original author of the theme did a nice work
of including lots of bootstrap features into the theme. 

Bootstrap 4 has been released for a while, so I decide to use Bootstrap 4 and create a theme 
for this website. Whenever I am not sure about a certain pelican theme feature, 
I check the code of the "pelican-bootstrap3" and start from there. 

Another nice pelican theme is 
[*pelican-subtle*](https://github.com/pR0Ps/pelican-subtle). 
The Markdown code style on this website is copied from pelican-subtle. I also read the 
code of this theme to get a better understanding on how pelican and pelican theme work. 

I changed the Bootstrap 4 default colors on the 
[bootstrap.build webiste](https://bootstrap.build/). Another website has a 
[Bootstrap theme kit](https://hackerthemes.com/kit/) if you want to customize 
Bootstrap locally.

The theme of this website has the following color variables:
 
```Scss
// _variables.scss 
$blue: #990000;
$green: #720027;
$cyan: #ce4257;
$yellow: #ff9b54;
$pink: #4f000b;
$font-size-base: 1.1rem;
$h4-font-size: $font-size-base * 1.1;
$h5-font-size: $font-size-base * 1.0;
$h3-font-size: $font-size-base * 1.4;
$h2-font-size: $font-size-base * 1.6;
$h1-font-size: $font-size-base * 1.8;
$h6-font-size: $font-size-base;
$paragraph-margin-bottom: 1.1rem;
$print-page-size: letter;
```

The pelican-theme github repo collects many themes.  However, it seems to me that
few of them are of professional quality. The possible reason is that most 
themes are produced by hobbyists during spare time. 

The three images on the homepage are downloaded from 
[pexels.com](https://www.pexels.com/), 
which is a very nice website for free photos. The icons on the Projects page are from 
[pixabay.com](https://pixabay.com/), and are modified with Gimp. 
 
### Invoke Package

[Invoke package](http://docs.pyinvoke.org/en/1.2/getting-started.html)
"is a Python task execution tool and library". It is similar to GNU 
Make program, but the script tasks.py is written in Python.  The tasks.py 
file is an equivalent of Makefile for GNU Make. 

I usually install Invoke package along with pelican and Markdown packages in a
python virtual environment. 

```python
python -m venv ~/.venv/pelican
source ~/venv/pelican/bin/activate
pip install pelican Markdown invoke
```

The `pelican-quickstart` command will create a tasks.py file in the project directory. 
One nice feature of Invoke is that you can run multiple tasks in one command. The 
command below cleans the `output` directory, rebuilds the project, and serves the 
website at `http://localhost:8000` address. 

```bash
invoke clean build serve
```

### Future Blog Plan

My future plan for the blog is to write about one post per month.  That comes 
to about 12 posts per year.  My goal is to write at least 6 posts per year 
even I am busy at work.  Another goal is to keep the blog running for at 
least 10 years, so we will see if the site has 60 posts in the year 2029. 

This site does not track who is reading or visiting. It does not have 
Google Analytics or similar services to track users. 

