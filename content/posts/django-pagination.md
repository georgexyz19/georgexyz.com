title: Django Pagination
slug: django-pagination
meta: This post discusses django pagination
date: 2019-07-17 10:05
modified: 2020-04-30 12:58
tags: django
note: this note is based on a previous hard copy note 3/4/19
no: 19

Merriam-Webster dictionary defines pagination as "the action of paging". In web 
design world, pagination means separating a large list of contents onto 
different pages for easy web navigation.   

Django provides a few classes that help you manage pagination.  The official documentation has 
[one page on Pagination](https://docs.djangoproject.com/en/2.2/topics/pagination/).
The source code is in one file django/core/paginator.py, which has 195 lines 
(version 2.2.2). The Paginator and Page classes defined in this file are very 
good python class examples. 

The Paginator class has those public methods:

* validate\_number
* get_page : calls page method, handles exception
* page : page number is 1-based
* count : cached_property
* num\_pages
* page\_range

The Page class is derived from collections.abc.Sequence, and it has those 
public methods:

* has\_next
* has\_previous
* has\_other\_pages
* next\_page\_number
* previous\_page\_number
* start\_index
* end\_index

The Page class also defines `__len__` and `__getitem__` methods, and it has 
three attributes: object\_list, number, and paginator.

Chapter 14 of *Django Unleashed* book covers how to use the django pagination 
in detail. An online article 
[How to Paginate with Django](https://simpleisbetterthancomplex.com/tutorial/2016/08/03/how-to-paginate-with-django.html) 
is also a nice summary on how to use paginator.  In class based views, all 
it takes is to add one line of code to use Django paginator.

```python
paginate_by = 10
```

The template will be rendered with a context object with those contents:

```
context = {
            'paginator': paginator,
            'page_obj': page,
            'is_paginated': is_paginated,
            'object_list': queryset
        }
```

The context object is defined in the `get_context_data` method of MultipleObjectMixin. The 
`queryset` value of `context` dictionary is returned by `paginate_queryset` method, and it is 
`page.object_list`.  You can easliy navigate the source code on this 
[Class CBV website](https://ccbv.co.uk/projects/Django/2.2/django.views.generic.list/ListView/). 


