title: What is WSGI Request/Response Process
slug: django-request-response
meta: Discuss django process and WSGI
date: 2019-05-04 12:27
modified: 2019-05-04 12:27
tags: django
status: draft
note: none
no: 11


Most Django tutorials and books do not discuss how the web framework starts and finishes. 
A developer needs to dig into source code and online blog posts to find out how Django 
processes a request. Fortunately many people have written on this topic and 
[Django source code](https://github.com/django/django/tree/2.2)
is easily accessible to anyone who is interested. 

In this article, I am writing down my understanding of this process. 
A developer does not have to know this process to create great web apps, but it is always 
interesting to know how web framework works behind the scene.  Before we discuss 
Django code, let's look at WSGI first. 

### WSGI

WSGI is an abbreviation for Web Server Gateway Interface, which is a "simple calling 
convention for web servers to forward requests to web applications for frameworks written
in Python."   WSGI is part of Python ecosystem.  It was originally specified in PEP-333
in 2003, and was updated to PEP-3333 for python 3 in 2010.   Python standard library even 
has a wsgiref WSGI reference server built in. 

The best writing on WSGI is probably 
[a blog post](http://lucumr.pocoo.org/2007/5/21/getting-started-with-wsgi/) 
by Armin Ronacher, who is the creator of Flask web framework and many other open 
source Python packages.   Three code examples in this article are fantastic 
prototypes showing how WSGI and web framework work.  I would suggest anyone 
who is interested to read the article multiple times to get a good understanding 
of the topic.  The article was written in 2007 with Python 2.  A developer needs to
make small changes to the code for Python 3.  Here are 
[the example code](https://github.com/georgexyz19/WSGI_example_code) 
I modified for Python 3.

Why do we need to know WSGI? A Python web app is essentially an WSGI app. A
web framework like Django adds many other functions such as database handling and 
template processing to generate html files. 

### Other Articles

After several google searches, I found a few related articles on the topic.  Those articles 
were written a few years ago, but most contents still apply to 
Django 2.2 which is the version I am looking at now.

[An article by Simon Willison](https://simonwillison.net/2005/Aug/15/request/) 
in 2005 is an early discussion on the topic.  This article does not contain any code. 
The ModPythonHandler class has been removed from recent Django releases. The article 
presents a good overview on how Django processes a request and how middleware works. 

James Bennett wrote 
[a long article](https://www.b-list.org/weblog/2006/jun/13/how-django-processes-request/) 
on his blog discussing how Django processes a request in 20016. The contents of the 
article are still very relevant today. 

[Another article](https://k4ml.me/posts/django-where-does-the-application-start.html) 
written by Kamal Mustafa is closer to what I am looking for.  The article discusses 
Django code and traces through several functions and classes. 

Brian Rosner has an interesting 
[short article](https://eldarion.com/blog/2013/02/14/entry-point-hook-django-projects/) 
about how to run code when Django starts. We will get back to the example later in this 
article.

### Django Code













