title: Python Standard Library Module Logging
slug: python-logging
meta: A summary on how to use Python standard library module logging. 
date: 2019-04-04 20:57
modified: 2019-04-05 09:44
tags: python 
note: 013 016(realpython) 033 034


Python has a standard library module logging which is a very useful development 
tool.  When a development environment does not have access to command line 
interface such as writing an extension for Inkscape, a programmer cannot call `print` 
function to output intermediate program variables.  Instead, you use logging module
to monitor program flow. 

The default logger is named root.  You only need three lines of code to output
some information to a log file.  Predefined logging levels are debug, info, 
warning, error, and critical.  By default, root logger only outputs messages
with a severity level of warning and above. 

```python
import logging
logging.basicConfig(level=logging.DEBUG, filename='logging.txt')
logging.debug('This is a debug message')
``` 
Logging module defines many class.  Commonly used classes are Logger,
LogRecord, Handler, and Formatter.  Logger class is not instantiated directly. 
The first time call to module level function  `logging.getLogger(name)` returns
a Logger object.  Subsequent calls to the function return a reference to the same 
Logger object. A typical example looks like this, 

```python
logger = logging.getLogger(__name__)
f_handler = logging.FileHandler('file.log')  # StreamHandler
f_handler.setLevel(logging.ERROR)
f_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
f_handler.setFormatter(f_format)
logger.addHandler(f_handler)
logger.error('This is an error')
```

If you need a more versatile logging system, you create a config file or a 
dictionary and then load it using `fileConfig` or `dictConfig` methods. 
 
#### Reference
 
An article 
[Logging in Python](https://realpython.com/python-logging/) 
in realpython.com site is a very nice introduction to the topic. 

Here is a link to the official 
[Python logging module document](https://docs.python.org/3/howto/logging.html). 
 
