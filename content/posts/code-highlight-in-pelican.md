title: Code Highlighting in Pelican
slug: code-highlight-in-pelican
date: 2020-05-22 16:49
modified: 2020-05-22 16:49
tags: pelican
note: Discuss CodeHilite/Pygments etc. along with Pelican.
no: 47

It is easy getting confused about code highlighting when reading Pelican 
documentation. It mentions keywords like `CodeHilite` and `Pygments` without 
much explanation. When I am reviewing my Pelican notes, I decide to 
spend a little time to figure out how code highlighting works in Pelican or 
more broadly in Python. 

The `CodeHilite` is an extension for Python package `Markdown`. When you run 
the command `pip install markdown`, the installed package includes the 
`CodeHilite` because it is a standard `Markdown` extension. Confusing enough, 
the documentation for `Markdown` package calls itself `Python-Markdown`. You 
can see the documentation for `CodeHilite` on 
[this webpage](https://python-markdown.github.io/extensions/code_hilite/). 
The summary says that "the CodeHilite extension adds code/syntax highlighting 
to standard Python-Markdown code blocks using Pygments." It is still not very 
clear on what it actually does. 

On the same documentation page, there are two example `Pygments` commands from 
the command line. 

```
pygmentize -S default -f html -a .codehilite > styles.css
pygmentize -L style
```

The first command creates a CSS file `styles.css` with `default` style.  The 
`-f html` option specifies the formatter and `-a .codehilite` option specifies 
a class in the `styles.css` file. The second command lists all the styles 
that comes with `Pygments` package. 

After running the first command, the generated `styles.css` file has 69 lines of 
CSS rules. The `.codehilite` class is specified by the `-a` option on the 
command line. 

```css
.codehilite .hll { background-color: #ffffcc }
.codehilite  { background: #f8f8f8; }
.codehilite .c { color: #408080; font-style: italic } /* Comment */
.codehilite .err { border: 1px solid #FF0000 } /* Error */
.codehilite .k { color: #008000; font-weight: bold } /* Keyword */
...
```

The Pelican default configuration dictionary has a key `MARKDOWN`, and the 
corresponding value is shown below. 

```python
'MARKDOWN': {'extension_configs': 
    {'markdown.extensions.codehilite': 
        {'css_class': 'highlight'},
     'markdown.extensions.extra': {},
     'markdown.extensions.meta': {}},
```

It specifies a default CSS class value `highlight`. The Python `Markdown` 
package transforms code block in a markdown file to html segment like below. 
The `CodeHilite` plugin does the work, and it actually calls the `Pygments` 
package to generate the html code. Specifically, Line 122 of the `CodeHilite` 
plugin source code file 
[codehilite.py](https://github.com/Python-Markdown/markdown/blob/master/markdown/extensions/codehilite.py) 
calls `highlight` function in the `Pygments` package. 

```html
<div class="highlight">
  <pre>
    <code>
      <span class="k">if</span> 
      <span class="vm">__name__</span> 
      ...
    </code>
  </pre>
</div>
```

The html template should link to the `styles.css` file discussed earlier in 
the article, so the generated html code section has the specified CSS styles. 
If you use default Pelican configuration, the `-a .codehilite` option of the 
first pygmentize command should be `-a highlight`. 

It is also interesting to find that the `Markdown` Python package does not 
list `Pygments` package as a dependent, 
while `Pelican` itself lists `Pygments` as a dependent. If you use pipenv 
manage virtual environment, the command `pipenv graph` lists dependent packages
as follows. 

```
Markdown==3.2.1
  - setuptools [required: >=36, installed: 46.1.3]
pelican==4.2.0
  - blinker [required: Any, installed: 1.4]
  - docutils [required: Any, installed: 0.16]
  - feedgenerator [required: >=1.9, installed: 1.9.1]
    - pytz [required: >=0a, installed: 2020.1]
    - six [required: Any, installed: 1.14.0]
  - jinja2 [required: >=2.7, installed: 2.11.2]
    - MarkupSafe [required: >=0.23, installed: 1.1.1]
  - pygments [required: Any, installed: 2.6.1]
  - python-dateutil [required: Any, installed: 2.8.1]
    - six [required: >=1.5, installed: 1.14.0]
  - pytz [required: >=0a, installed: 2020.1]
  - six [required: >=1.4, installed: 1.14.0]
  - unidecode [required: Any, installed: 1.1.1]
...
```

This page has five code sections, and you can see code highlighting 
effects in the middle three sections. 