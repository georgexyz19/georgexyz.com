title: Remove Dash Conversion Of Smartypants Python Package
slug: remove-dash-conversion
date: 2021-04-07 13:31
modified: 2021-04-07 13:31
tags: web development, python, pelican
note: Pelican Plugin
related_posts: typogrify-python-package
no: 72

When I am working on the last post 
[Git Command Reference]({filename}git-command-reference.md), 
git commands often 
include an option such as `git config --help`. Bash commands often have two dashes
`--` before options. The python `typogrify` package (used in pelican) invokes `smartypants` package 
to convert `--` into html en-dash `&#8212;`, and `---` into em-dash `&#8211;`. 
However after checking the `smartypants` source code, I found that by default 
it actually only convert en-dash, not em-dash. 

This is a case of code becoming too smart. I do not want two dashes `--` to show up 
as en-dash.  How to turn this feature off? Reading my previous post 
[Typogrify Python Package]({filename}typogrify-python-package.md), it is easy to 
create a new pelican plugin to remove this conversion. 

Here are the code in `mod_typogrify.py`. 

```
from pelican import logger
from pelican import signals

from typogrify import filters

def init_mod_typogrify(sender):
    logger.debug('Init mod_typogrify Plugin')

def register():
    signals.initialized.connect(init_mod_typogrify)

    def smartypants(text):
        """Applies smarty pants to curl quotes.
    
        >>> smartypants('The "Green" man')
        'The &#8220;Green&#8221; man'
        """
        try:
            import smartypants
        except ImportError:
            raise TypogrifyError("Error in {% smartypants %} filter: ")
        else:
            from smartypants import Attr        #----- NEW
            attr = Attr.set1 & (~(Attr.mask_d)) #----- NEW
            output = smartypants.smartypants(text, attr) #--- add attr
            return output

    filters.smartypants = smartypants
```

I only added two lines and modified a line of `smartypants` function in `typogrify` 
to make it work. But figuring out 
how to create the correct `attr` took some time. Here is the bash session 
history when I am doing the experiment. 

```
(venv) george@X220:~/Code/georgexyz.com$ python
Python 3.9.2 (default, Mar 19 2021, 09:17:52) 
[GCC 9.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from smartypants import Attr
>>> Attr.mask_d
56
>>> bin(Attr.mask_d)
'0b111000'
>>> bin(Attr.set1)  #---- default setting
'0b1001011'
>>> bin(Attr.set1 & (~(Attr.mask_d)))
'0b1000011'
```

Here is a test of -- and ---. They should show up as two dashes and three dashes 
instead of en-dash and em-dash. 

This code change involves Python bitwise operators.  Here is a link to 
[Bitwise Operator on Python.org](https://wiki.python.org/moin/BitwiseOperators). 

