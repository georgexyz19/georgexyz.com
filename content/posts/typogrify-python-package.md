title: Typogrify Python Package
slug: typogrify-python-package
date: 2020-05-07 08:58
modified: 2020-05-07 08:58
tags: pelican, web development
note: Discuss typogrify python package
no: 43

Typogrify Python package is automatically called within Pelican when the setting 
`TYPOGRIFY` is true. The `typogrify` function is called in `Readers.read_file` 
method of `readers.py` file. The function acts as a filter and the code looks like 
this. 

```
content, metadata = read(filename)
if setting['TYPOGRIFY']:
    from typogrify.filters import typogrify
    content = typogrify(content)
    metadata['title'] = typogrify(metadata['title'])
    metadata['summary'] = typogrify(metadata['summary']) 
```

The `typogrify` function calls other 5 filters in the package: `amp`, `smartypants`, `caps`, 
`initial_quotes`, and `widont`. 
[The documentation](https://github.com/mintchaos/typogrify) 
on github is clear on what `amp`, `caps`, and `initial_quotes` do. 

The `smartypants` filter is the most important one in `Typogrify` package. It is a 
separate Python package, which is a port of SmartyPants 
Perl program written by John Gruber (who is known as the inventor of the Markdown language). 
The `smartypants` [documentation on github](https://github.com/leohemsted/smartypants.py) 
has information on how to use the Python package. 
The documentation on John Gruber's website is more clear on what the program does. 

> SmartyPants can perform the following transformations:
> 
> - Straight quotes (<code>"</code> and<code>'</code>) into "curly" quote HTML entities
> - Backticks-style quotes (<code>``</code>like this<code>''</code>) into "curly" quote HTML entities
> - Dashes ("<code>--</code>" and "<code>---</code>") into en- and em-dash entities
> - Three consecutive dots ("<code>...</code>") into an ellipsis entity


The `widont` filter is also interesting. It is "based on Shaun Inman's PHP utility 
of the same name, replaces the space between the last two words in a string with 
<code>&</code><code>nbsp;</code> to avoid a final line of text with only one word". 
I do not need this filter for this blog site, so I write a short Pelican plugin to remove 
the `widont` filter. Here is the code. 

```
from pelican import logger
from pelican import signals

from typogrify import filters
from typogrify.filters import process_ignores, applyfilters

def init_rmwidont(sender):
    logger.debug('Init rmwidont Plugin')

def register():
    signals.initialized.connect(init_rmwidont)

    def typogrify(text, ignore_tags=None):
        section_list = process_ignores(text, ignore_tags)
        rendered_text = ""
        for text_item, should_process in section_list:
            if should_process:
                rendered_text += applyfilters(text_item)
            else:
                rendered_text += text_item
        ## Remove widont here 
        return rendered_text # widont(rendered_text)

    filters.typogrify = typogrify

```


