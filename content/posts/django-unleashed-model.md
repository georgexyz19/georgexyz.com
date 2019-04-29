title: Django Unleashed Book Model Diagram
slug: django-unleashed-model
meta: A diagram for Chap 3 of Django Unleashed book.
date: 2019-04-23 07:47
modified: 2019-04-29 13:37
tags: django
note: none
no: 11


Andrew Pinkham's 
[*Django Unleashed*](https://www.amazon.com/gp/product/0321985079/ref=ppx_od_dt_b_asin_title_s00?ie=UTF8&psc=1)
 is a very good Django book. It covers many aspects of Django Web Framework with an example project. It 
is not a book for complete beginners. A reader needs to know a little Python and Django basics to get started.

The Chapter 3 of the book is about Django Models, discussing the example project models. 
The project has 4 models, 3 many-to-many relations, and 1 many-to-one relation. The book does not 
include a diagram showing the models and relations. Here is the diagram I draw in Inkscape:

<div style="max-width:800px">
  <img class="img-fluid" src="/images/django-unleashed-models.svg" alt="django unleashed models"> 
</div>

Here is the link to the [PDF page](/files/django-unleashed-models.pdf) of the diagram.

The 
[django-extensions](https://django-extensions.readthedocs.io/) has a 
[grahp_models command](https://django-extensions.readthedocs.io/en/latest/graph_models.html) which 
generates similar model diagrams. 

The extension command depends on the graphviz package and pydot/pyparsing modules.  Install those 
dependencies in Ubuntu 18.04 with commands shown below. 

```
$sudo apt-get install graphviz
(env)$pip install pyparsing pydot
(env)$python manage.py graph_models blog organizer --pydot -o models.png
```

Add the GRAPH_MODELS dictionary to the project settings file. 

```python
GRAPH_MODELS = {
  'all_applications': False, 
  'group_models': True,
```

Here is the generated PNG file. 

<div style="max-width:800px">
  <img class="img-fluid" src="/images/django-unleashed-models.png" alt="django unleashed models"> 
</div>
