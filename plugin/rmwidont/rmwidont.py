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

        return rendered_text # widont(rendered_text)

    filters.typogrify = typogrify
