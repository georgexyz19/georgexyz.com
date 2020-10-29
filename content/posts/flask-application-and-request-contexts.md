title: Flask Application And Request Contexts
slug: flask-application-and-request-contexts
date: 2020-10-29 09:13
modified: 2020-10-29 09:13
tags: flask, python
note: A short post about Flask application and request contexts
no: 57

Application and request contexts are one of the hard to understand concepts in Flask. 
They are easy for programmers to use, but they are not easy to understand. The 
implementation of those concepts is complicated. 

Patrick Kennedy wrote a long article on testdriven.io website regarding this topic. He 
also had a presentation on the same topic for FlaskCon2020.  Both article and 
presentation are very good. The article also discusses the request-response cycle 
in more details than other articles. 

Article - [Deep Dive into Flask's Application and Request Contexts](https://testdriven.io/blog/flask-contexts-advanced/)

Presentation on Youtube - [Demystifying Flask's Application and Request Contexts with pytest](https://www.youtube.com/watch?v=fq8y-9UHjyk&ab_channel=FlaskCon2020)

The article above needs some background knowledge on Python threading.  The realpython 
website has an excellent article on threading by Jim Anderson. The article covers most threading topics on the official Python threading documentation. 

Realpython.com - [An Intro to Threading in Python](https://realpython.com/intro-to-python-threading/)

Python.org - [Threading - Thread-based Parallelism](https://docs.python.org/3/library/threading.html#thread-local-data)

Above is what I have read on the topic.  I will continue to read articles and 
Flask source code in this topic and update the post. 


 

