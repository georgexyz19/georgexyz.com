title: Tipue Search for Pelican Web Site
slug: tipue-search-pelican
date: 2020-05-04 22:10
modified: 2020-05-04 22:10
tags: javascript, pelican, web development
note: Shows how to add tipue search for this personal site
no: 42

Pelican has a very nice [documentation site](https://docs.getpelican.com/en/stable/). 
However Pelican itself is not the tool that 
generates the site, instead it is created with the Sphinx python documentation tool. 
The site has a nice search function. I wonder how to add such a search feature 
to a static site.

A little online research reveals that Pelican plugin github repo has a 
[tipue-search](https://github.com/getpelican/pelican-plugins/tree/master/tipue_search) 
plugin. The Tipue Search tool itself has [a nice website](https://tipue.com/search/) 
and documentation. I spend a few hours reading the documentation and try to figure out 
how this tool works. 

The tipue-search Pelican plugin creates a js file `tipuesearch_content.js` which 
defines a js variable `tipuesearch`. The variable is assigned a large js object 
containing all search data. The plugin uses BeautifulSoup to parse html 
title and content of posts and pages generated in Pelican.  The size of the file `tipuesearch_content.js` 
obviously depends on the number of pages on a website.  The 41 posts on this 
site result in a 144 KB js file.  

The Tipue Search tool is mainly a js program.  The web page will download the 
`tipuesearch_content.js` file first, and Tipue Search tool will search the data 
and present the results on the page. The package also includes a nice CSS 
file which formats the search box and search results. Below are the steps on 
how to setup the tool for a blog site like this one. 

- Install BeautifulSoup in python virtual environment. Copy tipue_search directory (
   include three files `__init__.py`, `README.rst`, and `tipue_search.py`)
   to the plugin subdirectory under project directory. 
- Revise one line and add one additional line of code in `pelicanconf.py`. Pelican
  will load the plugin and generate the `tipuesearch_content.js` file in output 
  directory. 

<div class="ml-5">
```
PLUGIN_PATHS = ['plugin/', ]
PLUGINS=['related_posts', 'tipue_search']
DIRECT_TEMPLATES = ['index', 'tags', 'categories', 
    'authors', 'archives', 'search']
```
</div>

- Add a `search.html` file to the theme templates directory 
([see file on github repo](https://github.com/georgexyz19/georgexyz.com/blob/master/bs4/templates/search.html)).
The contents
   of this file is very similar to the demo page of Tipue Search. I also adjusted 
   a few lines of code in `base.html` to fit the needs of this new `search.html` file. 
   Pelican will automatically generate a corresponding `search.html` in output directory. 
- Copy Tipue Search tool directory `tipuesearch` (including 4 js files and 1 css file) to theme static directory. Pelican will automatically copy them to `theme/tipuesearch` under output
directory during site generation. 
- Add a link on the Articles page and Tags page which will open the `search.html` page. 

If you want to try out the Tipue Search tool, click the [link here](/search.html). 

After adding the tipue search to this blog site, I find the search function is really 
convenient even for a small blog site like this. I use it all the time to find 
articles I write before. Every web site should provide some kind of search 
function for users. 
 
 

<div class="mt-5 border-top">
  <h3>Related:</h3>
  <ul>
    <li><a href="/search.html">Search Tool</a></li>
  </ul>
</div>




