title: URL Mapping in Flask
slug: url-mapping-in-flask
date: 2020-11-05 22:38
modified: 2020-11-05 22:38
tags: flask, python
note: discuss url mapping in Flask
related_posts: understand-wsgi-interface-in-flask, django-WSGI
no: 61

URL Mapping is not a big topic in Flask.  The Flask documentation has a very short 
section on [URL Route Registrations](https://flask.palletsprojects.com/en/1.1.x/api/#url-route-registrations). 
Miguel Grinberg's *Flask Web Development (2nd)* book only discusses the topic briefly on pages 8-9 and 36-38. 
The `route` decorator is very straightforward to work with in Flask.  

```
@app.route('/)
def index():
    ....

@app.route('/user/<name>')
def user(name):
    ....
```

You can define the route function first and call `add_url_rule` method of Flask class to 
add the url rule.

```
def index():
    ....

app.add_url_rule('/', 'index', index)
```

If the URL mapping is only one directional which maps a URL route to a function, the Python code 
implementing the function should not be very complicated.  The URL mapping can also do reverse mapping. 
When you have an end point name `index`, you can call `url_for('index')` to get the URL route `/`, or
call `url_for('user', name='john')` to get the route `/user/john`. 

Let's take a quick look at the Flask code related to URL Mapping.

To be continued .......







