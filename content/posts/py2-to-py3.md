title: Convert Python 2 Code to Python 3
slug: py2-to-py3
meta: Experience of converting py2 code to py3 
date: 2020-02-10 12:07
modified: 2020-02-10 12:07
tags: python
note: 27

I am working on a personal project putting my OpenSignTool Inkscape 
python extension app online.  I plan to wrap the python code into 
a Flask web app and make the code run on a web server. 

The extension app is written in Summer 2018 and mostly python 3 ready. 
However, they depend on several existing Inkscape extension modules. 
Those are all python 2 code written years ago by others. Specifically, 
the extension code depends on 6 python modules. These are 

- simplestyle.py
- simplepath.py
- simpletransform.py
- inkex.py
- cubicsuperpath.py
- bezmisc.py

Originally I plan to test my app in python 3.7 and fix any errors 
that pop up. I work on fixing the code for one hour or two, and 
find that this approach is too timing consuming even for a small 
code base of a few hundred lines of code.

A little Google search finds that Python standard library includes a
2to3 tool that can do the job automatically. 
[The documenation](https://docs.python.org/3.8/library/2to3.html) is 
pretty straightforward. This is the command I used to convert all python 
files in the current directory. 

```
$2to3 -o ../dev_py3 -W -n ./
```

The option `-o` is to specify the output directory, `-W` is for 
writing files even not changed, and `-n` means that backups are not 
needed. 

The tool is very useful, and it can figure out almost all changes. The 
place the tool has trouble figuring out is string encoding.  I change 
a few places that involve string encoding, and the program runs 
perfectly in Python 3. 

The Inkscape project is upgrading the extension system to be Python 3 
compatible.  [The new extension python code](https://gitlab.com/inkscape/extensions) 
are available online. 

