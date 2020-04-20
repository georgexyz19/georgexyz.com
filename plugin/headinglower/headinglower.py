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
                # Revise here, comment out ( - 1 )
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
