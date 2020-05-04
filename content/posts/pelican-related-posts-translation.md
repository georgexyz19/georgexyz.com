title: Pelican Related Posts and Translation
slug: pelican-related-posts-translation
meta: Describes how to use related posts and translation
date: 2020-04-28 12:02
modified: 2020-04-28 12:02
tags: web development, pelican
note: Describe pelican related posts and translation.
related_posts: print-source-code-paper, pelican-source-code-plugin, new-theme-2020, pelican-boostrap-website
no: 40

The Pelican source code has a related_posts attribute defined in the `Generator` class. The variable 
is initialized as a blank list and is not used in the program. I do a Google search and find 
a plugin called `related_posts` in the pelican plugin repo. The `related_posts` plugin has a 
[one page documentation](https://github.com/getpelican/pelican-plugins/tree/master/related_posts).

### Related Posts Plugin

Related posts could be a useful function for a blog site like this.  When I start a new blog post, 
it is often related to a previous post.  It's logical to add links to previous related posts 
either on a sidebar or at the bottom of the new article. Here are the steps to setup the plugin. 

- Create a sub-directory `plugin` in the project directory. Copy the `related_posts` directory
  to the `plugin`. It includes three files `__init__.py`, `related_posts.py`, and `Readme.rst`. 
- In this site, posts with same tags should not be counted as related posts, so I comment out 
  the lines 37 to 53 in the `related_posts.py` file. 
- Add the following settings to `pelicanconf.py`. 

<div class="ml-5">
```
PLUGIN_PATHS = ['plugin/', ]
PLUGINS=['related_posts',]
```
</div>

- Add the following html snippet to the `article.html` template file after statement `{{ article.content }}`. 

<div class="ml-5">
```
{% if article.related_posts %}
<div class="mt-5 border-top">
  <h3>Related Posts:</h3>
  <ul>
    {% for related_post in article.related_posts %}
    <li><a href="{{ SITEURL }}/{{ related_post.url }}">
      {{ related_post.title }}</a></li>
    {% endfor %}
  </ul>
</div>
{% endif %}
```
</div>

- Add a meta field to the post. The contents of the field are slugs of previous posts. 

<div class="ml-5">
```
related_posts: print-source-code-paper, pelican-source-code-plugin, ...
```
</div>

After those steps, each article will have a section "Related Posts" like on this page 
if the post includes a meta field `related_posts`. 

### Translation

This site does not have any translated articles. But I find it is not difficult to 
translate articles to other languages with Pelican after reading the source code. 

You can set a meta field such as `lang: es` for a translated article.  The article should 
have the same slug as the original one. Then, you can add the following html snippet on 
the `artilce.html` template. The page will have a link to the translated 
article in another language. 

```
{% if article.translations %}
  <hr>
  {% for art in article.translations %}
      <p><a href="{{ art.url }}">{{ art.title }}</a> in language
      {% if art.lang == 'en' %} 
          English
      {% elif art.lang == 'es' %}
          Spanish
      {% endif %} 
      </p>
  {% endfor %}
{% endif %}
```



