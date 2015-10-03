#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# PLUGIN_PATHS = ['/home/real/projects/websites/pelican_generic/plugins']
PLUGIN_PATHS = ['../pelican_generic/plugins/pelican-plugins']
PLUGINS = ['render_math','tipue_search']

DIRECT_TEMPLATES = \
    (('index','tags','categories','authors','archives','search'))



STATIC_PATHS = ['articles']
ARTICLE_PATHS = ['articles']
PAGE_PATHS = ['pages']

# Files that we will not copy to output dir:
# Ignore vim swap files:
IGNORE_FILES = ['*.swp','*.swo']

# Directories and categories settings.
# Every article will be in a single directory, which will
# also contain the images and other related files.

# We don't use the directory name as the category, as we have many nested
# directories. Instead, we use the default category 'Blog':
USE_FOLDER_AS_CATEGORY = False
DEFAULT_CATEGORY = 'Articles'

# We display pages and categories on the website menu:
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = True

# Delete the output directory before generating new output files:
DELETE_OUTPUT_DIRECTORY = True


THEME = 'newtolife_theme'

AUTHOR = u'real'
SITENAME = u'newtolife'
SITEURL = 'https://www.newtolife.net'

PATH = 'content'

TIMEZONE = 'UTC'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# License text at the end of every page:
LICENSE_TEXT = """<a rel="license"
href="http://creativecommons.org/licenses/by-nc/4.0/"><img alt="Creative Commons License" 
style="border-width:0"
src="https://i.creativecommons.org/l/by-nc/4.0/80x15.png" /></a><br />This work
is licensed under a <a rel="license"
href="http://creativecommons.org/licenses/by-nc/4.0/">Creative Commons
Attribution-NonCommercial 4.0 International License</a>."""


# Blogroll
#   LINKS = (('Pelican', 'http://getpelican.com/'),
#            ('Python.org', 'http://python.org/'),
#            ('Jinja2', 'http://jinja.pocoo.org/'),
#            ('You can modify those links in your config file', '#'),)


# Social widget
# SOCIAL = (('You can add links in your config file', '#'),
#           ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = False
