title: Python Optparse and Argparse Example
slug: python-argparse
meta: An example showing how to use optparse and argparse Python modules
date: 2019-04-01 21:18
modified: 2019-04-01 21:18
tags: python


Argparse module was in Python version 3.2 and up.  It superseded
optparse module. Inkscape 0.92 extension program inkex.py file was
written many years ago with optparse module. I read several articles trying 
to understand how to use optparse and argparse modules. 
An example discussed in this
[blog post](https://www.saltycrane.com/blog/2009/09/python-optparse-example/) 
is very helpful. 

The article has an example program designed with two options.  Run the program 
on command line with options and arguments shown on that blog, and it shows 
how optparse module works behind scene. 

Following code is a rewrite of the example with argparse. 
You can execute similar commands shown below and compare the results. 
Here is the link to the code in github: [github repo](https://github.com/georgexyz19/argparse_examples).  

```python
#!/usr/bin/env python3
# argparse_example.py
# This is a version using argparse
# revised by GHZ on 2/2019

import argparse

def main():

    parser = argparse.ArgumentParser(
        usage = 'usage: %(prog)s [options] filename'
    )

    parser.add_argument('-x', '--xhtml',
        action = 'store_true', dest = 'xhtml_flag',
        default = False,
        help = 'create a XHTML template instead of HTML'
        )
    
    parser.add_argument('-c', '--cssfile',
        action = 'store',
        dest = 'cssfile',
        default = 'style.css',
        help = 'CSS file to link',
    )

    parser.add_argument('filename', nargs='?',  # '*' for multiple files
        action = 'store',
        help = 'the name of file to be processed'
    )

    parser.add_argument('-V', '--version',
        action='version', version='%(prog)s 1.0')

    args = parser.parse_args()
    print(args)
    print(args.filename)

if __name__ == '__main__':
    main()
```

Here are the bash commands to test code. 

```
python argparse_example.py -h
python argparse_example.py 
python argparse_example.py myfile.html
python argparse_example.py -x -c mystyle.css myfile.html
python argparse_example.py --xhtml --cssfile=mystyle.css myfile.html
```
The argparse module contains many other options.  Here is a link to 
[Python argparse Official Doc](https://docs.python.org/3/howto/argparse.html).

### Argparse v.s. Optparse

The two modules have some obvious differences. Run the commands below to 
start the scripts. The options or arguments start after `optparse_ex.py` 
and `argparse_ex.py`.  

```
$python2 optparse_ex.py ...
$python argparse_ex.py ...
```

The optparse module separates command line arguments into *options* and *args* 
two groups.  It calls `parser.add_option` methods to add options, and it does 
not need to add *args* to the parser beforehand. The argparse module has 
*positional arguments* and *optional arguments*.  It calls `parser.add_argument` 
method to add arguments. 

Argparse module seems to widely used in many open source projects, but newer 
third party module (e.g. Click) is also available. 
