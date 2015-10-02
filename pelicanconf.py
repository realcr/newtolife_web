#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

STATIC_PATHS = ['articles']
ARTICLE_PATHS = ['articles']
PAGE_PATHS = ['pages']

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

THEME = 'tuxlite_tbs'

AUTHOR = u'new'
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
RELATIVE_URLS = True
