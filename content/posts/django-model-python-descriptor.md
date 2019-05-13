title: Python Descriptor and Django Model Field
slug: python-descriptor-django-model
meta: This post is about python descriptor and django model field
date: 2019-05-12 17:48
modified: 2019-05-12 17:48
tags: python, django
note: 110 111 112 and 114
no: 13


Django model fields are descriptors. The descriptor is a Python intermediate feature. 
It is almost impossible to understand the FileField and ImageField source code 
without understanding Python descriptor.  Marty Alchin's book *Pro Django* has 
a short section on descriptors (Page 31 to 33), but it is not detailed. 

### Descriptor Online Articles

After some google search, I found several articles on Python descriptors. 
The first article is Michael Driscoll's 
[Python 201: What are descriptors?](https://www.blog.pythonlibrary.org/2016/06/10/python-201-what-are-descriptors/), 
which is a good introduction. At bottom of the linked page, it has a reference 
to Ned Batchelder's blog site. I heard Ned Batchelder on 
[Talk Python To Me Podcase](https://talkpython.fm/) and read his excellent 
[article on Unicode](https://nedbatchelder.com/text/unipain.html). His blog post 
on descriptor is actually recommending a lightning talk and an article by Chris 
Beaumont. 

The article 
[Python Descriptors Demystified](https://nbviewer.jupyter.org/urls/gist.github.com/ChrisBeaumont/5758381/raw/descriptor_writeup.ipynb) 
by Chris Beaumont is possibly the best writing on descriptors.  Many descriptor techniques 
discussed in the article are used in Django Model source code. Here are the main points 
of the article:

* Descriptors are reusable properties
* Put descriptors at class level
* Keep instance level data instance specific
* Label your descriptor
* Label descriptors with Metaclasses

The article itself is not long, but it takes time to understand the techniques. The article 
also beriefly discussed property. I found a short article 
[Property Explained – How to Use and When](https://www.machinelearningplus.com/python/python-property/) 
which has nice Python property examples.

Python official documentation has an article 
[Descriptor HowTo Guide](https://docs.python.org/3/howto/descriptor.html) 
written by Raymond Hettinger. This article is not easy, it takes time to digest the content. 

Here is the 
[link to my Github repo](https://github.com/georgexyz19/PythonDescriptor) 
which consists of code examples in those articles. 


### Django Model Code

This section is trying to answer the question "how does the class variable 'name' 
become an instance variable"? The source code and line number reference below are from Django 
[version 2.1](https://github.com/django/django/tree/2.1). 

```python
class Book(models.Model):
    name = models.CharField(max_length=255)
    ...
    
b = Book.objects.get(pk = ... )
bn = b.name

```

The two lines of code below are from base.py ModelBase class (L138-139), which is
a Metaclass for Model.
  
```python
for obj_name, obj in attrs.items():
    new_class.add_to_class(obj_name, obj)
```

The attrs is the fourth argument to the `__new__` method in meta class ModelBase. 
The obj_name refers to 'name' and obj refers to `'models.CharField(max_length=255)'` 
where name is a field in Book model class. 

```python
def __new__(cls, name, bases, attrs, **kwargs):
```

The `add_to_class` method is defined on L301.  The method checks to see if the 
value being added has `contribute_to_class` method, and if it does it will call 
this method. Otherwise, the method calls `setattr` to set (name, value) pair 
as class attribute.  The `getattr` and `setattr` are python built-in functions. 

```python
def add_to_class(cls, name, value):
    # We should call the contribute_to_class method only if it's bound
    if not inspect.isclass(value) and hasattr(value, 'contribute_to_class'):
        value.contribute_to_class(cls, name)
    else:
        setattr(cls, name, value)
```

The `contribute_to_class` method is defined in `db/models/fields/__init__.py` L727. 
It is a method in Field class. 
This is where the actual magic happens.  The self, cls, and name in `contribute_to_class` 
are models.CharField(max_length=255), Book, and 'name', respectively. 

The first thing `contribute_to_class` does is it takes the value assigned to the 
class variable and stores it in class attribute \_meta, which is an Options object. 

The second thing it does is to assign an instance of a DeferredAttribute class 
to this field.  The class is a Descriptor in python. The construction of 
`DeferredAttribute` has an argument `self.attname`, which has the same name of 
the field.  It can be shown that for fields the `getattr(cls, self.attname, None)` 
function returns None.  The comments indicate that this line is intended for the class method. 

```python
def contribute_to_class(self, cls, name, private_only=False):
    """
    Register the field with the model class it belongs to.
    If private_only is True, create a separate instance of this field
    for every subclass of cls, even if cls is not an abstract model.
    """
    self.set_attributes_from_name(name)
    self.model = cls
    if private_only:
        cls._meta.add_field(self, private=True)
    else:
        cls._meta.add_field(self)
    if self.column:
        # Don't override classmethods with the descriptor. This means that
        # if you have a classmethod and a field with the same name, then
        # such fields can't be deferred (we don't have a check for this).
        if not getattr(cls, self.attname, None):
            setattr(cls, self.attname, DeferredAttribute(self.attname))
    if self.choices:
        setattr(cls, 'get_%s_display' % self.name,
                partialmethod(cls._get_FIELD_display, field=self))
```

The `DeferredAttribute` descriptor class is defined in db.models.query_utils.py 
file L116.  The code for the class is not long, and they are shown below. 
The instance and cls in `__get__` method will be a book instance and cls will 
be Book class. The code in `__get__` method shows the subtle differences 
between `__dict__` attribute and `getattr` (search tree). 

```python
class DeferredAttribute:
    """
    A wrapper for a deferred-loading field. When the value is read from this
    object the first time, the query is executed.
    """
    def __init__(self, field_name):
        self.field_name = field_name

    def __get__(self, instance, cls=None):
        """
        Retrieve and caches the value from the datastore on the first lookup.
        Return the cached value.
        """
        if instance is None:
            return self
        data = instance.__dict__
        if data.get(self.field_name, self) is self:
            # Let's see if the field is part of the parent chain. If so we
            # might be able to reuse the already loaded value. Refs #18343.
            val = self._check_parent_chain(instance, self.field_name)
            if val is None:
                instance.refresh_from_db(fields=[self.field_name])
                val = getattr(instance, self.field_name)
            data[self.field_name] = val
        return data[self.field_name]

    def _check_parent_chain(self, instance, name):
        """
        Check if the field value can be fetched from a parent field already
        loaded in the instance. This can be done if the to-be fetched
        field is a primary key field.
        """
        opts = instance._meta
        f = opts.get_field(name)
        link_field = opts.get_ancestor_link(f.model)
        if f.primary_key and f != link_field:
            return getattr(instance, link_field.attname)
        return None
```
