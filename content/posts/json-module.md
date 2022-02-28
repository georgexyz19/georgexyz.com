title: Json Module
slug: json-module
date: 2022-02-28 09:35
modified: 2022-02-28 09:35
tags: python
note: note to be added
no: 83

The `JSON` module is often used to transmit data between web servers and applications. 
It is time to take a close look at this module after discussing several difficult 
modules. 

### References

Realpython website has a nice introductory article on Json. Here is the link, 

[Working With JSON Data in Python](https://realpython.com/python-json/)

The official Python document for Json module is good. 

[Official JSON Module Documentation](https://docs.python.org/3/library/json.html)

### Source Code

Like many other Python modules, the best way to learn is to read the source code. 
The json directory has five files. Here is a list of the files. 

```
$ cd ~/.pyenv/versions/3.9.7/lib/python3.9/json
$ find . -maxdepth 1 -name '*.py' -exec wc -l '{}' + | sort -n
   73 ./scanner.py
   78 ./tool.py
  356 ./decoder.py
  359 ./__init__.py
  442 ./encoder.py
 1308 total
```

The files in this module is quite short comparing with other modules. The total 
line count is 1,308.  The reason is that some of the source code is written in 
C and the code is in `_json` C module. But we are not going to discuss C code 
in this post. 

The `__init__` module defines several functions like `dump`, `dumps`, `load`, 
and `loads`.  For function `dumps`, it calls `JSONEncoder` to do the actual 
encoding work.  The code looks like this, 

```
# simplified code 
from .encoder import JSONEncoder
_default_encoder = JSONEncoder(...)

def dumps(obj, ....):
    return _default_encoder.encode(obj)

```

The `encoder.py` module only defines one class `JSONEncoder` and several 
functions.  The `encode` method is easy to understand. 

```
# encode method of JSONEncoder
def encode(self, o):
    """Return a JSON string representation of a Python data structure.
    """
    if isinstance(o, str):
        if self.ensure_ascii:
            return encode_basestring_ascii(o)
        else:
            return encode_basestring(o)

    chunks = self.iterencode(o, _one_shot=True)
    if not isinstance(chunks, (list, tuple)):
        chunks = list(chunks)
    return ''.join(chunks)

```

The `encode` method calls `iterencode` method to do the work. The `iterencode` 
method in turn calls `c_make_encoder` or `_make_iterencode` function. 
The `c_make_encoder` function is imported from C module. In simple cases, 
the Json module will call the C module to do the encoding. 

```
# in module scope
try:
    from _json import encode_basestring as c_encode_basestring
except ImportError:
    c_encode_basestring = None

# inside JSONEncoder class
def iterencode(self, o, _one_shot=False):

    ......

    if (_one_shot and c_make_encoder is not None
            and self.indent is None):
        _iterencode = c_make_encoder(...)
    else:
        _iterencode = _make_iterencode(...)
    return _iterencode(o, 0)

```

The `_make_iterencode` function shows how to convert a Python object to 
a JSON iterable. There are recursive calls to do the conversion. The 
code is not easy to write. 

The `decoder.py` module is the opposite of `encoder.py` module.  It defines 
a `JSONDecoder` class to do the decoding work. The decoding is more complicated 
than the encoding, but most of the implementation is in C code. The `scanner.py` 
module defines a helper function `make_scanner` for `decoder.py` module. 

The `tool.py` module defines a command line tool, so we can use the module 
in bash like this. 

```
$ echo '{"json": "obj"}' | python -m json.tool
$ python -m json.tool infile outfile
$ python -m json.tool --help   # to find more about the command line tool
```


