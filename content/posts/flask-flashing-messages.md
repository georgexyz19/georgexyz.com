title: Flask Flashing Messages
slug: flask-flashing-messages
date: 2020-11-13 14:21
modified: 2020-11-13 14:21
tags: flask
note: look at flash method and get_flashed_message
no: 63

Flask includes message flashing functionality as a core feature.  The Flask 
documentation has two sentences which summarize the functionality well. 

> The flashing system basically makes it possible to record a message 
> at the end of a request and access it on the next (and only the next) request.
> This is usually combined with a layout template to expose the message.

The *Flask Web Development* book describes *Message Flashing* on Pages 53-55. 
The Flask documentation also has a webpage titled 
*[Message Flashing](https://flask.palletsprojects.com/en/1.1.x/patterns/flashing/#message-flashing-pattern)*, 
which also includes code examples.  

You can call function `flash` in a view function like this. 

```python
from flask import flash

# inside view function
flash('Log in successfully')
```

The base template calls `get_flashed_messages` function and renders the 
messages. The code below renders the messages as an un-ordered list. 

```
{% with messages = get_flashed_messages() %}
  {% if messages %}
    <ul class="flashes">
    {% for message in messages %}
      <li>{{ message }}</li>
    {% endfor %}
    </ul>
  {% endif %}
{% endwith %}
```

Flashing messages also support categories.  You can pass a second 
argument category to `flash` method.  The above example code 
is modified to be like this. 

```
flash('Log in failed', 'error')
```
```
{% with messages = get_flashed_messages(with_categories=True) %}
  {% if messages %}
    <ul class="flashes">
    {% for category, message in messages %}
      <li class="{{ category }}">{{ message }}</li>
    {% endfor %}
    </ul>
  {% endif %}
{% endwith %}
```

The interesting part of the above code is that the function  `get_flashed_messages` is available to all 
template html files. How does it happen? Let's take a look at 
Flask source code. 

The `flask/__init__.py` file has those two lines of code 
(Lines 36 and 37). 

```python
from .helpers import flash
from .helpers import get_flashed_messages
```

The actual functions are defined on Lines 399 and 429 of `helpers.py` file.  
The code of of those two functions are not long.  The `message_flashed` 
variable in `flash` function is a signal, which I will discuss in a 
future article.  The key `_flashes` of `session` dictionary has a value which 
is a list. The list values are tuples.  Here is an example `[('message', 'log in'), ('error', 'log out')]`. 

```python
def flash(message, category="message"):
    """ ... """
    flashes = session.get("_flashes", [])
    flashes.append((category, message))
    session["_flashes"] = flashes
    message_flashed.send(
        current_app._get_current_object(), message=message, 
        category=category
    )
```

```python
def get_flashed_messages(with_categories=False, category_filter=()):
    """ ....  """
    flashes = _request_ctx_stack.top.flashes
    if flashes is None:
        _request_ctx_stack.top.flashes = flashes = (
            session.pop("_flashes") if "_flashes" in session else []
        )
    if category_filter:
        flashes = list(filter(lambda f: f[0] in category_filter, flashes))
    if not with_categories:
        return [x[1] for x in flashes]
    return flashes
```

The purpose of putting `flashes` on the top of `_request_ctx_stack.top` is that,
> further calls in the same request to the function will return the same messages.

How does Jinja2 know `get_flashed_messages` function? The code is in 
`create_jinja_environment` method of Flask class (Line 761 of app.py). 
The function is added to the Jinja2 environment globals along with 
other functions and variables. 

```python
def create_jinja_environment(self):
    ......
    rv = self.jinja_environment(self, **options)
    rv.globals.update(
        url_for=url_for,
        get_flashed_messages=get_flashed_messages,
        config=self.config,
        # request, session and g are normally added with the
        # context processor for efficiency reasons but for imported
        # templates we also want the proxies in there.
        request=request,
        session=session,
        g=g,
    )
    rv.filters["tojson"] = json.tojson_filter
    return rv
```






