title: Django Messages Contrib App
slug: django-messages
meta: This post discusses django messages contrib app
date: 2019-07-15 11:25
modified: 2019-07-15 11:25
tags: django
note: this note is based on a previous hard copy note 2/25/19
no: 18


Django messages app is used to "display one-time notification message to the 
user after processing a form or some other types of user input." Django 
official documentation has a page 
[the messages framework](https://docs.djangoproject.com/en/2.2/ref/contrib/messages/) 
for the app. 

### How to Use Messages App

Chapter 11 of *Django Unleashed* book utilizes the app to convey a message 
that an email has been successfully sent. The code is easy to understand. 
The view adds a success message to the message queue. The next web page 
(redirected page `blog_post_list`) will show the message.

```python
# contact/views.py

...
from django.contrib.messages import success

class ContactView(View):
    ....

    def post(self, request):
        bound_form = self.form_class(request.POST)
        if bound_form.is_valid():
            mail_sent = bound_form.send_email()
            if mail_sent:
                success(request, 'Email successfully sent.')  # <------
                return redirect('blog_post_list')             # <------
        return render(request, self.template_name, 
                      {'form': bound_form } )
```

The code to show the messages is in the base.html file, and all web pages 
extended from the base.html will show the messages. 

```html
<ul>
  {% for message in messages %}
    {% if message.tags %}
    <li class="{{ message.tags }}">
    {% else %}
    <li>
    {% endif %}
    {{ message }}</li>
  {% endfor %}
</ul>
```

The code above is very similar to the code shown on the Django official 
documentation page (shown below). 

```
{% if messages %}
<ul class="messages">
    {% for message in messages %}
    <li{% if message.tags %} class="{{ message.tags }}"{% endif %}>
      {{ message }}</li>
    {% endfor %}
</ul>
{% endif %}
```

### Source Code Files

The source code for the messages app is in the django/contrib/messages directory. 
It consists of 13 python files, and the total line count is 647 in Django 2.2.2.

```bash
george@STK2M3:~$ find . -name '*.py' -exec wc -l {} +
   26 ./middleware.py
    4 ./__init__.py
   21 ./constants.py
   96 ./api.py
   18 ./views.py
   13 ./context_processors.py
   12 ./utils.py
    7 ./apps.py
  170 ./storage/base.py       #  <----- backend storage
   12 ./storage/__init__.py
   48 ./storage/session.py
  166 ./storage/cookie.py
   54 ./storage/fallback.py
  647 total
```

### Messages App API

The \_\_init\_\_.py file imports all from api.py and constants.py. The api.py 
file defines the API of the messages app, which includes those functions:

* add\_message
* get\_message
* get\_level
* set\_level
* debug, info, warning, success, and error (call add\_message)

The functions shows that the attribute `_message` of request is the message 
storage.

The constants.py defines a few constants:

```python
# messages/constants.py

DEBUG = 10
INFO = 20
SUCCESS = 25
WARNING = 30
ERROR = 40

DEFAULT_TAGS = {
    DEBUG: 'debug',
    INFO: 'info',
    SUCCESS: 'success',
    WARNING: 'warning',
    ERROR: 'error',
}

DEFAULT_LEVELS = {
    'DEBUG': DEBUG,
    'INFO': INFO,
    'SUCCESS': SUCCESS,
    'WARNING': WARNING,
    'ERROR': ERROR,
}
```

The middleware.py code is an good example of how to write a middleware for 
Django. The class derives from MiddlewareMixin and defines two methods 
`process_request` and `process_response`.  The `process_request` adds 
`_messages` attribute to the request and `process_response` stores the messages 
by calling `update` method of `_message` and raises an exception if messages 
are not all stored.

```python
# messages/middleware.py

from django.conf import settings
from django.contrib.messages.storage import default_storage
from django.utils.deprecation import MiddlewareMixin


class MessageMiddleware(MiddlewareMixin):
    """
    Middleware that handles temporary messages.
    """

    def process_request(self, request):
        request._messages = default_storage(request)

    def process_response(self, request, response):
        """
        Update the storage backend (i.e., save the messages).

        Raise ValueError if not all messages could be stored and DEBUG is True.
        """
        # A higher middleware layer may return a request which does not contain
        # messages storage, so make no assumption that it will be there.
        if hasattr(request, '_messages'):
            unstored_messages = request._messages.update(response)
            if unstored_messages and settings.DEBUG:
                raise ValueError('Not all temporary messages could be stored.')
        return response
```

The context\_processor.py defines a function `messages` which simply returns a 
dictionary of two context variables.

```python
# messages/context_processor.py 

from django.contrib.messages.api import get_messages
from django.contrib.messages.constants import DEFAULT_LEVELS


def messages(request):
    """
    Return a lazy 'messages' context variable as well as
    'DEFAULT_MESSAGE_LEVELS'.
    """
    return {
        'messages': get_messages(request),
        'DEFAULT_MESSAGE_LEVELS': DEFAULT_LEVELS,
    }
```

The `views.py` defines a SuccessMessageMixin, which adds a success message 
attribute to class based views. It is probably easier for a programmer 
to call `success` API method directly to add a message. 

The `utils.py` file defines a `get_level_tags` function which returns a 
dictionary of level tags. 

### Messages Backend Storage

The interesting part of the messages app is its storage. The \_\_init\_\_.py in 
the storage defines a `default_storage` function. 

```python
# messages/storage/__init__.py

from django.conf import settings
from django.utils.module_loading import import_string


def default_storage(request):
    """
    Callable with the same interface as the storage classes.

    This isn't just default_storage = import_string(settings.MESSAGE_STORAGE)
    to avoid accessing the settings at the module level.
    """
    return import_string(settings.MESSAGE_STORAGE)(request)
```

The grep command results show that `MESSAGE_STORAGE` is assigned FallBackStorage 
class which is defined in fallback.py file. 

```
george@STK2M3:~/Desktop/django-2.2.2$ grep -nr 'MESSAGE_STORAGE' ./
./django/contrib/messages/storage/__init__.py:9: 
   This isn't just default_storage = import_string(settings.MESSAGE_STORAGE)
./django/contrib/messages/storage/__init__.py:12: 
   return import_string(settings.MESSAGE_STORAGE)(request)
./django/conf/global_settings.py:554:MESSAGE_STORAGE = 
   'django.contrib.messages.storage.fallback.FallbackStorage'
```

The `import_string` function is defined in the module\_loading.py file, which 
"imports a dotted module path and return the attribute/class designated by the 
last name in the path."

The base.py file defines Message class, which has three attributes: 
level, message, and extra\_tags. It also defines BaseStorage class, 
which is an abstraction of messages storage.  Two methods of the class `_get` 
and `_store` are placeholders and they must be overridden. 

To understand code in the BaseStorage class, we need to think about 
how an Message object is instantiated, stored, and retrieved. Here are the 
steps in which methods in BaseStorage are called. 

1. A request comes to Django. Messages middleware initializes a default_storage
   backend and assigns it to the `_messages` attribute of request.
2. The `add_message` method of message API is called. It calls the add method in 
   BaseStorage, which changes `added_new` attribute to `True` and append the 
   message into the `_queued_messages` list. 
3. The view function does not call the template render function. The 
   `__iter__` method of BaseStorage is not called.
4. The `process_response` method of middleware class calls `update` method of 
   BaseStorage, which stores unread messages. They are stored in client's 
   browser storage, not on the server.
5. A new request comes in, Django does the same as step 1.
6. The view function calls the template `render` method, which calls the 
   `__iter__` method of BaseStorage.  It changes `used` attribute to `True`. 
   The `_queued_messages` is empty at this time, and it is not the 
   same object described in step 2. It then calls `_loaded_messages` property 
   and calls `_get` method to retrieve the stored message from client's browser 
   storage.
7. The `process_response` method of middleware class calls `update` method 
   of BaseStorage. In this case the `_queued_messages` list is empty, and 
   nothing is stored. 

The logic in the `update` method of BaseStorage is smart. If two consecutive 
requests add two messages without displaying them, both messages will be 
stored. Here is the source code. 

```python
# update method of BaseStorage class
def update(self, response):
    """
    Store all unread messages.

    If the backend has yet to be iterated, store previously stored messages
    again. Otherwise, only store messages added after the last iteration.
    """
    self._prepare_messages(self._queued_messages)
    if self.used:
        return self._store(self._queued_messages, response)  # normally empty
    elif self.added_new:
        messages = self._loaded_messages + self._queued_messages
        return self._store(messages, response)
```

### Cookies and Sessions

The discussion of the messages app has already became convoluted, and it will 
become even more complicated when we examine how Cookies and Sessions work. 
I will have a general dicussion on Cookies and Sessions and stop here.  It will 
be in another post to have a detailed discussion of those topics. 

Internet cookies is "a small piece of data sent from a web server and stored 
on the user's computer".  The 
[wikipedia http cookie page](https://en.wikipedia.org/wiki/HTTP_cookie) 
provides a good overview of the topic. The cookie information is sent via the 
http header, which may have a size limit. The session cookie 
contains a unique session id, and the infomation is saved in server database. 
Django web framework also comes with a sessions contrib app.  Here is the link 
to the 
[official documentation](https://docs.djangoproject.com/en/2.2/topics/http/sessions/). 

The SessionStorage class does not need to consider the size limit when saving 
messages, so the code is simpler than in CookieStorage class.  Here is the 
source code of session.py file. 

```python
# messages/storage/session.py
import json

from django.conf import settings
from django.contrib.messages.storage.base import BaseStorage
from django.contrib.messages.storage.cookie import (
    MessageDecoder, MessageEncoder,
)


class SessionStorage(BaseStorage):
    """
    Store messages in the session (that is, django.contrib.sessions).
    """
    session_key = '_messages'

    def __init__(self, request, *args, **kwargs):
        assert hasattr(request, 'session'), "The session-based temporary "\
            "message storage requires session middleware to be installed, "\
            "and come before the message middleware in the "\
            "MIDDLEWARE%s list." % ("_CLASSES" if settings.MIDDLEWARE is None else "")
        super().__init__(request, *args, **kwargs)

    def _get(self, *args, **kwargs):
        """
        Retrieve a list of messages from the request's session. This storage
        always stores everything it is given, so return True for the
        all_retrieved flag.
        """
        return self.deserialize_messages(self.request.session.get(self.session_key)), True

    def _store(self, messages, response, *args, **kwargs):
        """
        Store a list of messages to the request's session.
        """
        if messages:
            self.request.session[self.session_key] = self.serialize_messages(messages)
        else:
            self.request.session.pop(self.session_key, None)
        return []

    def serialize_messages(self, messages):
        encoder = MessageEncoder(separators=(',', ':'))
        return encoder.encode(messages)

    def deserialize_messages(self, data):
        if data and isinstance(data, str):
            return json.loads(data, cls=MessageDecoder)
        return data
```

### Conclusion

The messages app is easier to use in a Django app, but the implementation of 
the app is not simple.  Reading the source code helps us understand how the 
Django web framework works.   



