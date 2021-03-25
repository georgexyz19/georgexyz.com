title: Python Import Statement
slug: python-import-statement
date: 2021-03-25 09:40
modified: 2021-03-25 09:40
tags: flask, python
note: Python import based on Chap 7 of Miguel Grinberg book
no: 69

Python import statement seems very easy to use, but it can get complicated once the project 
scale becomes larger. It is one of those things that is easy to learn by looking at an example. 
Miguel Grinberg's book *Flask Web Development* Chapter 7 has such an example. The flask apps 
project structure looks like this.  

<div style="margin-left: 20px">
<pre>
flasky
├── app
│   ├── email.py
│   ├── __init__.py
│   ├── main
│   │   ├── errors.py
│   │   ├── forms.py
│   │   ├── __init__.py
│   │   └── views.py
│   ├── models.py
│   ├── static
│   │   └── favicon.ico
│   └── templates
│       ├── 404.html
│       ├── 500.html
│       ├── base.html
│       ├── index.html
│       ├── mail
│       │   ├── new\_user.html
│       │   └── new\_user.txt
│       └── user.html
├── config.py
├── data.sqlite
├── hello.py
├── migrations
├── README.md
├── requirements.txt
├── set\_env.sh
├── set\_mail.sh
└── tests
    ├── __init__.py
    └── test_basics.py
7 directories, 24 files
</pre>
</div>

When you are running the app (command `flask run`), you are in the `/flasky` directory. 
The `app/__init__.py` file defines a `create_app` function which is the app factory. It 
imports `config` dict from `config.py` file like this. 

```
from config import config
```

The `flasky.py` file imports the `create_app` from `app/__init__.py`. Here you can 
think of `app/__init__.py` as an `app.py` file. The `flasky.py` also imports db models 
from `app/models.py`.

```
from app import create_app
from app.model import User
```

The `test_basics.py` file also imports `create_app`. It uses the same import statement 
shown above. You can look at `app` here similar to an absolution path. 

Relative path is a little more difficult. The `app/main/views.py` file imports `User` 
model from `app/models.py` file. The statement looks like this. The first dot(.) goes 
into `app/main` directiory, and the second dot goest into `app` directory. 

```
from ..models import User
# from app.models import User  # could be
``` 

The interesting import statement is a circular one.  The `app/main/__init__.py` file 
imports views and errors modules at the end of the file. This import statement causes
the code in `views.py` and `errors.py` to run.  The purpose is to register view functions 
and error handler functions (via decorators). 

```
# app/main/__init__.py
from flask import Blueprint
main = Blueprint('main', __name__)
from . import views, errors  # MUST be at the end of the file
```

The `app/main/view.py` file also imports `main` from `app/main/__init__.py` 
like this. 

```
from . import main
@main.route(...)
```
