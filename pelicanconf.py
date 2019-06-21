#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Rahul Ahuja'
SITENAME = 'Rahul Ahuja'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ('GitHub', 'https://github.com/rhlahuja'),
    ('LinkedIn', 'https://www.linkedin.com/in/rahul-ahuja-22291184/'),
)

# Social widget
# SOCIAL = (('You can add links in your config file', '#'), ('Another social link', '#'))
M_DISABLE_SOCIAL_META_TAGS = True

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# THEME = 'startbootstrap-agency'
# BOOTSTRAP_THEME = ''

THEME = 'm.css/pelican-theme'
THEME_STATIC_DIR = 'static'
DIRECT_TEMPLATES = ('index',)

M_CSS_FILES = (
    'https://fonts.googleapis.com/css?family=Source+Sans+Pro:400,400i,600,600i%7CSource+Code+Pro:400,400i,600',
    '/static/m-dark.css',
)
M_THEME_COLOR = '#22272e'

FAVICON_PATH = 'extra/favicon.ico'
# M_FAVICON = (FAVICON_PATH, 'image/x-ico')

PLUGIN_PATHS = ('m.css/plugins',)
PLUGINS = ('m.htmlsanity',)

STATIC_PATHS = (FAVICON_PATH,)
EXTRA_PATH_METADATA = {
    FAVICON_PATH: {'path': 'favicon.ico'},
    'extra/CNAME': {'path': 'CNAME'},
}
