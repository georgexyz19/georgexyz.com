title: Python Dictionary Methods
slug: dict-methods
meta: A post about python dict methods.
date: 2020-04-06 09:40
modified: 2020-04-06 09:40
tags: python
note: A short post about python dict methods
no: 35

Some Python code I read yesterday uses dictionary methods `copy` and `update`. 
This prompted me to test those two methods and check all other python dictionary methods. 

Here is the code testing the two methods:

```python
>>> d = {'a': 1, 'b': 2, 'c':3}
>>> d
{'a': 1, 'b': 2, 'c': 3}
>>> d1 = d
>>> d['a']=0
>>> d1
{'a': 0, 'b': 2, 'c': 3}
>>> d2 = d.copy()
>>> d['a'] = 4
>>> d1
{'a': 4, 'b': 2, 'c': 3}
>>> d2
{'a': 0, 'b': 2, 'c': 3}
>>> d2.update({'a':4, 'e':5})
>>> d2
{'a': 4, 'b': 2, 'c': 3, 'e': 5}
>>> 
```

Python official documentation lists dictionary methods on the 
[Built-in Types](https://docs.python.org/3/library/stdtypes.html) 
page. The page has a seciton 
[Mapping Types - dict](https://docs.python.org/3/library/stdtypes.html#typesmapping)
which lists all dictionary methods. The notable class methods are `clear`, `copy`, 
`fromkeys`, `get`, `items`, `keys`, `pop`, `popitem`, `setdefault`, `update`, and 
`values`. 

I found some interesting online documentation when searching for the topic. 

* This blog post 
[Copy a Python Dict with Updates](https://www.ibisc.univ-evry.fr/~fpommereau/blog/2009-05-12-copy-a-python-dict-with-updates.html) 
has an example of `copy` and `update` methods.
* [This stackoverflow Q\&A](https://stackoverflow.com/questions/5551672/how-to-copy-a-dict-and-modify-it-in-one-line-of-code) 
discusses the same problem
* [This webpage](https://www.w3schools.com/python/python_ref_dictionary.asp) 
on W3schools.com has a list of python dictionary methods. 
* Realpython.com has an article 
[Dictionaries in Python](https://realpython.com/python-dicts/#restrictions-on-dictionary-values)
which discusses the dictionary with more details. 

The dictionary is so fundamental in Python and programmers should become familar with those methods. 









