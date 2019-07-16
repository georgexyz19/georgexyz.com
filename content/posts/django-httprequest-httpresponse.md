title: Django HttpRequest and HttpResponse
slug: django-httprequest-httpresponse
meta: This post discusses django HttpRequest and HttpResponse
date: 2019-07-11 23:45 
modified: 2019-07-11 23:45 
tags: django
note: this note is based on several notes.
no: 17


Django view "is simply a Python function that takes a web request and 
returns a response." A typical view function loads template, retrieves 
some data from database, and returns a response. Django 1.3 starts supporting 
class-based views, which makes writing views easier. The drawback is that 
the code is not as straightforward to understand as function-based view. 

Here is a typical Django view function from official Django tutorial. 

```python
def index(request):
    latest = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = { 'latest': latest }
    return HttpResponse(template.render(context, request))
```

The request object passed to the view function is a WSGIRequest object, and 
WSGIRequest is a subclass of HttpRequest.  When web browser sends an http/https
request to the web server, Django web framework receives the infomation in 
the form of an environ object, and creates the request object.  Yes, Django 
creates this object and passes it to the view function.  This is a 
typical example of *inversion of control*. A web app developer does not have
control over the flow of a program when using a web framework. 

The HttpRequest and HttpResponse classes are defined in the request.py and 
response.py files in http directory. The response.py file also defines 
several other classes such as Http404 and HttpResponseRedirect. 

The Django office documentation has 
[a reference page](https://docs.djangoproject.com/en/2.2/ref/request-response/) 
for HttpRequest and HttpResponse. It is probably to easier to read the source 
code directly. Here is a list of files in the http directory.

```

george@STK2M3:~/Desktop/django-2.2.2/django$ wc -l http/*.py
   26 http/cookie.py
   21 http/__init__.py
  688 http/multipartparser.py
  602 http/request.py
  559 http/response.py
 1896 total
```

How do I find this information? The grep command below shows that HttpRequest 
only appears a few places in Django source code. The wsgi.py file defines the 
WSGIRequst class as a subclass of HttpRequest. 

```
george@STK2M3:~/Desktop/django-2.2.2/django$ grep -r "HttpRequest" ./
./template/context.py:    Create a suitable Context from a plain dict ...
./core/handlers/base.py:        """Return an HttpResponse object for  ...
./core/handlers/wsgi.py:from django.http import HttpRequest, QueryDict, parse_cookie
./core/handlers/wsgi.py:class WSGIRequest(HttpRequest):    ++++++ Notice ++++
./core/files/uploadhandler.py:        >>> from django.http import HttpRequest
./core/files/uploadhandler.py:        >>> request = HttpRequest()
./views/decorators/debug.py:from django.http import HttpRequest
......
```

We can then try to find where the WSGIRequest object is defined and passed along 
to other functions as an argument. 

```
george@STK2M3:~/Desktop/django-2.2.2/django$ grep -rn "WSGIRequest" ./core
./core/management/commands/runserver.py:57:   # way to reach WSGIRequestHandler....
./core/handlers/wsgi.py:66:class WSGIRequest(HttpRequest):
./core/handlers/wsgi.py:131:    request_class = WSGIRequest
...
```

In the file wsgi.py line 131, it assigns WSGIRequest class to `request_class`. 
Let's try to find where `request_class` is instantiated. 

```
george@STK2M3:~/Desktop/django-2.2.2/django$ grep -rn "request_class" ./core
./core/handlers/wsgi.py:131:    request_class = WSGIRequest
./core/handlers/wsgi.py:140:        request = self.request_class(environ)
```

Grep command can also see the lines before and after the target line.  The command 
below shows the context code. 

```
george@STK2M3:~/Desktop/django-2.2.2/django$ grep -rn -C 5 "request_class" ./core
....
./core/handlers/wsgi.py-130-class WSGIHandler(base.BaseHandler):
./core/handlers/wsgi.py:131:    request_class = WSGIRequest
./core/handlers/wsgi.py-132-
./core/handlers/wsgi.py-133-    def __init__(self, *args, **kwargs):
./core/handlers/wsgi.py-134-        super().__init__(*args, **kwargs)
./core/handlers/wsgi.py-135-        self.load_middleware()
./core/handlers/wsgi.py-136-
./core/handlers/wsgi.py-137-    def __call__(self, environ, start_response):
./core/handlers/wsgi.py-138-        set_script_prefix(get_script_name(environ))
./core/handlers/wsgi.py-139-        signals.request_started.send(sender=self.__class__, environ=environ)
./core/handlers/wsgi.py:140:        request = self.request_class(environ)
./core/handlers/wsgi.py-141-        response = self.get_response(request)
./core/handlers/wsgi.py-142-
./core/handlers/wsgi.py-143-        response._handler_class = self.__class__
./core/handlers/wsgi.py-144-
./core/handlers/wsgi.py-145-        status = '%d %s' % (response.status_code, response.reason_phrase)
```

The wsgi.py line 141 `response = self.get_response(request)` is where 
the request is passed to the view function. It is also where the response created 
in the view function passed back to the Django. 
[The WSGI discussion]({filename}django-wsgi.md) 
clearly shows that the `environ` argument is the one passed on by the web 
server. 

"The `get_response` method is where nearly all of the activity happens." James 
Bennett's article 
[How Django processes a request](https://www.b-list.org/weblog/2006/jun/13/how-django-processes-request/) 
has a very detailed discussion on the topic. 

If you want to find out what information is contained in the reqeust object, the 
view function below displays the contents. 

```python
def display_meta(request):  # from django book
    values = request.META.items()
    values = sorted(values)
    html = []
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))

    txt = '<table>%s</table>' % ('\n'.join(html) )  # added by me
    txt += '<p>Number of items in META : ' + str(len(request.META)) + '</p>' 
    txt += '<p>request.path : ' + str(request.path) + '</p>' 
    txt += '<p>request.get_host() : ' + str(request.get_host()) + '</p>' 
    txt += '<p>request.get_full_path() : ' + str(request.get_full_path()) + '</p>' 
    txt += '<p>request.is_secure() : ' + str(request.is_secure()) + '</p>' 
    txt += '<p>request.method : ' + str(request.method) + '</p>' 
    txt += '<p>request.encoding : ' + str(request.encoding) + '</p>' 
    txt += '<p>request.content_type : ' + str(request.content_type) + '</p>' 
    print(type(request))  # for debug only
    return HttpResponse(txt)
```

Here is the partial output from the `display_meta` function:

```
......
XDG_SESSION_DESKTOP	cinnamon
XDG_SESSION_ID	c2
XDG_SESSION_PATH	/org/freedesktop/DisplayManager/Session0
XDG_SESSION_TYPE	x11
XDG_VTNR	7
_	/home/george/.venv/django/bin/python
wsgi.errors	<_io.TextIOWrapper name='' mode='w' encoding='UTF-8'>
wsgi.file_wrapper	
wsgi.input	
wsgi.multiprocess	False
wsgi.multithread	True
wsgi.run_once	False
wsgi.url_scheme	http
wsgi.version	(1, 0)

Number of items in META : 85
request.path : /info/
request.get_host() : 127.0.0.1:8000
request.get_full_path() : /info/
request.is_secure() : False
request.method : GET
request.encoding : None
request.content_type : text/plain

```


