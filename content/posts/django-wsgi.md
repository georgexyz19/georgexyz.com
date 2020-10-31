title: What is WSGI?
slug: django-WSGI
meta: Discuss WSGI
date: 2019-05-04 12:27
modified: 2019-05-04 12:27
tags: WSGI, django, flask
note: 100 and 100A
no: 11


WSGI is an abbreviation for Web Server Gateway Interface, which is a "simple calling 
convention for web servers to forward requests to web applications for frameworks written
in Python."   WSGI is part of Python ecosystem.  It was originally specified in PEP-333
in 2003, and was updated to 
[PEP-3333](https://www.python.org/dev/peps/pep-3333/) 
for python 3 in 2010.   Python standard library even has a wsgiref package (WSGI 
reference server) built in. 

Why do we need to know WSGI? A Django/Flask web app is essentially an WSGI app. A
web framework like Django/Flask adds many other functions such as database handling and 
template processing to generate html files. It helps a developer understand 
how web framework works behind the scene. 

The best writing on WSGI is probably 
[a blog post](http://lucumr.pocoo.org/2007/5/21/getting-started-with-wsgi/) 
by Armin Ronacher, who is the creator of Flask web framework and many other open 
source Python packages.   Three code examples in this article are fantastic 
prototypes showing how WSGI and web framework work. 

I would suggest anyone who is interested in this topic to read the article multiple times 
to get a good understanding 
of the topic.  The article was written in 2007 with Python 2.  A developer needs to
make small changes to the code for Python 3.  Here is the 
[link to github repo](https://github.com/georgexyz19/WSGI_example_code) 
which contains code I modified for Python 3.

You can run the WSGI app with a real server like [gunicorn](https://gunicorn.org/). 
Install gunicorn in the virtual environment and run the server with commands shown below.  When run the app with gunicorn, the `environ` dictionary variable has 29 keys, and it has 82 keys with `wsgiref` server. 

```
$ pip install gunicorn
$ gunicorn -w 4 get_started:hello_world
```


### References

[PEP 3333 - Python Web Server Gateway Interface v1.0.1](https://www.python.org/dev/peps/pep-3333/) 
on Python.org. 

Full Stack Python website has 
[an WSGI article](https://www.fullstackpython.com/wsgi-servers.html) 
which includes links to many other articles. 

[An online article](https://www.appdynamics.com/blog/engineering/an-introduction-to-python-wsgi-servers-part-1/) 
by Kevin Goldberg dicusses several WSGI web servers. 














