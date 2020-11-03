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

If you ignore the exception handling code for a minute, the code is not too difficult to 
understand.

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
request relevant information". Let's look at the class members defined in `__init__` 
method. 

- self.app
- self.request
- self.url_adapter
- self.flashes
- self.session
- self.preserved = Flase

The class defines a property `g` for easy access to the variable on the app stack. 
The main methods of the class is `push` and `pop` defined on Lines 355 and 398. 
To better understand those two methods, you can read 
[Patrick Kennedy's article](https://testdriven.io/blog/flask-contexts-advanced/). 
The interesting part of `push` method is that session is part of the request 
context object and is initialized here.  The `_request_ctx_stack` object is 
a global variable defined in global.py module.  

```python
def push(self):
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