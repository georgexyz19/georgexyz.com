from pelican import logger
from pelican import signals

from typogrify import filters

def init_mod_typogrify(sender):
    logger.debug('Init mod_typogrify Plugin')

def register():
    signals.initialized.connect(init_mod_typogrify)

    def smartypants(text):
        """Applies smarty pants to curl quotes.
    
        >>> smartypants('The "Green" man')
        'The &#8220;Green&#8221; man'
        """
        try:
            import smartypants
        except ImportError:
            raise TypogrifyError("Error in {% smartypants %} filter: ")
        else:
            from smartypants import Attr
            attr = Attr.set1 & (~(Attr.mask_d))
            output = smartypants.smartypants(text, attr)
            return output

    filters.smartypants = smartypants


