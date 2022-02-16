title: Wsgiref Module
slug: wsgiref-module
date: 2022-02-14 00:15
modified: 2022-02-14 00:15
tags: WSGI
note: wsgi module code
related_posts: understand-wsgi-interface-in-flask, django-WSGI, http-module
no: 82

I have written two posts regarding `wsgi` interface before, but I still have questions.  
This post discusses the `wsgiref` module in the Python standard library. 
To quote the python standard documentation,

> The Web Server Gateway Interface (WSGI) is a standard interface between web server
> software and web applications written in Python. Wsgiref module contains WSGI utilities 
> and a reference server implementation.

### Source Code

The source code of the module is in this directory. 

```
~/.pyenv/versions/3.9.7/lib/python3.9/wsgiref
```

The statistics of the files is shown below. 

```
$ find . -maxdepth 1 -name '*.py' -exec wc -l '{}' + | sort -n
   23 ./__init__.py
  165 ./simple_server.py
  172 ./util.py
  184 ./headers.py
  441 ./validate.py
  571 ./handlers.py
 1556 total
```

The files are not long, and the total line count is only 1,556.  The code 
in the `simple_server.py` is dependent on the classes in `http.server` module. 
We will have difficulty to understand it if we haven't read `http` module. 
The `__init__.py` file only contains a doc string, and it does not have 
any code in it. 

### Simple Server Module 

The `simple_server` module is quite interesting. It is only 165 lines long, but 
it it the heart of the whole `wsgiref` module. The module defines a `demo_app` 
function, which is similar to a `hello_world` app in the `get_started.py` discussed 
in my first WSGI post. The main part of the module is also interesting, and the 
code is shown below. 

```
if __name__ == '__main__':
    with make_server('', 8000, demo_app) as httpd:
        sa = httpd.socket.getsockname()
        print("Serving HTTP on", sa[0], "port", sa[1], "...")
        import webbrowser
        webbrowser.open('http://localhost:8000/xyz?abc')
        httpd.handle_request()  # serve one request, then exit
```

The `with` statement sets up a server `httpd`, then it imports `webbrowser` module 
and opens a link. It is the same as sending a `GET` request to the server, then 
it calls `handle_request` method of the server to handle the request. 
The `demo_app` is passed as an argument to the `make_server` call, and it 
becomes parts of the server. 

The three classes defined in the module are relatively easy to understand. The 
`WSGIServer` derives from `HTTPServer` and works as the server. The `WSGIRequestHandler` 
class derives from `BaseHTTPRequestHandler` class and overrides its `handle` 
method. That's the method where the WSGI app is called. It initializes a 
`ServerHandler` instance and calls its `run` method. The `ServerHandler` 
class is derived from `SimpleHandler` class, which is defined in the 
`wsgi.handler` module. 

```
def handle(self):
    """Handle a single HTTP request"""

    self.raw_requestline = self.rfile.readline(65537)
    if len(self.raw_requestline) > 65536:
        self.requestline = ''
        self.request_version = ''
        self.command = ''
        self.send_error(414)
        return

    if not self.parse_request(): # An error code has been sent, just exit
        return

    handler = ServerHandler(
        self.rfile, self.wfile, self.get_stderr(), self.get_environ(),
        multithread=False,
    )
    handler.request_handler = self      # backpointer for logging
    handler.run(self.server.get_app())
```

### Handlers Module

The `wsgi.handlers` module defines the `BaseHandler` and `SimpleHandler` classes. 
The two classes run the `wsgi` app to handle an http request. The `run` method of 
`BaseHandler` class can be regarded as the entry point. If we ignore exception 
handling code, the method looks like this, 

```
# remove exception handling code
def run(self, application):
    self.setup_environ()
    self.result = application(self.environ, self.start_response)
    self.finish_response()
```

The `setup_environ` method is to setup the environment for one request. The 
`application` is the `wsgi` app which could be a function or an entry point 
to a web framework like Flask.  The second argument to the `application` is 
`self.start_response`, which is a method defined in the same class. The 
`finish_response` call does the actual work of transmitting the http response 
back to the client. 

Let's look at the `start_response` method first. The code is actually very 
simple if we ignore the exception handling code. The method assigns two 
instance variables `status` and `headers`, which are used later in other 
methods. The `headers_class` is `Headers` class defined in the `headers.py`. 

```
# exception handling code removed
def start_response(self, status, headers,exc_info=None):
    """'start_response()' callable as specified by PEP 3333"""

    if exc_info:
        ...

    self.status = status
    self.headers = self.headers_class(headers)
    status = self._convert_string_type(status, "Status")

    return self.write
```

The `finish_response` method sends the response back to the client. It 
calls the `write` and `finish_content` methods. The `write` method in 
turn calls `send_headers`, which calls `send_preamble` and `_write`. 
The methods have status checks.  If a header is already sent, it won't 
be sent again.  The `finish_response` method has the following code, which 
shows how the return value of the wsgi application is handled by the server. 

```
# exception handling code removed
def finish_response(self):
    try:
        if not self.result_is_file() or not self.sendfile():
            for data in self.result:
                self.write(data)
            self.finish_content()
```

That's basically how the wsgi server works. The `wsgiref` code is 
well written and easy to read. 

The `util.py` file defines some helping class and functions for other 
modules. The `validate.py` file defines a `validator` middleware which 
can check WSGI compliancy.  The doc string of the function says this, 

> This middleware does not modify the request or response in any
> way, but will raise an AssertionError if anything seems off

### Test POST Method

The `wsgi` demo app doesn't have code to handle POST request. 
Let's see what happens if we send the serve a POST request. 
This is the `wsgi` app from the `wsgiref` documentation page. 

```
# hello_wsgi.py
from wsgiref.simple_server import make_server

def hello_world_app(environ, start_response):
    status = '200 OK'  # HTTP Status
    headers = [('Content-type', 'text/plain; charset=utf-8')] 
    start_response(status, headers)

    # The returned object is going to be printed
    return [b"Hello World\n"]

with make_server('', 8080, hello_world_app) as httpd:
    print("Serving on port 8080...")

    # Serve until process is killed
    httpd.serve_forever()
```

We can run the app with bash command `python hello_wsgi.py`.  On 
anther terminal window, send a POST request with `curl`. 

```
$curl -v -d "param1=value1&param2=value2" -X POST http://localhost:8080/
```

Here is the response from the server. 

```
Note: Unnecessary use of -X or --request, POST is already inferred.
*   Trying 127.0.0.1:8080...
* Connected to localhost (127.0.0.1) port 8080 (#0)
> POST / HTTP/1.1
> Host: localhost:8080
> User-Agent: curl/7.74.0
> Accept: */*
> Content-Length: 27
> Content-Type: application/x-www-form-urlencoded
> 
* upload completely sent off: 27 out of 27 bytes
* Mark bundle as not supporting multiuse
* HTTP 1.0, assume close after body
< HTTP/1.0 200 OK
< Date: Tue, 15 Feb 2022 15:19:37 GMT
< Server: WSGIServer/0.2 CPython/3.9.7
< Content-type: text/plain; charset=utf-8
< Content-Length: 12
< 
Hello World
* Closing connection 0

```

The server doesn't care if it is a GET or POST request. It simply 
sends the same response back.  The request method info is saved 
in the `environ` variable with the key `REQUEST_METHOD`, but the 
wsgi app doesn't use this info for the above example. 

