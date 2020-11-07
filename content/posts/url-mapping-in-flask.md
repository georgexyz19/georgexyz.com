title: URL Mapping in Flask
slug: url-mapping-in-flask
date: 2020-11-05 22:38
modified: 2020-11-05 22:38
tags: flask, python
note: discuss url mapping in Flask
related_posts: understand-wsgi-interface-in-flask, django-WSGI
no: 61

URL Mapping (or URL Routing) is not a big topic in Flask.  The Flask documentation has a very short 
section on [URL Route Registrations](https://flask.palletsprojects.com/en/1.1.x/api/#url-route-registrations). 
Miguel Grinberg's *Flask Web Development (2nd)* book only discusses the topic briefly on pages 8-9 and 36-38. 
The `route` decorator is very straightforward to use in Flask.  

```python
@app.route('/)
def index():
    ....

@app.route('/user/<name>')
def user(name):
    ....
```

You can define the route function first and call `add_url_rule` method of Flask class to 
add the url rule.

```python
def index():
    ....

app.add_url_rule('/', 'index', index)
```

If the URL mapping is only one directional that maps a URL route to a function, the Python code 
implementing it should not be very complicated.  The URL mapping can also do reverse mapping. 
When you have an end point name `index`, you can call `url_for('index')` to get the URL route `/`, or
call `url_for('user', name='john')` to get the route `/user/john`. 

Let's look at the Flask source code to find out more about URL mapping.  The `__init__` method 
of Flask class defines an instance variable `url_map` on Line 582.  

```python
self.url_map = self.url_map_class()
self.url_map.host_matching = host_matching
```

The `url_map_class` is a class variable defined on Line 366 which is `Map` class imported 
from `werkzeug.routing` module. 

The `add_url_rule` method is defined on Line 1177 in app.py module.  The method is quite 
long, and part of the code is shown below. 

```python
if endpoint is None:
    endpoint = _endpoint_from_view_func(view_func)
...
rule = self.url_rule_class(rule, methods=methods, **options)
...
self.url_map.add(rule)
...

if view_func is not None:
    ...
    self.view_functions[endpoint] = view_func

```

The `url_rule_class` is referring to `Rule` class imported from `werkzeug.routing`.  
The `view_functions` is one of the instance variables (dictionary) of Flask class 
defined on Line 444. 

The `route` decorator is defined on Line 1288.  It calls the `add_url_method` method, 
and the code is shown below. 

```python
def route(self, rule, **options):
        def decorator(f):
            endpoint = options.pop("endpoint", None)
            self.add_url_rule(rule, endpoint, f, **options)
            return f

        return decorator
```

The `route` decorator is interesting.  If you read Miguel Grinberg's 
[ultimate guide to Python decorator](https://blog.miguelgrinberg.com/post/the-ultimate-guide-to-python-decorators-part-i-function-registration), 
it is a combination of *Function Registration* and *Decorators with 
Arguments*.  

The URL reverse function `url_for` is defined on Line 226 of helpers.py 
module. The functions retrieves a `url_adapter` from request context or 
app context, and calls `build` method on `url_adapter` to return the 
reversed URL.  

```python
appctx = _app_ctx_stack.top
reqctx = _request_ctx_stack.top

if reqctx is not None:
    url_adapter = reqctx.url_adapter
    ...
else:
    url_adapter = appctx.url_adapter
...
rv = url_adapter.build(
    endpoint, values, method=method, force_external=external
)
```

When does this `url_adapter` is initialized? The `url_adapter` is one of 
instance variables of `RequestContext` class defined on Line 290 in ctx.py module. 

```python
def __init__(self, app, environ, request=None, session=None):
    ....
    self.url_adapter = None
    try:
        self.url_adapter = app.create_url_adapter(self.request)
    ...
```

The `url_adapter` is also one of the instance variables of `AppContext` class
defined on Line 216 in ctx.py module. 

```python
def __init__(self, app):
    ...
    self.url_adapter = app.create_url_adapter(None)
```

The `create_url_adapter` method of `Flask` class calls `bind_to_environ` or
`bind` method of `Map` class to create an instance of `MapAdapter` class, which 
is also defined in `werkzeug.routing` module.

The actual URL mapping happens on Line 2447 of app.py module (inside `wsgi_app` 
method) in Flask.  It calls `full_dispatch_request` method of Flask class, which is 
defined on Line 1938. It then calls `dispatch_request` method, which is 
in turn defined on Line 1914. 

```python
def dispatch_request(self):
    """Does the request dispatching.  Matches the URL and returns the
    return value of the view or error handler. ...
    """
    ...
    return self.view_functions[rule.endpoint](**req.view_args)

```

The method simply uses the `view_functions` instance variable (a dictionary) 
to find the corresponding view function for the URL.  

The URL Routing functions are mainly provided by the Werkzeug package, which is 
one of the dependent packages of Flask. The Werkzeug documentation has a page 
specifically for [URL Routing](https://werkzeug.palletsprojects.com/en/1.0.x/routing/).  







