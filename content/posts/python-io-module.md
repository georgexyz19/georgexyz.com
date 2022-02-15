title: Python IO Module
slug: python-io-module
date: 2022-02-07 09:50
modified: 2022-02-07 09:50
tags: python
note: note to be added
no: 81

The previous three modules logging, unittest, and http all import a low level module io and use 
classes in the io module. So 
I decide to take a close look at the io module. Unfortunately there aren't many documents 
available for the module. 

The standard library documentation page for the module is not written in a tutorial style and it 
does not include many examples on how to use the classes. 

[io module documentation](https://docs.python.org/3/library/io.html)

The *Python 3 Module of the Week* has a short page for the module, which has three 
good examples. 

[io module on PyMOTW-3](https://pymotw.com/3/io/index.html)

The source code of the `io.py` only has 99 lines. which is a wrapper for the low level 
built-in C module `_io`.  This 
[stack overflow answer](https://stackoverflow.com/questions/26208863/whats-the-difference-between-io-and-io) 
explains how the source code is organized. Unfortunately I don't want to read 
the C code at this moment, so I really don't have much to discuss in this post. 
Hopefully I could add more to this post in the future when I read the C source 
code or discover some good resources on this topic. 
 

