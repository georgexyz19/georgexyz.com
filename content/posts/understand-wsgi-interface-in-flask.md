title: Understand WSGI Interface and Request Context in Flask
slug: understand-wsgi-interface-in-flask
date: 2020-11-01 22:48
modified: 2020-11-01 22:48
tags: WSGI, flask
note: wsgi_app method in flask
related_posts: django-WSGI, flask-application-and-request-contexts
no: 59

The Flask class is defined in the app.py module.   The class has a `__call__` method 
defined on Line 2460 (Flask version 1.1.2).  If you have an object `app` that is an 
instance of Flask class,
you can treat the object as a function (or callable). When you call the object `app(...)`, 
it will actually run the code in `__call__` method.  

The `__call__` method in Flask class is simply calling another method `wsgi_app`, which 
I will discuss in this article.  The code in the method is not long (list below) 
because it just calls a few other methods. 

```python
def wsgi_app(self, environ, start_response):
    ctx = self.request_context(environ)
    error = None
    try:
        try:
            ctx.push()
            response = self.full_dispatch_request()
        except Exception as e:
            error = e
            response = self.handle_exception(e)
        except:  # noqa: B001
            error = sys.exc_info()[1]
            raise
        return response(environ, start_response)
    finally:
        if self.should_ignore_error(error):
            error = None
        ctx.auto_pop(error)
```

If you ignore the exception handling code for a minute, the code is not too long. It is 
something like this. 

```
def wsgi_app(self, environ, start_response):
    ctx = self.request_context(environ)
    ctx.push()
    response = self.full_dispatch_request()
    rv = response(environ, start_response)
    ctx.auto_pop(error)  //show concept only
    return rv
```

Let's look the first line of the method in detail.  

```python
ctx = self.request_context(environ)
```

The `request_context` method is defined on Line 2345, and the method is returning a 
`RequestContext` object. Notice the first argument to the `RequestContext` constructor is 
`self`, which is an instance of the Flask class.  

```python
def request_context(self, environ):
    return RequestContext(self, environ)
```

The `RequestContext` class is defined on Line 255 of the ctx.py module.  The first 
sentence of the class documentation states that "the request context contains all 
request relevant information". Let's look at the instance variables initialized 
in `__init__` method. 

- self.app
- self.request
- self.url_adapter
- self.flashes
- self.session
- self.preserved = False

The class defines a property `g` for easy access to the variable on the app stack. 
The main methods of the class are `push` and `pop` defined on Lines 355 and 398. 
To better understand those two methods, you can read 
[Patrick Kennedy's article](https://testdriven.io/blog/flask-contexts-advanced/). 
The interesting part of `push` method is that session is part of the request 
context object and is initialized here.  The `_request_ctx_stack` object is 
a global variable defined in global.py module.  

```python

def push(self):
    top = _request_ctx_stack.top
    if top is not None and top.preserved:
        top.pop(top._preserved_exc)

    app_ctx = _app_ctx_stack.top
    if app_ctx is None or app_ctx.app != self.app:
        app_ctx = self.app.app_context()
        app_ctx.push()
        self._implicit_app_ctx_stack.append(app_ctx)
    else:
        self._implicit_app_ctx_stack.append(None)

    if hasattr(sys, "exc_clear"):
        sys.exc_clear()

    _request_ctx_stack.push(self)

    if self.session is None:
        session_interface = self.app.session_interface
        self.session = session_interface.open_session(self.app, self.request)

        if self.session is None:
            self.session = session_interface.make_null_session(self.app)

    if self.url_adapter is not None:
        self.match_request()
```

I will stop here for now and look at other code in `wsgi_app` at a later time.   

<hr>

*updated on 3/28/2021*

Those three concepts are confusing if you do not read the source code. Kennedy's article 
helps to make them clear.  

1.&nbsp;*Request Context*

The request context refers to the instance of `RequestContext` class.  It contains 
all request relevant information.  

2.&nbsp;*Request Stack*

The request stack is an `LocalStack` *context local* object. It is defined in `globals.py` 
file L57. The `RequestContext` object has a `push` method and it can push itself onto
the stack.  

3.&nbsp;*Request*

The flask `request` object is a LocalProxy to the `request` instance variable of 
`RequestContext` class. It is defined on L60 of `globals.py` file. 

```
# globals.py
_request_ctx_stack = LocalStack()
request = LocalProxy(partial(_lookup_req_object, "request"))

# L35 of globals.py
def _lookup_req_object(name):
    top = _request_ctx_stack.top
    if top is None:
        raise RuntimeError(_request_ctx_err_msg)
    ## this is to get request instance variable from RequestContext
    return getattr(top, name)  
```

Miguel Grinberg's *Flask Web Development* Book Chapter 2 Page 18 has an example to show
how the application context works. 

```
(venv) george@X220:~/Code/flask-hello$ python
Python 3.9.2 (default, Mar 19 2021, 09:17:52) 
[GCC 9.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from hello import app
>>> from flask import current_app
>>> current_app.name
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  ...
RuntimeError: Working outside of application context.

This typically means that you attempted to use functionality that needed
to interface with the current application object in some way. To solve
this, set up an application context with app.app_context().  See the
documentation for more information.
>>> app_ctx = app.app_context()
>>> app_ctx.push()
>>> current_app.name
'hello'
>>> app_ctx.pop()
```

The reason of the runtime exception is that the `app` is not invoked by the 
WSGI server. If the `app` is called by the server, the `wsgi_app` method 
will automatically create the application context and push it on to the stack. 
But it will be difficult to show the process in a python session. 

The code in ctx.py file shows that `app` and `g` are instance variables 
of `AppContext`, `request` and `session` are instance variables of `RequestContext` 
class. Miguel Grinberg's book refers those variables as "flask context globals" 
on Table 2-1 (Page 2-1).  Those are probably should be called "context locals" as 
in Kennedy's article. 

The paragraphs of this article could be better organized, and I will revise the 
article again later.  This probably is the most important topic in Flask. 
