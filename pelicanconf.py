#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'George Zhang'
SITENAME = 'George Zhang'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# four directories under contents: images, files, posts, pages
STATIC_PATHS = ['images', 'files', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME' : {'path': 'CNAME' }}

THEME = "bs4"

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': 
           {"css_class": "highlight", "guess_lang": False, "linenums": False},
        'markdown.extensions.extra': {},
        'markdown.extensions.admonition': {},
    },
    'output_format': 'html5',
}

# not using category
CATEGORY_SAVE_AS = ''
CATEGORIES_SAVE_AS = ''

# not using author
AUTHORS_URL = ''
AUTHORS_SAVE_AS = ''
AUTHOR_URL = ''
AUTHOR_SAVE_AS = ''

DEFAULT_PAGINATION = 3
INDEX_SAVE_AS = 'article-list.html'
SUMMARY_MAX_LENGTH = 30


