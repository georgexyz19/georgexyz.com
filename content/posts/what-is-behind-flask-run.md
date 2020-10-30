title: What Is Behind Flask Run Command
slug: what-is-behind-flask-run
date: 2020-10-29 22:06
modified: 2020-10-29 22:06
tags: flask
note: trace source code for Flask Run command
no: 58

Chapter 2  of Miguel Grinberg's *Flask Web Development* describes how to run a basic Flask app. 
Suppose you have a basic Flask app like below (from the book). 

```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello World</h1>'
```

You can use the Python 3 build in venv module to create a virtual environment like below. 

```
$ python -m venv ven
$ source venv/bin/activate
$ pip install flask
```

Here is output of `flask freeze` command.  The `pip install` command also installs Flask dependencies.  

```
click==7.1.2
Flask==1.1.2
itsdangerous==1.1.0
Jinja2==2.11.2
MarkupSafe==1.1.1
Werkzeug==1.0.1
```

Then you can setup two environment variables and type `flask run` to start the app. But what happens 
when you start the command `flask run`?  I am trying to figure out the answer and this article records 
my efforts. 

```
$ export FLASK_APP=hello.py
$ export FLASK_ENV=development
$ flask run
```

When you run the command `pip install flask`, the pip system installs a `flask` python script in the 
`venv/bin/` directory.  You can think of `flask` as a command and `run` as an argument to the command. 
The `run` part is actually a sub-command.  You can run `flask --help` to find out other available 
sub-commands. 

The `flask` script file in `venv/bin/` directory only has a few lines as shown below. The script is 
calling the `main()` function in the flask.cli module. 

```
import re
import sys

from flask.cli import main

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(main())
```

Let's open the `cli.py` file in `venv\lib\python3.8\site-packages\flask` directory. Line 965 
defines the `main` function. Here the `as_module` argument is `False` and the main funtion 
calls `cli.main` method with two arguments args=['run', ] and prog_name=None. The `cli` part 
of `cli.main` method call is an object of FlaskGroup class which is defined on Line 945.  

```
def main(as_module=False):
    # TODO omit sys.argv once ... is fixed
    cli.main(args=sys.argv[1:], 
        prog_name="python -m flask" if as_module else None)
```

Here things become complicated and I have not figured everything out.  The FlaskGroup class 
is defined on Line 462 and it has a main method defined on Line 567 (code shown below). 
The method makes changes to some settings and calls the `main` method in super class.   

```
def main(self, *args, **kwargs):

    os.environ["FLASK_RUN_FROM_CLI"] = "true"

    if get_load_dotenv(self.load_dotenv):
        load_dotenv()

    obj = kwargs.get("obj")

    if obj is None:
        obj = ScriptInfo(
            create_app=self.create_app, set_debug_flag=self.set_debug_flag
        )

    kwargs["obj"] = obj
    kwargs.setdefault("auto_envvar_prefix", "FLASK")
    return super(FlaskGroup, self).main(*args, **kwargs)
```

The `FlaskGroup` is derived from `AppGroup` class which is defined on Line 431. The `AppGroup` 
in turn is derived from `click.Group` class defined in `core.py` file in click package. The 
class derivation tree is shown below. 

```
FlaskGroup                      cli.py Line 462
  AppGroup                      cli.py Line 431
    click.Group                 click/core.py Line 1331
      click.MultiCommand             /core.py Line 1069
        click.Command                /core.py Line 832
          click.BaseCommand          /core.py Line 631
```

I am stopping here and will continure tomorrow 11:28PM. 


