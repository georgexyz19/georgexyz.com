title: Simple Pelican Project Structure
slug: simple-pelican-project-structure
date: 2022-03-16 10:28
modified: 2022-03-16 10:28
tags: pelican, python
note: note to be added
no: 85

Pelican project structure can be complicated for a beginner.  A simple project structure 
makes it easy to create simple websites. Once you understand the sub directories in the 
`output` dir, you can use `/` to reference the website root and it makes 
easier to reference other images files or static files. 

The image below shows a simple Pelican project structure I used for one website. 

<div style="max-width:800px">
  <img class="img-fluid pb-3" src="/images/simple_pelican_project.png" alt="pelican project dir"> 
</div>

Here are the details of the project structure. 

1. The `files` dir in `content` becomes `files` dir in `output`. 
2. The `images` dir is copied to `output`. It is the same as `files` dir. 
3. The html files in `pages` dir map to the same files in `output`.  This is not the default Pelican 
behavior, and it requires a setting in the `pelicanconf.py` file. 
4. The markdown files (.md) in `posts` dir map to files in `output`. 
5. Pelican creates a `theme` dir in `output`.  It maps to `theme` dir under project dir. 
6. The `static` dir under `theme` disappears.  <span style="color:red;">This Pelican design choice is strange.</span> 
7. The directories in `static` dir are copied to be under `theme` dir in `output`. 
8. The `templates` dir disappears.  The contents of the files become part of html file in `output`. 

Below is the contents of the `pelicanconf.py` file with some default settings removed. 

```
#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'FistName LastName'
SITENAME = 'www.example.com'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

STATIC_PATHS = ['images', 'files']
# refer to files like this `/files/calendar/2019.svg`
# images with src = `/images/homepage.png`

THEME = "theme"

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': 
           {"css_class": "highlight", "guess_lang": False, 
            "linenums": False},
        'markdown.extensions.extra': {},
        'markdown.extensions.admonition': {},
    },
    'output_format': 'html5',
}

# not using category
CATEGORY_SAVE_AS = ''
CATEGORIES_SAVE_AS = ''

ARCHIVES_SAVE_AS = ''

# not using author
AUTHORS_URL = ''
AUTHORS_SAVE_AS = ''
AUTHOR_URL = ''

# not using tags
TAG_SAVE_AS = ''
TAGS_SAVE_AS = ''
TAG_URL = ''

# DEFAULT_PAGINATION = 3
INDEX_SAVE_AS = ''
# SUMMARY_MAX_LENGTH = 30

TYPOGRIFY = True

# change from `/output/pages/{slug}.html` 
#  to /output/{slug}.html
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'

```