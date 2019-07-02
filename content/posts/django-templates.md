title: A Close Look at Django Template System
slug: django-templates
meta: This post records the notes when I am study django templates system.
date: 2019-07-02 13:40
modified: 2019-07-02 13:40 
tags: django
note: this note is based on several previous notes. 
no: 15


Django has a built-in template system. It is relatively easy to understand, and 
the source code is not as complicated as other parts of Django. This article is 
a summary of the notes I took  when studying the system. 

### Official Documentation

The online Django documentation has 5 pages dedicated to template. 

* Intro to template ([link](https://docs.djangoproject.com/en/2.2/topics/templates/))
* Template language reference ([link](https://docs.djangoproject.com/en/2.2/ref/templates/language/)) 
* Built-in tags and filters ([link](https://docs.djangoproject.com/en/2.2/ref/templates/builtins/)) 
* How to use template system ([link](https://docs.djangoproject.com/en/2.2/ref/templates/api/))
* Custom tags and filters ([link](https://docs.djangoproject.com/en/2.2/howto/custom-template-tags/))

A Django application developer probably does not need to know all of those details. 
But it is always a good thing for programmers to know how things work behind the scene. 
 

### Template Language Summary

Django Template Language (DTL) syntax mainly consists of three elements: variable, 
tag, and filter. Here are some examples:

**variable**

```
{{ variable }}
{{ tag.name }}
```

**tag**

```
{% expression %}
{% for startup in tag.startup_set.all %}
  ...
{% endfor %}

{% extends "base.html" %}
{% block title %}
  {{ block.super }} - Tag List
{% endblock title %}

{% if/else/endif %}
{% if not tag.startup_set all and not tag.blog_posts.all %}
```

**filter**

```
{{ startup_date|date:"F jS, Y" }}  ▶ July 2nd, 2019
{{ startup.website|urlize }}
{{ startup.description|linebreaks }}
```
*other filters*:  title, pluralize, truncatewords:20, default:"base.html"


### How to Load Templates

#### Method 1

The django.template.loader module defines `get_template` and `select_template` 
functions. Both functions can load template files and render them agaist a dict. 
The difference is that `get_template` accepts a template name and 
`select_template` accepts a list of template names. Here is an example from 
Django official tutorial. 

```python
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))
```

#### Method 2

The more common code is to use the `render` function defined in django.shortcuts 
module in views.  

```python
from django.shortcuts import render
...
return render(request, 'template_name.html', {'tag': tag})
```

The `render` function itself (Django2.2.2 source code) is very simple and short. 
It calls `render_to_string` function in django.template.loader module, which in 
turn calls `get_template` or `select_template` depending on template_name. 

```python
# in django.shortcuts
def render(request, template_name, context=None, content_type=None, 
           status=None, using=None):
    """
    Return a HttpResponse whose content is filled with the result of calling
    django.template.loader.render_to_string() with the passed arguments.
    """
    content = loader.render_to_string(template_name, context, request, 
                                      using=using)
    return HttpResponse(content, content_type, status)

# in django.template.loader 
def render_to_string(template_name, context=None, request=None, using=None):
    """
    Load a template and render it with a context. Return a string.
    template_name may be a string or a list of strings.
    """
    if isinstance(template_name, (list, tuple)):
        template = select_template(template_name, using=using)
    else:
        template = get_template(template_name, using=using)
    return template.render(context, request)

```

#### Method 3

The django.template module has two classes Template and Context. Those 
are template system's lower level APIs. Here is an example:

```
from django.template import Template, Context
template = Template('Hi, my name is {{ name }}.')
context = Context({'name': 'Andrew'})
template.render(context)
#  result is 'Hi, my name is Andrew.'

```

### Template System Source Code

The source code for Django template system is in django/template directory, and 
consists of 26 python files. 

Bash command `wc` outputs number of lines in a file. We know that total number 
of lines of Django template system code is 5,863 (Django 2.2.2). The output 
below also shows that two files `base.py` and `defaulttags.py` have over 1,000 
lines of code each. 

```
george@STK2M3:~/django-2.2.2/django/template$ wc -l *.py
  1044 base.py
    81 context_processors.py
   280 context.py
   907 defaultfilters.py
  1474 defaulttags.py
   180 engine.py
    42 exceptions.py
    68 __init__.py
   328 library.py
    66 loader.py
   317 loader_tags.py
   145 response.py
   208 smartif.py
   107 utils.py
  5247 total
george@STK2M3:~/django-2.2.2/django/template$ wc -l loaders/*.py
  14 loaders/app_directories.py
  49 loaders/base.py
  95 loaders/cached.py
  46 loaders/filesystem.py
   0 loaders/__init__.py
  27 loaders/locmem.py
 231 total
george@STK2M3:~/django-2.2.2/django/template$ wc -l backends/*.py
   81 backends/base.py
  129 backends/django.py
   53 backends/dummy.py
    0 backends/__init__.py
  108 backends/jinja2.py
   14 backends/utils.py
  385 total

```



