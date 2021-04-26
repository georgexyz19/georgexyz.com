#!/usr/bin/env python

import os
import uuid
import datetime

from pelican.tools.pelican_quickstart import ask
from pelican.utils import slugify
from pelican.settings import DEFAULT_CONFIG, read_settings
from pelican import __version__

from pelican import Pelican
from jinja2 import Environment, BaseLoader

markdown_temp = '''title: {{ title }}
slug: {{ slug }}
date: {{ date }}
modified: {{ modified }}
tags: {{ tags }}
note: {{ note }}
{% if hasrp -%}
related_posts: {{ related_posts }}
{% endif -%}
no: {{ no }}

{{ first_sentence }}
'''


def main():

    print('''Welcome to pelican-post v{v}.

This script will help you create a new pelican post.

Please answer the following questions so this script can generate the post.
    '''.format(v=__version__))

    CONF = {}

    # where to save post
    cwd = os.path.dirname(os.path.abspath(__file__))
    dirpath = os.path.join(cwd, 'content', 'posts')
    rel = os.path.relpath(dirpath, cwd)
    # print(f'{cwd} \n {dirpath} \n {rel}')

    CONF['basedir'] = os.path.abspath(
        os.path.expanduser(
            ask('Where do you want to save the markdown file?',
                answer=str,
                default=rel)))

    CONF['title'] = ask('What will be the title of this post?',
                        answer=str,
                        default='NEW TITLE')

    default_slug = slugify(CONF['title'],
                           DEFAULT_CONFIG['SLUG_REGEX_SUBSTITUTIONS'])

    CONF['slug'] = ask('What will be the slug of this post?',
                       answer=str,
                       default=default_slug)

    extension = '.md'
    dest_file = os.path.join(CONF['basedir'], CONF['slug'] + extension)

    if os.path.exists(dest_file):
        random_chars = uuid.uuid4().hex.upper()[0:6]
        print(
            f'{CONF["slug"]} file already exists, \
                add a random string {random_chars} to slug'
        )
        CONF['slug'] = CONF['slug'] + random_chars
        dest_file = os.path.join(CONF['basedir'], CONF['slug'] + extension)

    time_format = "%Y-%m-%d %H:%M"
    time_string = datetime.datetime.now().strftime(time_format)

    CONF['date'] = ask('What will be the date/time of the post?',
                       answer=str,
                       default=time_string)

    CONF['modified'] = CONF['date']

    # try reading tags, wrap in try block
    # need markdown package in order to read markdown ###
    settings = read_settings('pelicanconf.py', override={})
    pelican = Pelican(settings)
    context = settings.copy()

    context['generated_content'] = {}
    context['static_links'] = set()
    context['static_content'] = {}
    context['localsiteurl'] = settings['SITEURL']

    generators = [
        cls(
            context=context,
            settings=pelican.settings,
            path=pelican.path,
            theme=pelican.theme,
            output_path=pelican.output_path,
        ) for cls in pelican.get_generator_classes()
    ]

    for p in generators:
        if hasattr(p, 'generate_context'):
            p.generate_context()

    tags = context['tags']
    tag_names = [t.name for t, _ in tags]
    tag_names = sorted(tag_names)

    print('> Tags already used in other posts (choose one or more): ')
    for no, tag in enumerate(tag_names, start=1):
        print(f'    {no} -> {tag}')

    rv_tags = ask(
        'Choose one or more tags (e.g. 1, 4)'
        ' 0 to enter new tag(s)',
        answer=str,
        default='0')

    input_tags = False
    if rv_tags == '0':
        tags_str = ask('Enter new tag(s), (e.g. pelican, python)',
                       answer=str,
                       default='')
        tags_str = tags_str.lower()
        input_tags = True
    else:
        index_tags = rv_tags.split(',')
        index_tags = [int(i) - 1 for i in index_tags]
        tags_value = [tag_names[ind] for ind in index_tags]
        tags_str = ', '.join(tags_value)

    CONF['tags'] = tags_str

    CONF['hasrp'] = ask('Do you want to add related posts?',
                        answer=bool,
                        default=False)

    if CONF['hasrp']:
        if input_tags:
            print('Tags are new input, enter related posts in text editor...')
            CONF['related_posts'] = ' '
        else:
            all_articles = []
            for tag_name in tags_value:
                for t, articles in tags:
                    if t.name == tag_name:
                        all_articles = all_articles + articles
            all_articles = list(dict.fromkeys(all_articles))
            print('> Posts with same tags (choose one or more) ')
            for no, art in enumerate(all_articles, start=1):
                print(f'    {no} -> {art.title}')

            rv_art = ask(
                'Choose one or more articles (e.g. 1, 3)'
                ' 0 to cancel',
                answer=str,
                default='0')

            if rv_art == '0':
                CONF['hasrp'] = False
            else:
                index_art = rv_art.split(',')
                index_art = [int(i) - 1 for i in index_art]
                related = [all_articles[ind].slug for ind in index_art]
                CONF['related_posts'] = ', '.join(related)

    top_no = 0
    for art in context['articles']:
        try:
            if int(art.no) > top_no:
                top_no = int(art.no)
        except AttributeError:
            # print('Warning: {0}'.format(e))
            pass
    top_no = top_no + 1
    CONF['no'] = ask('Add a number for the post (start from 1)',
                     answer=int,
                     default=top_no)

    CONF['note'] = ask('Add a short note to yourself for this post?',
                       answer=str,
                       default='note to be added')

    CONF['first_sentence'] = ask('Write the first sentence of the article',
                                 answer=str,
                                 default='This is the first sentence ...')

    try:
        with open(dest_file, 'w') as fd:
            _template = Environment(
                loader=BaseLoader).from_string(markdown_temp)
            fd.write(_template.render(**CONF))
    except OSError as e:
        print('Error: {0}'.format(e))

    print('Done. Your new post is available at %s' % rel)
    # import pprint
    # pprint.pprint(CONF)
    # pprint.pprint(tags_str)
    # pprint.pprint(context)

    return


if __name__ == "__main__":
    main()
