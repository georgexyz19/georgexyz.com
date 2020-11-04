title: Flask Application Context
slug: flask-application-context
date: 2020-11-03 15:19
modified: 2020-11-03 15:19
tags: flask
note: look at Flask AppContext code
related_posts: understand-wsgi-interface-in-flask, django-WSGI
no: 60

The `push` method of `RequestContext` class has those two lines of code (Lines 373 and 374 of 
ctx.py module in Flask 1.1.2) listed below. It pushes the application context 
variable `app_ctx` when a request context is pushed. 

```
app_ctx = self.app.app_context()
app_ctx.push()
```

The `app_context` method of `Flask` class is defined on Line 2324 in app.py file. The method 
is really simple and the code is shown below. It initializes an `AppContext` object and returns
it.  

```
def app_context(self):
    return AppContext(self)
```

The `AppContext` class is however defined on Line 205 of ctx.py file.  The code in `__init__` 
method of `AppContext` class is shown below. 

```
class AppContext(object):
    def __init__(self, app):
        self.app = app
        self.url_adapter = app.create_url_adapter(None)
        self.g = app.app_ctx_globals_class()

        # Like request context, app contexts can be pushed multiple times
        # but there a basic "refcount" is enough to track them.
        self._refcnt = 0
    ......
```

The `AppContext` class defines 4 instance variables `self.app`, `self.url_adapter`, 
`self.g`, and `self._refcnt`.  The interesting variable is `self.g`, which is 
an instance of `_AppCtxGlobals` class defined on Line 28 of ctx.py file.  Because 
it is a class object, you can set any attribute on the object like this. 

```
g.user = User(...)
```

The `push` and `pop` methods of `AppContext` class is simpler than methods in 
`RequestContext` class. It pushes or pops the object on the `_app_ctx_stack` 
global variable defined in `globals.py`.

I will discuss the `self.url_adapter` in a later article. 

