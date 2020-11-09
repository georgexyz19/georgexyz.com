title: Flask Extension System
slug: flask-extension-system
date: 2020-11-08 15:48
modified: 2020-11-08 15:48
tags: flask
note: flask extension discussion
no: 62

Flask is a micro web framework, and many functionalities are provided by various 
extensions. The Flask documentation only has two pages on extensions, one is on 
[how to use extensions](https://flask.palletsprojects.com/en/1.1.x/extensions/#extensions) 
and the other is about 
[how to develop new extensions](https://flask.palletsprojects.com/en/1.1.x/extensiondev/).  

### Flask-Bootstrap

Let's look at the source code of some popular extensions in this article.  The 
first one is Flask-Bootstrap.  When you read Miguel Grinberg's *Flask Web 
Development* book, you will find that Flask-Bootstrap not only helps Flask
integrating with Bootstrap, it also helps integrating Bootstrap with WTForms 
and provides a `quick_form` function.  You can render a form like this. 

```
{% import "bootstrap/wtf.html" as wtf %}
{{ wtf.quick_form(form) }}
```

The drawback of this extension is that it has not been updated for sometime. 
The Bootstrap 4 has been released a while, but the extension 
still includes the version 3.  There is a fork Flask-BS4 with Bootstrap 4, 
but it is not as popular as Flask-Bootstrap. 

After you pip install Flask-Bootstrap in a virtual environment, the 
files are installed in this directory. 

<pre>
.../venv/lib/python3.8/site-packages/flask_bootstrap
</pre>

The directory has three Python files `__init__.py`, `forms.py`, and 
`nav.py`.  It also has two directories `static` and `templates`. 
The directory structure looks like this. 

<div style="margin-left: 20px">
<pre>
├── forms.py
├── __init__.py
├── nav.py
├── static
│   ├── css
│   │   ├── bootstrap.css
│   │   ├── ....
│   ├── fonts
│   │   ├── glyphicons-halflings-regular.eot
│   │   ├── ....
│   ├── jquery.js
│   ├── jquery.min.js
│   ├── jquery.min.map
│   └── js
│       ├── bootstrap.js
│       ├── bootstrap.min.js
│       └── npm.js
└── templates
    └── bootstrap
        ├── base.html
        ├── fixes.html
        ├── google.html
        ├── pagination.html
        ├── utils.html
        └── wtf.html
</pre>
</div>

When you use the Flask-Bootstrap in an app, you initialize it with 
those two lines. 

```
from flask_bootstrap import Bootstrap
....
bootstrap = Bootstrap(app)
```

The `Bootstrap` class is defined on Line 123 (version 3.3.7.1) of 
`__init__.py` file. The `init_app` method does the actual initialization 
work. 

```python
def init_app(self, app):
    app.config.setdefault('BOOTSTRAP_USE_MINIFIED', True)
    ......

    blueprint = Blueprint(
        'bootstrap',
        __name__,
        template_folder='templates',
        static_folder='static',
        static_url_path=app.static_url_path + '/bootstrap',
        subdomain=app.config['BOOTSTRAP_LOCAL_SUBDOMAIN'])

    # add the form rendering template filter
    blueprint.add_app_template_filter(render_form)

    app.register_blueprint(blueprint)

    app.jinja_env.globals['bootstrap_is_hidden_field'] =\
        is_hidden_field_filter
    app.jinja_env.globals['bootstrap_find_resource'] =\
        bootstrap_find_resource
    app.jinja_env.add_extension('jinja2.ext.do')

    if not hasattr(app, 'extensions'):
        app.extensions = {}
    ......
```

The interesting part of the `init_app` method is that it registers itself as 
a blueprint (sub application) of the app. After you initialize 
the extension, the app will search template and static files 
in this extension. 

### Flask-Moment

Flask-Moment is introduced in Chapter 3 (pages 38-41) of the 
*Flask Web Development* book. 
The extension is actually created by Miguel Grinberg. The extension 
makes [Moment.js Javascript library](https://momentjs.com/) 
easy to use in Flask. 

The Flask-Moment is simple, and it only has one file `flask_moment.py` 
which is 198 lines long.  The `Moment` class code is shown below. 

```python
class Moment(object):
    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        if not hasattr(app, 'extensions'):
            app.extensions = {}
        app.extensions['moment'] = _moment
        app.context_processor(self.context_processor)

    @staticmethod
    def context_processor():
        return {
            'moment': current_app.extensions['moment']
        }

    def create(self, timestamp=None):
        return current_app.extensions['moment'](timestamp)
```

The `context_processor` static method returns a dictionary.  The key (`moment`) is 
the variable or method name used in template, and the value (`current_app.extensions[moment]` refers to `_moment`) is the actual Python variable or method. The 
implementation here is a little difficult to understand at a glance.  The `_moment`
is actually a class defined in the same file.   

```python
class _moment(object):
    @staticmethod
    def include_moment(version=default_moment_version, 
                       local_js=None,
                       no_js=None, sri=None):
        js = ''
        ...
    ......

    def __init__(self, timestamp=None, local=False):
        if timestamp is None:
            timestamp = datetime.utcnow()
        self.timestamp = timestamp
        self.local = local

    ......
    def fromNow(self, no_suffix=False, refresh=False):
        return self._render("fromNow", 
                            no_suffix=int(no_suffix),
                            refresh=refresh)
    ......
```

Let's look at an example in a template file. 

```
{{ moment(current_time).fromNow(refresh=True) }}
```

When you have this template variable in your template file, the 
`moment(current_time)`  part is actually calling the `__init__` 
method of `_moment` class. The return 
value is an instance of `_moment` class.  The `fromNow` method is called on
this instance.  It then calls the `_render` method, which returns a `<span>`
html element which has a class attribute `flask-moment`. 

```python
def _render(self, func, format=None, timestamp2=None, 
                no_suffix=None,
                refresh=False):
        t = self._timestamp_as_iso_8601(self.timestamp)
        ......
        return Markup((
            '<span class="flask-moment" data-timestamp="{}" ' +
            '{} data-refresh="{}" ' +
            'style="display: none">{}</span>').format(
            t, data_values, int(refresh) * 60000, t))
```

The `include_moment` static method of `_moment` class includes a CDN link 
for the Moment Javascript library and three functions to render html elements 
with `flask-moment` class attribute.  

This `include_moment` method is quite interesting because the 
Python file includes Javascript code quoted as a multi-line string.  When Jinja2 
renders the template file, the string is rendered as Javascript code 
on the html file.  The html file is then transmitted to the client browser, 
and finally the browser runs the Javascript code originated in a 
Python file.  

