==============================
Pelican Source Code and Plugin
==============================

:slug: pelican-source-code-plugin
:date: 2020-04-19 22:08
:modified: 2020-04-19 22:08
:tags: python, pelican
:meta: Show how to write pelican plugin for rst files
:note: pelican source code and plugin
:no: 37

Articles on this website before this one are all written in markdown format. I want to 
write some articles in reStructuredText (rst) format but the default :code:`docutils` tool 
that comes with Pelican has a flaw causing me to stay away from the rst format.  

The problem is that the top title of an aritle (e.g. "Pelican Source Code and Plugin" 
on this page) is rendered as :code:`h2` html tag, and section title (e.g. "Pelican Plugin" 
section below) starts with :code:`h3` tag. It is designed this way since the start of the website. 
In a markdown file, I can add two :code:`#` to specify a title as :code:`h2`.  There is 
no easy way to specify the heading levels in rst files. 

The same problem is described in this question_ on github.

.. _question: https://github.com/github/markup/issues/567

Pelican Plugin
==============

When I am reading Pelican source code, I find that the Pelican class in the 
:code:`__init__.py` file has an :code:`init_plugins` method. This method calls each plugin's  
register function as shown below. 


.. code-block:: python

    def init_plugins(self):
        self.plugins = []
        ......
        for plugin in self.settings['PLUGINS']:
            .....
            plugin.register()
            self.plugins.append(plugin)

The Pelican plugin page has an existing plugin :code:`headerid` which implements a similar 
function.  It adds anchor tags to headings in rst files. 

Override Docutils Method
========================

Google searching class names 
in the :code:`headerid` plugin lead me to a very nice article 
`reStructureText(RST) Tutorial <https://www.devdungeon.com/content/restructuredtext-rst-tutorial-0>`_. 
This article discusses the exact same heading problem I have with the rst format and 
has code examples on how to solve it.  It becomes easy for me to modify the code in 
this article to a Pelican plugin which is very similar to :code:`headerid`.  I name this new 
Pelican plugin :code:`headinglower` which lowers the heading levels in rst files. 

Headinglower Code
-----------------

The :code:`headinglower` plugin has two files. The :code:`__init__.py` file only has one line of code.   

.. code-block:: python

    # __init__.py 
    from .headinglower import *

The :code:`headinglower.py` file has the following code. 

.. code-block:: python

    # headinglower.py
    from pelican import readers, logger
    from pelican.readers import PelicanHTMLTranslator
    from pelican import signals
    from docutils import nodes

    def init_headinglower(sender):
        logger.debug('Init Headinglower Plugin')

    def register():
        signals.initialized.connect(init_headinglower)

        class ModPelicanHTMLTranslator(PelicanHTMLTranslator):
            def visit_title(self, node):
                """Only 6 section levels are supported by HTML."""
                close_tag = '</p>\n'
                if isinstance(node.parent, nodes.topic):
                    self.body.append(
                        self.starttag(node, 'p', '', CLASS='topic-title'))
                elif isinstance(node.parent, nodes.sidebar):
                    self.body.append(
                        self.starttag(node, 'p', '', CLASS='sidebar-title'))
                elif isinstance(node.parent, nodes.Admonition):
                    self.body.append(
                        self.starttag(node, 'p', '', CLASS='admonition-title'))
                elif isinstance(node.parent, nodes.table):
                    self.body.append(
                        self.starttag(node, 'caption', ''))
                    close_tag = '</caption>\n'
                elif isinstance(node.parent, nodes.document):
                    self.body.append(self.starttag(node, 'h1', '', CLASS='title'))
                    close_tag = '</h1>\n'
                    self.in_document_title = len(self.body)
                else:
                    assert isinstance(node.parent, nodes.section)
                    ## revise here, comment out ( - 1 )
                    h_level = self.section_level + self.initial_header_level # - 1
                    atts = {}
                    if (len(node.parent) >= 2 and
                        isinstance(node.parent[1], nodes.subtitle)):
                        atts['CLASS'] = 'with-subtitle'
                    self.body.append(
                        self.starttag(node, 'h%s' % h_level, '', **atts))
                    atts = {}
                    if node.hasattr('refid'):
                        atts['class'] = 'toc-backref'
                        atts['href'] = '#' + node['refid']
                    if atts:
                        self.body.append(self.starttag({}, 'a', '', **atts))
                        close_tag = '</a></h%s>\n' % (h_level)
                    else:
                        close_tag = '</h%s>\n' % (h_level)
                self.context.append(close_tag)

        readers.PelicanHTMLTranslator = ModPelicanHTMLTranslator

The code add a method :code:`visit_title` to the PelicanHTMLTranslator class.  It overrides a method  
defined in :code:`HTMLTranslator` class of docutils.writers._html_base module. 

Plugin Settings
---------------

Add the following settings to the :code:`pelicanconf.py`, the Pelican will automatically load the 
plugin. 

.. code-block:: settings

    PLUGIN_PATHS = ['plugin/', ]
    PLUGINS=['headinglower',]

Better Way
==========

The above method works well and solves my problem.  But there is a better and easier 
way to solve the exact problem.  Pelican has over 100 settings, and one 
of them is :code:`DOCUTILS_SETTINGS`.  It is described on the documentation_ page as:

    Extra configuration settings for the docutils publisher (applicable only to 
    reStructuredText). See Docutils Configuration settings for more details.

The :code:`RstReader` class in :code:`readers.py` file of Pelican source code has a method 
:code:`_get_publisher`. It has the following lines of code. 

.. code-block:: python

    extra_params = {'initial_header_level': '2',
                        'syntax_highlight': 'short',
                        'input_encoding': 'utf-8',
                        'language_code': self._language_code,
                        'halt_level': 2,
                        'traceback': True,
                        'warning_stream': StringIO(),
                        'embed_stylesheet': False}

    user_params = self.settings.get('DOCUTILS_SETTINGS')
    if user_params:
        extra_params.update(user_params)

I can simply set the :code:`initial_header_level` value to 3 and the problem is solved. 
Add the following settings in the :code:`pelicanconf.py`, the first section title heading will 
become :code:`h3`.  Note the article title heading level :code:`h2` is actually set in the 
:code:`article.html` template file. I also comment out the two plugin settings 
shown in the previous section.   

.. code-block:: settings

    DOCUTILS_SETTINGS = {'initial_header_level': '3', }

.. _documentation: https://docs.getpelican.com/en/stable/settings.html

Rst File of This Article
========================

The rst file of this article is available on github. `Click here`_ to read the source file and click 
"Raw" button to see the text file. 

.. _Click here: https://github.com/georgexyz19/georgexyz.com/blob/master/content/posts/pelican-source-code-plugin.rst
