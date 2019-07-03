#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys

sys.path.append(os.curdir)
from pelicanconf import *


# If your site is available via HTTPS, make sure SITEURL begins with https://
SITEURL = 'https://rahuja.dev'
RELATIVE_URLS = False

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'

DELETE_OUTPUT_DIRECTORY = True

M_CSS_FILES = (
    'https://fonts.googleapis.com/css?family=Source+Sans+Pro:400,400i,600,600i%7CSource+Code+Pro:400,400i,600',
    '/static/m-dark-compiled.css',
)


GOOGLE_ANALYTICS_UNIVERSAL = 'UA-142490565-1'
GOOGLE_ANALYTICS_PROPERTY = 'rahuja.dev'
