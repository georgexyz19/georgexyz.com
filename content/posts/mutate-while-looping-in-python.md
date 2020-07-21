title: Mutate While Looping in Python
slug: mutate-while-looping-in-python
date: 2020-07-21 00:47
modified: 2020-07-21 00:47
tags: python
note: some python code
no: 51

Raymond Hettinger once said "if you mutate something while you're iterating over it, 
you're living in a state of sin and deserve what ever happens to you". Recent version 
of Python actually does not allow you change a dictionary while looping over it. Here is 
some test code. 

```python
Python 3.7.4 (default, Sep 20 2019, 00:15:38) 
[GCC 7.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> d = {'matthew': 'blue', 'rachel': 'green', 'raymond': 'red'}
>>> d
{'matthew': 'blue', 'rachel': 'green', 'raymond': 'red'}
>>> for k in d:
...   print (k)
... 

>>> d2 = d.copy()
>>> for k in d.keys():
...   if k.startswith('r'):
...     del d[k]
... 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
RuntimeError: dictionary changed size during iteration

```

Sometimes "mutate while looping" is necessary and it can make code simpler. Here is 
an example from Al Sweigart's *Automate The Boring Stuff With Python* book.

To be continued...
