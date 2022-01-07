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
The How-to article is written by the logging module author Vinay Sajip. The official Python documentation also has a Logging Cookbook article. 

[Logging How-To](https://docs.python.org/3/howto/logging.html)

[Logging Cookbook](https://docs.python.org/3/howto/logging-cookbook.html#logging-cookbook)

A 2018 PyCon presentation by Mario Corchero is also very nice.  PyCon talk video is usually better than 
other youtube teaching videos. Mario Corchero also writes an article which is published on opensource.com. 

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



