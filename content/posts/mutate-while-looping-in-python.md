title: Mutate While Looping in Python
slug: mutate-while-looping-in-python
date: 2020-07-21 00:47
modified: 2020-07-21 00:47
tags: python
note: some python code
no: 51

Raymond Hettinger once said "if you mutate something while you're iterating over it, 
you're living in a state of sin and deserve whatever happens to you". Recent version 
of Python actually does not allow you mutate a dictionary while looping over it. Here are  
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
an example (modified) from 
[Chapter 6](https://automatetheboringstuff.com/2e/chapter6/) 
of Al Sweigart's *Automate The Boring Stuff With Python* book.

```python
def prefix(word):
    prefixnonletters = ''
    while len(word) > 0 and not word[0].isalpha():
        prefixnonletters += word[0]
        word = word[1:]
    return prefixnonletters, word
```

This function separates a word (e.g., '123word') into two parts: the prefix non-letter 
part ('123') and following letter part ('word'). The code loops over the input word and mutates it 
in the loop body. It is difficult to write the function in other ways. One alternative 
way I can think of is to use regular expression. 

```python
def prefix_re(word):
    import re
    m = re.match(r'([^A-Za-z]+)(\w*)', word)
    if m:
        return m.group(2), m.group(2)
    else:
        return '', word
```
