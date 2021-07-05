title: Python Counting With Dictionary
slug: python-count-with-dict
meta: Short discussion on a small python task
date: 2020-03-02 02:20
modified: 2020-03-02 02:20
tags: python
note: 29
 

When I am reading a realpython article 
[Working With JSON Data in Python](https://realpython.com/python-json/), I find 
an interesting python technique that reminds me something else I read before. 
It is called *Counting With Dictionary* by Raymond Hettinger in a python talk.
[A previous blog post]({filename}good-python-learning-resources.md) has the links 
to the video and the note. 

Given a list such as colors below,
```python
colors = ['red', 'green', 'red', 'blue', 'green', 'red']
```
the python code should generate a dictionary. The keys of the dictionary are 
values in the list, and the values of the dictionary are the corresponding number of 
keys in the list.  For the above example, the result dictionary `d` is 
```python
{'red': 3, 'green': 2, 'blue': 1}
```
There are many ways to write the code.  I will summarize these techniques below. 

### Basic Way to Count

The basic way is to set the d[color] to 0 when the dictionary sees the color 
first time.  Total line count is 5. 

```python
d = {}
for color in colors:
    if color not in d:
        d[color] = 0
    d[color] += 1
```

You can make slight changes to the code above, but the logic is the same. It will 
have one more line. 

```python
d = {}
for color in colors:
    if color not in d:
        d[color] = 1
    else:
        d[color] += 1
```


### Get Method of Dictionary
If the color is not in the dictionary, using `d[color]` to access its value raises
a KeyValue exception.  The dictionary `get` method returns the second argument 
when the first argument is not already in the dictionary.  Line count is 3. 

```python
d = {}
for color in colors:
    d[color] = d.get(color, 0) + 1
```
    
### Use Defaultdict 
The standard collections package has a defaultdict class. The class sets a default 
value for a key.  Line count is still 5. 

```python
from collections import defaultdict
d = defaultdict(int)
for color in colors:
    d[color] += 1
d = dict(d)
```

### Try and Except to Handle Exception
The above three methods are from Raymond Hettinger's python talk.  The method below
is from the *Real Python* article I introduced earlier.  This method takes 6 lines, 
but the logic is very clear. 

```python
d ={}
for color in colors:
    try:
        d[color] += 1
    except KeyError:
        d[color] = 1
```
        
### Setdefault Method of Dictionary
This method is between the first two methods.  Line count is also between 5 and 3. 
This method uses dictionary method `setdefault`, which is also discussed in 
Raymond Hettinger's python talk.

```python
d={}
for color in colors:
    d.setdefault(color, 0)
    d[color] +=1 
```

Python is very flexible to write once you know the basics, and there are always 
many ways to solve a problem. 

### Counter Class in collections Module

When I am browsing `collections` module 
[documentation on python.org](https://docs.python.org/3.8/library/collections.html), 
I find a `Counter` class which is "a counter tool provided to support convenient 
and rapid tallies". 

```python
from collections import Counter
cnt = Counter(colors)
d = dict(cnt)
```

This method is probably the easiest and the line count is only 3. 
