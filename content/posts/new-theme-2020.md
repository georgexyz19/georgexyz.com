title: New Pelican Theme
slug: new-theme-2020
meta: Describes how to revise the pelican theme
date: 2020-04-11 22:31
modified: 2020-04-11 22:31
tags: web development, pelican
note: Describe how the revise the theme for this site.
no: 36

This site has been online for more than one year.  It is time to revise the pelican 
theme to present a new look.  I spend a few hours revising the code, and now 
it is easier for myself to publish or revise articles. 

The Bootstrap theme css file is now compiled on my computer.  It is not too difficult to 
compile Bootstrap scss to css. This 17 minute long youtube video explains it very well. 

[Bootstrap 4 Theme Customization with Sass](https://youtu.be/6Ovw43Dkp44)

I install Node version of Sass and Minify in Linux Mint with these commands. The Minify 
tool removes extra blanks and line breaks in the css, and it also works for js and html files. 

```
$sudo npm install -g sass
$sudo npm install -g minify

#compile sass to css
$sass main.scss main.css
$minify main.css > main.min.css
```

The main.scss for the new theme has those contents. 

```
$font-size-base: 1.1rem;
$h5-font-size: $font-size-base * 1.0;
$h4-font-size: $font-size-base * 1.1;
$h3-font-size: $font-size-base * 1.4;
$h2-font-size: $font-size-base * 1.6;
$h1-font-size: $font-size-base * 1.8;

$paragraph-margin-bottom: 1.2rem;
$headings-margin-bottom:  1.0rem;

$body-color: #111;
$headings-color: #333;
$link-color: #0017c7;
$code-color: #15228a;
$code-font-size: 88%;

$print-page-size: letter;

@import "node_modules/bootstrap/scss/bootstrap";

```

The light blue color of the navbar is set in the `base.html` file, which is copied from
Bootstrap documentation. 

```
<nav class="navbar navbar-expand-md navbar-light" style="background-color: #e3f2fd;">
```

The `pelicanconf.py` file also has a few changes.  I remove default index.html page and 
change the previous about page to new homepage.  The Python `Typogrify` package makes 
"double quotes" and other html elements look better. 

```python
# DEFAULT_PAGINATION = 3
INDEX_SAVE_AS = ''
SUMMARY_MAX_LENGTH = 30

# link to this file in base.html
# work computer blocks archives.html web page
ARCHIVES_SAVE_AS = 'articlelist.html'
TYPOGRIFY = True
```

The `tasks.py` file created by the pelican-quickstart command has a `livereload` task, which 
requires installing a Python package with the same name `livereload`.  The live reload function
is really nice.  This is something you do not think you need before trying it, but after trying 
it you fall love with it.  The default setting only watches for markdown and RST 
file types, you can add html to the list of files to watch. 

I also change the github repo to SSH connection instead of HTTPS connection and add a public
SSH key to the github account, so I do not need to type password when I update the github 
repo.  This stackoverflow Q/A shows how to do it. 

[How to Push to Github with SSH Key](https://stackoverflow.com/questions/14762034/push-to-github-without-password-using-ssh-key)

To end this post, below is a screen shot of this site with old theme.

<div style="max-width:800px">
  <img class="img-fluid pb-3" src="/images/homepage2019.png" alt="Old theme"> 
</div>
