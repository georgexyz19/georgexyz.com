title: ChatGPT Solves Programming Problem
slug: chatgpt-solves-programming-problem
date: 2025-05-04 23:03
modified: 2025-05-04 23:03
tags: ai
note: Use ChatGPT to solve an old python programming problem
no: 90

When I come across a well-written Python article online, I often print a copy and 
store it in a three-ring binder. Here is the link to an article I printed 
on 9/28/2021:

[Context Managers and the “with” Statement in Python](https://dbader.org/blog/python-context-managers-and-with-statement)

The article includes an example of a class-based context manager, structured like this:

```python
class Indent:
    def __init__(self):
        self.level = 0

    def __enter__(self):
        self.level += 1
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.level -=1

    def print(self, text):
        print('    ' * self.level + text)


with Indent() as indent:
    indent.print('hi!')
    with indent:
        indent.print('hello')
        with indent:
            indent.print('bonjour')
    indent.print('hey')
```

Near the end of the articles, the author Dan Bader suggests that "another 
good execise would be trying to refactor this code to be generator-based". 

I attempted to solve the problem twice before. On 1/3/2022, I wrote 
a note: "Don't know how—leave it for the future." Then, on 1/23/2023, 
I noted: "Still don’t know how to do it. It seems the class-based approach is easier."

When I revisited the article today, I asked ChatGPT to help me solve 
the problem. Here is the prompt I used:


> Here is a python program with class based context manager, can you 
> rewrite the context manager to be generator-based?

After I pasted in the code above, the answer (see below) came back almost immediately.
The code runs perfertly. I don't know how chatGPT did it, but it is magical!

```python
from contextlib import contextmanager

class Indent:
    def __init__(self):
        self.level = 0

    def print(self, text):
        print('    ' * self.level + text)

@contextmanager
def indent_context(indent):
    indent.level += 1
    try:
        yield indent
    finally:
        indent.level -= 1

# Usage
indent = Indent()
with indent_context(indent) as i:
    i.print('hi!')
    with indent_context(i):
        i.print('hello')
        with indent_context(i):
            i.print('bonjour')
    i.print('hey')
```

