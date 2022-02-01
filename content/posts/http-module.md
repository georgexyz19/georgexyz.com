title: Http Module
slug: http-module
date: 2022-01-31 16:00
modified: 2022-01-31 16:00
tags: python
note: Http Module
no: 80

Python `http` module is "a package that collects several modules for working with 
the HyperText Transfer Protocol".  The module is a middle level module that sits 
between low level `socket` and high level `urllib` modules. It is relatively simpler 
than the other two modules.  

I can't find many documentation for the http module.  The standard library 
has one page for each file in this package. The *Python 3 Module of the Week* 
site has two pages for http.server and http.cookies. 

[HTTP Modules - Python Docs](https://docs.python.org/3/library/http.html)

[http.server on Pymotw](https://pymotw.com/3/http.server/index.html)

[http.cookies on Pymotw](https://pymotw.com/3/http.cookies/index.html)

### Source Code 

The files are saved in this directory. 

```
~/.pyenv/versions/3.9.7/lib/python3.9/http
```

The module has five files and the statistics of the files are shown below.

```
$ find . -maxdepth 1 -name '*.py' -exec wc -l '{}' + | sort -n
   149 ./__init__.py
   612 ./cookies.py
  1295 ./server.py
  1519 ./client.py
  2113 ./cookiejar.py
  5688 total
```

Those modules appear to have different authors so they are loosely related. 
The `__init__.py` module defines an `HTTPStatus` class which "defines 
a number of HTTP status codes, reason phrases and long descriptions".  

### Http Server Module

The http.server can be invoked directly on the command line.  We can setup 
a simple http server via this command serving the current directory. 

```
python -m http.server 8080
```

In the web browser we can access a static website by typing the address 
`http://localhost:8080/`.  The http server will start serving the 
`index.html` file of a website.

The command will invoke the `server.py` script and start a server.  The 
code after the `... = '__main__':` line starts running.  The code looks 
like the concept shown below. 

```
# concept code

addr = (host, port)
with DualStackServer(addr, SimpleHTTPRequestHandler) as httpd:
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print('...')
        sys.exit(0)
```

The `DualStackSever` is derived from `ThreadingHTTPServer`, which is 
in turn derived from HTTPServer.  The whole hierarchy of the classes is 
shown below. 

```
socketserver.BaseServer
    socketserver.TCPServer
        HTTPServer
            ThreadingHTTPServer
                DualStackServer

socketserver.ThreadingMixIn
    ThreadingHTTPServer
```

The `http.server` module is closer to the `socketserver` module than 
other modules in the `http` package. 

The `serve_forever` command can be thought as the entry point of the 
module. It is defined in the `BaseServer` class of the `socketserver` 
module. The code is shown below. 

```
# serve_forever method in BaseServer

def serve_forever(self, poll_interval=0.5):
    """Handle one request at a time until shutdown.

    Polls for shutdown every poll_interval seconds. Ignores
    self.timeout. If you need to do periodic tasks, do them in
    another thread.
    """
    self.__is_shut_down.clear()
    try:
        # XXX: Consider using another file descriptor or connecting to the
        # socket to wake this up instead of polling. Polling reduces our
        # responsiveness to a shutdown request and wastes cpu at all other
        # times.
        with _ServerSelector() as selector:
            selector.register(self, selectors.EVENT_READ)

            while not self.__shutdown_request:
                ready = selector.select(poll_interval)
                # bpo-35017: shutdown() called during select(), 
                #     exit immediately.
                if self.__shutdown_request:
                    break
                if ready:
                    self._handle_request_noblock()

                self.service_actions()
    finally:
        self.__shutdown_request = False
        self.__is_shut_down.set()
```

The `serve_forever` method uses the selector module. The `register` method is 
called only once here, so the selector only have one server socket registered. 
The selector does not include client sockets. I haven't seen code like this in 
other places. The method then calls `_handle_request_noblock`, which in turn 
calls other methods in `BaseServer` and `TCPServer` classes. The `self.socket` 
shown below is a network socket initialized in `__init__` method of `TCPServer` class. 
The `request` variable is normally named `conn` or `connection` which is a 
client socket. 

```
# concept code in _handle_request_noblock, simplified

request, client_address = self.socket.accept() 
self.RequestHandleClass(request, client_address, self)
request.close()
```

The `RequestHandler` class also has a hierarchy. Two of the classes 
are defined in the `socketserver` module and other two are defined in 
the `http.server` module. Those four classes are well organized. 

```
socketserver.BaseRequestHandler
    socketserver.StreamRequestHandler
        BaseHTTPRequestHandler
            SimpleHTTPRequestHandler
```

Here is the code in the `__init__` method of `BaseRequestHandler` class. 

```
    def __init__(self, request, client_address, server):
        self.request = request
        self.client_address = client_address
        self.server = server
        self.setup()
        try:
            self.handle()
        finally:
            self.finish()
```

The `setup` method is defined in the `StreamRequestHandler` class. It 
sets up two file streams `rfile` and `wfile` on the client socket, and 
derived classes can use those two streams to accept request from client 
and write response to the client. 

The `rfile` is the return value of the `makefile` call on the socket. 
The `wfile` is a class `_SocketWrite` object which derives from 
`BufferedIOBase` class, and it has a method `write` which calls 
`sendall` method of the socket. So those classes are all built on 
top of the `socket` module. 

The `handle` method in `BaseHTTPRequestHandler` class calls the 
`handle_one_request` method. It in turn calls `parse_request` 
method and `method`.  The `parse_request` will parse the first 
line of the request (e.g., "GET / HTTP/1.1") and the HTTP headers. 
The `method` refers to one of the methods defined in `SimpleHTTPRequestHandler` 
class such as `do_GET` and `do_HEAD`.  The `do...` method will 
write to the `wfile` stream and send the response back. 
The `SimpleHTTPRequestHandler` does not define a `do_POST` method, 
so it can't handle any POST method. 

That's basically how the `http.server` handles a request. 

### Http Client Module

The `http.client` module "defines classes implement the client side of the 
HTTP and HTTPS protocols".  The documentation says that "it is normally not 
used directly" and implies that `urllib` is recommended. Here is an example 
on how to use the module. 

```
conn = http.client.HTTPSConnection('www.python.org')
conn.request('GET', '/')
resp = conn.getresponse()
print(resp.status, resp.reason)
data = resp.read()  # return content in a byte string
```

If you already read the `http.server` module code, the source code in this 
module is not difficult to understand. The `request` method will call the 
`_send_request` method of the `HTTPConnection` class, which in turn calls
`putrequest`, `putheader`, and `endheaders` methods.  The `send` method 
of the class calls `sendall` method of the socket to actually transfer 
the request. 

The `getresponse` method creates an instance of the `HTTPResponse` class, 
calls the `begin` method, and returns the instance. Then we can call 
the `read` method on the instance to get the actual HTTP response. 

### Http Cookies and Cookiejar

The http `cookies` module is relatively independent from 
other modules.  The `cookies.py` module only imports three standard modules, 
re, string, and types.  It defines `Morsel`, `BaseCookie`, and `SimpleCookie` 
classes. The examples in the Python documentation do not show how to 
use this module with other server or client module. 

The http `cookiejar` module defines a `Cookie` class and `CookieJar` and 
`FileCookieJar` classes. This `Cookie` class is not related to the `SimpleCookie` 
class. The examples on Python documentation shows how to use this module 
with the `urllib` module. 

### Conclusion

I spent quite some time reading the `http` module source code and trying to 
understand how they work. The code is a good resource for studying Python 
network related topics. 




