title: Python Doctest
slug: python-doctest
meta: A short note about python doctest. 
date: 2019-10-05 15:42
modified: 2019-10-05 15:42
tags: python
note: 23
 

Python doctest is easier to use than unittest and pytest. A developer writes the 
test cases in the documentation and doctest module verifies the results. There are 
examples in the *Fluent Python* book that use doctest, but I have not seen them 
used often. 

The Python Module of The Week web site has 
[a page on doctest](https://pymotw.com/3/doctest/).  It is a nice introduction on
how to use doctest. The doctest module is useful in some situations. 

Below is a python file which includes a single function. The function has a docstring
which also serves as doctest. 

```python
#!/usr/bin/env python

# nested_sum adds up elements from a list of lists of integers
#            file name: nested_sum.py

def nested_sum(t):
    """
    >>> t = [[1, 2], [3], [4, 5, 6]]
    >>> nested_sum(t)
    21
    """
    total = 0
    for ti in t:
        total += sum(ti)
    return total

```

Run the python file with the following command in bash. Note the `-m` option 
loads doctest module. The `-v` option represents verbose. Without the `-v` 
option, the command outputs nothing.


```bash
python -m doctest -v nested_sum.py 
```

Here is the doctest results:

```
Trying:
    t = [[1, 2], [3], [4, 5, 6]]
Expecting nothing
ok
Trying:
    nested_sum(t)
Expecting:
    21
ok
1 items had no tests:
    nested_sum
1 items passed all tests:
   2 tests in nested_sum.nested_sum
2 tests in 2 items.
2 passed and 0 failed.
Test passed.
```

