title: Python Program to Create New Pelican Post
slug: create-new-pelican-post
date: 2020-05-02 15:47
modified: 2020-05-02 15:47
tags: pelican, python
note: A post about how to create new Pelican post.
related_posts: pelican-related-posts-translation
no: 41

Pelican static site generator comes with a nice command `pelican-quickstart`. It 
generates a starter project which includes `pelicanconf.py`, `publishconf.py`, 
`tasks.py`, and other files and directories.  The source code is in the 
`pelican_quickstart.py` file under the tools directory. The code is a nice 
example on how to create similar programs. 

It is not difficult to write a program which generates a new Pelican starter
post. The benefit of the program is that it can automatically fill some meta fields.  
It can also present a list of tags that already used in other posts, and the user 
can pick one of more tags from the list. In addition, each post will have consistent meta fields. I write the 
[`newpost.py` python program](https://github.com/georgexyz19/georgexyz.com/blob/master/newpost.py) 
for this purpose.  

Here is how to run the program. 

```
(georgexyz.com) george@desktop:~/Desktop/georgexyz.com$ python newpost.py 
Welcome to pelican-post v4.2.0.

This script will help you create a new pelican post.

Please answer the following questions so this script can generate the post.
    
> Where do you want to save the markdown file? [content/posts] 
> What will be the title of this post? [NEW TITLE] Python Program 
        to Create New Pelican Post
> What will be the slug of this post? [python-program-to-create-new-pelican-post]
        create-new-pelican-post
> What will be the date/time of the post? [2020-05-02 15:47] 
```

The `newpost.py` program calls Pelican itself to read all existing posts and 
presents the tags on a list.  Before using the program, I usually open the 
["Tags" page](https://georgexyz.com/tags.html) of my blog website to pick one 
or more tags for the new post. The program can also generate a `related_posts` 
meta field if a user chooses to do so.  Feel free to copy and modify the program 
for your own site.

```
> Tags already used in other posts (choose one or more): 
    1 -> WSGI
    2 -> bash
    3 -> books
    4 -> bootstrap
    5 -> django
    6 -> flask
    7 -> inkscape
    8 -> javascript
    9 -> linux
    10 -> linux mint
    11 -> pelican
    12 -> python
    13 -> software utility
    14 -> traffic engineering
    15 -> ubuntu
    16 -> vim
    17 -> web development
> Choose one or more tags (e.g. 1, 4) 0 to enter new tag(s) [0] 11, 12
> Do you want to add related posts? (y/N) y
> Posts with same tags (choose one or more) 
    1 -> Pelican Related Posts and&nbsp;Translation
    2 -> Print Python Source Code on&nbsp;Paper
    3 -> Pelican Source Code and&nbsp;Plugin
    ......
> Choose one or more articles (e.g. 1, 3) 0 to cancel [0] 1
> Add a number for the post (start from 1) [41] 
> Add a short note to yourself for this post? [note to be added] A post about 
        how to create new Pelican post.
> Write the first sentence of the article [This is the first sentence ...] 
Done. Your new post is available at content/posts
(georgexyz.com) george@desktop:~/Desktop/desktop/georgexyz.com$ 
```
