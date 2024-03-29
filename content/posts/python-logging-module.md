title: Python Logging Module
slug: python-logging-module
date: 2022-01-07 08:49
modified: 2022-01-07 08:49
tags: python
note: first post in 2022
related_posts: python-logging
no: 78

This is the first post of 2022.  I haven't updated the blog site for a while. 
This is new year and new start, and I wish to spend more time on 
Python. 

### Links

The Python logging module deserves more time and I am doing a little more research 
into this module. Here are some useful links regarding the module. 

Those two youtube videos by Corey Schafer are excellent introduction to the module. 

[Logging Basics - Video](https://youtu.be/-ARI4Cz-awo)

[Logging Advanced - Video](https://youtu.be/jxmzY9soFXg?list=TLPQMDcwMTIwMjLZ4KpK-A_TWw)

Those two videos cover the most contents in the official Python How-To article. 
The How-to article is written by the logging module author Vinay Sajip. 
The official Python documentation also has a Logging Cookbook article. 

[Logging How-To](https://docs.python.org/3/howto/logging.html)

[Logging Cookbook](https://docs.python.org/3/howto/logging-cookbook.html#logging-cookbook)

A 2018 PyCon presentation by Mario Corchero is also very nice.  PyCon talk video 
is usually better than other youtube teaching videos. Mario Corchero also writes 
an article which is published on opensource.com. 

[Mario Corchero - Effortless Logging - Video](https://youtu.be/Pbz1fo7KlGg?list=TLPQMDcwMTIwMjLZ4KpK-A_TWw)

[A Guide to Logging in Python](https://opensource.com/article/17/9/python-logging)

The Python logging module has three files (see below) and the documentations for 
them are listed below. 

[logging — Logging facility for Python](https://docs.python.org/3/library/logging.html)

[logging.config — Logging configuration](https://docs.python.org/3/library/logging.config.html#module-logging.config)

[logging.handlers — Logging handlers](https://docs.python.org/3/library/logging.handlers.html#module-logging.handlers)


### Source Code

The Python version 3.9.7 is installed in my Ubuntu linux computer. The Python is 
installed via a tool pyenv and the files are in the `~/.pyenv` directory. 

Here is the bash command to find out where the logging module is located. 

```
$ find ~/.pyenv -type d -name "logging"
/home/george/.pyenv/versions/3.9.7/lib/python3.9/logging
```

Here is a command to list number of lines in the logging module files. 

```
$ find . -name '*.py' -exec wc -l '{}' + | sort -n
   945 ./config.py
  1544 ./handlers.py
  2220 ./__init__.py
  4709 total
```

The source code is well written and well organized. The `__init__` module 
defines most classes like LogRecord, Formatter, Filter, Filterer, Handler, 
Manager, Logger, and RootLogger.  It also defines several global variables 
and functions like root (variable), basicConfig, getLogger, and info.  The 
root logger is an instance of `RootLogger` class.  The code is on line 
1900 (version 0.5.1.2) as shown below. 

```
root = RootLogger(WARNING)
Logger.root = root
Logger.manager = Manager(Logger.root)
```

The `Manager` class instance holds a dictionary of all loggers and it is 
saved as a class variable of the class Logger. The key of the dict is the 
name of the logger (like 'A.B.C') and the value is the logger itself. The 
doc string of the `Manager` class is, 

> There is [under normal circumstances] just one Manager instance, which
> holds the hierarchy of loggers.

If we have those two lines of code in a module, the logger `A.B` will become 
parent of `A.B.C`.  If we don't have a logger 'A', the class will create 
a `PlaceHolder` instance. The purpose of the hierarchy is that if we 
do not attach a handler for `abc` logger, it will use the handler of 
its parent to handle a LogRecord instance.  The `root` logger sits on 
the top of the hierarchy.  

```
ab = getLogger('A.B')
abc = getLogger('A.B.C')
```

The `getLogger` function in the `__init__` module looks like this, 

```
def getLogger(name=None):
    """
    Return a logger with the specified name, creating it if necessary.

    If no name is specified, return the root logger.
    """
    if not name or isinstance(name, str) and name == root.name:
        return root
    return Logger.manager.getLogger(name)
```

The `getLogger(self, name)` method in the `Manager` class is essentially like 
the code below.  If the logger is in the dict, it returns the logger. 
It it is not, the method creates a Logger instance and saves it in the dict.  

```
loggerDict = {}
if name in self.loggerDict:
    rv = self.loggerDict[name]
    ...
else:
    rv = Logger(name)
    ...
    self.loggerDict[name] = rv
    ...
return rv
```

A logger method like `warning` will call the `_log` method in the Logger class. 
The `_log` method then calls `makeRecord` and `handle` method.  The 
`makeRecord` method creates an instance of `LogRecord` class, and the `handle` 
method calls `callHandlers` method, which "loops through all handlers for 
this logger and its parents in the logger hierarchy". 

There are lots of details hiding in those classes and functions. The above 
description gives you a general idea of the logging module. 

The `config.py` file has configuration related classes and functions, and 
the `handlers.py` file has additional handlers.  The `__init__` module 
defines two common handlers `StreamHandler` and `FileHandler`. 

