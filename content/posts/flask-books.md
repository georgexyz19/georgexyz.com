title: Two Flask Books by Miguel Grinberg
slug: flask-books
meta: April 1 post 
date: 2020-04-01 23:00
modified: 2020-04-01 23:00
tags: flask, books
note: A short post on April 1, 2020
no: 33

This static blog site started on Github one year ago on April 1, 2009. 
It has been one year, and it is going better than I originally planned. 
The most frequent visitor of the site is most likely myself, and the site 
serves as an online notepad for myself. 

I recently finished reading two Flask books by Miguel Grinberg.  The first 
one is *Flask Web Development - Developing Web Applications with Python*, and 
the second book is [The new and Improved Flask Mega Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world). 
Both books are fantastic. They are better than every Django book I have read, and they are 
definitely among the top programming books. 

<div style="max-width:400px">
  <img class="img-fluid pb-3" src="/images/flask-books.jpg" alt="Flask books"> 
</div>

Here are some tips to work with the Flask Web Development 
[source code flasky](https://github.com/miguelgrinberg/flasky). 


```
$ git clone https://github.com/miguelgrinberg/flasky.git
$ git checkout 8e
$ git checkout -b exercise
$ python -m venv venv
$ source venv/bin/activate
$ pip3 install -r requirements.txt
$ source setup.sh  # content see below
$ flask db upgrade
$ flask run
```

The `setup.sh` file sets two environment variables. 

```bash
export FLASK_APP=flasky.py
export FLASK_DEBUG=1
echo "setup FLASK_APP and FLASK_DEBUG"
```

If you run the commands above, the flask app will prompt errors because 
the configuration for the email smtp server is not complete. It is 
easier to setup a local smtp testing server than setup email accounts. 
Open a new terminal window and type the command below. The command 
invokes a standard python module smtpd and starts a debugging email 
server. 

```
$python -m smtpd -n -c DebuggingServer localhost:8025
```

In the `config.py` file, add three lines to the DevelopmentConfig section.

```
class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')
    MAIL_SERVER = os.environ.get('MAIL_SERVER', 'localhost')  ### NEW
    MAIL_PORT = int(os.environ.get('MAIL_PORT', '8025'))
    MAIL_USE_TLS = False
```

You also need to initialize database when running the code base after 
Chapter 9 and Chapter 12. The commands are shown below. 

```
$ flask shell
>>> Role.insert_roles()
>>> User.add_self_follows()
```

