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

You can use the Python 3 built-in venv module to create a virtual environment like below. 

```
$ python -m venv venv
$ source venv/bin/activate
$ pip install flask
```

Here is output of `pip freeze` command.  The `pip install` command installs several Flask dependencies.  

```
click==7.1.2
Flask==1.1.2
itsdangerous==1.1.0
Jinja2==2.11.2
MarkupSafe==1.1.1
Werkzeug==1.0.1
```

Then you can setup two environment variables and type `flask run` to start the app. But what happens 
when you start the command `flask run`?  I am trying to find out the answer and this article documents 
the effort. 

```
$ export FLASK_APP=hello.py
$ export FLASK_ENV=development
$ flask run
```

When you run the command `pip install flask`, the pip system installs a `flask` python script file in the 
`venv/bin/` directory.  You can think of `flask` as a command and `run` as an argument to the command. 
The `run` part is actually a sub-command in `click`.  You can run `flask --help` to 
find out other available sub-commands. 

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

Let's open the `cli.py` file in `venv\lib\python3.8\site-packages\flask` directory.  Line 965 
defines the `main` function. The `as_module` argument is `False` and the `main` function 
calls `cli.main` method with two arguments `args=['run', ]` and `prog_name=None`. The `cli` part 
of `cli.main` is an instance of FlaskGroup class defined on Line 945.  

```
def main(as_module=False):
    # TODO omit sys.argv once ... is fixed
    cli.main(args=sys.argv[1:], 
        prog_name="python -m flask" if as_module else None)
```

Here things become complicated and I have not figured everything out.  

The `__init__` method of `FlaskGroup` class (L487) adds three sub-commands to click. 
The `add_command` method is defined on L1343 Group class of click/core.py file. 

```python
if add_default_commands:
    self.add_command(run_command)
    self.add_command(shell_command)
    self.add_command(routes_command)
```

The FlaskGroup class 
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
in turn is derived from `click.Group` class defined in `core.py` file in click package. The complete
class inheritance tree is shown below.  The `main` method in super class mentioned above is 
defined all the way up in `click.BaseCommand` class.   

```
FlaskGroup                      cli.py Line 462
  AppGroup                      cli.py Line 431
    click.Group                 click/core.py Line 1331
      click.MultiCommand             /core.py Line 1069
        click.Command                /core.py Line 832
          click.BaseCommand          /core.py Line 631
```

Let's get back to the `flask/cli.py` file and take a look at `AppGroup` class. The 
`AppGroup` class overrides two methods (decorators) `command` and `group`.  It 
changes the behavior of the standard `command` decorator so that it automatically 
wraps the functions in `with_appcontext`. You can see examples of how those two 
decorators are used on the
[click documentation](https://click.palletsprojects.com/en/7.x/commands/) page. 

The `FlaskGroup` class overrides `get_command` and `list_commands` methods in addition 
to the `main` method. The 
[click documentation](https://click.palletsprojects.com/en/7.x/commands/) 
has a section *Custom Multi Commands* and the example in this section also overrides
those two methods. 

The actual `run` command is defined on Line 828 and the function is `run_command`. 
The command `run` becomes part of flask built in commands loaded by default. 
The code which loads the built in commands is in the `FlaskGroup.get_command`.  

The `run_command` function look like this.  It calls the `run_simple` function in 
werkzeug module and starts the development server.  The `DispatchingApp` class 
is also interesting, and it loads the app based on the environment variable 
settings.  I will discuss it in a later article. 

```python
@click.command("run", short_help="Run a development server.")
@click.option("--host", "-h", default="127.0.0.1", ...")
...
@pass_script_info
def run_command(info, host, port, ...):
    """Run a local development server."""
    ......
    show_server_banner(get_env(), debug, info.app_import_path, eager_loading)
    app = DispatchingApp(info.load_app, use_eager_loading=eager_loading)

    from werkzeug.serving import run_simple
    run_simple(host, port, app, ......)
```

The `shell` and `routes` commands are defined on Line 864 and Line 899 of 
the `cli.py` file.   

The Flask documentation has a page 
[Command Line Interface](https://flask.palletsprojects.com/en/1.1.x/cli/) 
which has very good info on Flask CLI. 



