title: Pelican Cache Module
slug: pelican-cache-module
date: 2020-05-08 09:49
modified: 2020-05-08 09:49
tags: pelican, python
note: Pelican python cache module description
related_posts: print-source-code-paper, pelican-source-code-plugin
no: 44

Pelican cache module ([cache.py](https://github.com/getpelican/pelican/blob/4.2.0/pelican/cache.py)) 
is relatively independent of other modules. It uses pickle module 
to serialize data and logger module to output debug and warning messages. The module 
defines two classes `FileDataCacher` and `FileStampDataCacher`. The `FileStampDataCacher` class derives from 
`FileDataCacher` and
adds file stamp to serialized data. File stamp could be modified time or a hash value of file content. 
Both classes have four methods `__init__`, `get_cached_data`, `cache_data`, and `save_cache`. 
The concept code below shows how they work. 

```
content = get_cached_data(path)
if content is None:
    content = read(path)
    cache_data(path, content)
    save_cache()
```

The Pelican documentation has a section 
"[Reading only modified content](https://docs.getpelican.com/en/stable/settings.html?highlight=cache#reading-only-modified-content)" 
on how to use caching. You should at least set those two setting values to `True` to 
turn on caching. 

CACHE_CONTENT
: True to save cache; default is False.

 LOAD_CONTENT_CACHE
: True to load cache; default is False.

Other cache related settings are listed below. 

CACHE_PATH
: default is `cache`; caching files are saved in this directory.

CONTENT_CACHING_LAYER
: `Readers` and `CachingGenerators` classes are derived from `FileStampDataCacher`. You can 
set the value to 'reader' or 'generator'; default value is `reader`. 

GZIP_CACHE
: use GZIP package to compress caching file; default is True. 

CHECK_MODIFIED_METHOD
: method to check if a file is modified sincing last caching; default is `mtime`.  The 
value can be a method name in `hashlib` module such as `md5` or `sha256`. 


The initialization method of both classes has four arguments. Unfortunately those 
arguments do not have default values, which make them difficult to use in other 
python projects. These 4 arguments are listed below.  It seems that only `cache_path` 
argument is mandatory. 

<!-- use definition list, add css for dl in custom.css -->
settings
: a dict of settings, a few keys `CACHE_PATH`, `GZIP_CACHE`, and `CHECK_MODIFIED_METHOD` are required for the class. 

cache_path
: the file name to cache.

caching_policy
: bool value to decide saving cache. 

load_policy
: bool value to decide loading cache. 

You can derive a class from `FileStampDataCacher` and add default values for three 
arguments of `__init__` method. 

```python
from pelican.cache import FileStampDataCacher

class FileCacher(FileStampDataCacher):
    def __init__(self, cache_name, settings = {
                    'CACHE_PATH': 'cache', 
                    'GZIP_CACHE': True,
                    'CHECK_MODIFIED_METHOD': 'mtime' 
                    # or sha256, sha512 
                }, caching_policy=True, load_policy=True):
        super(FileCacher, self).__init__(
            settings, cache_name, caching_policy, load_policy
        )
```

Here is an exmple to test the derived class. 

```python
if __name__ == '__main__':
    
    cacher = FileCacher('cache_file') # filename of cache
    content = cacher.get_cached_data('./pelican_help.txt')
    print(f'content is {content}')
    if content is None:
        with open('./pelican_help.txt', 'r') as f:
            content = f.read()
        cacher.cache_data('./pelican_help.txt', content)
        cacher.save_cache()
```

The Pelican documentation cautions the use of cache module. The `cache.py` file 
in Pelican 4.2.0 has not been modified since 2015. It may be useful 
when a website has thousands of pages.  I personally do not have a use case 
for the cache module yet. 
