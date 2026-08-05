#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 生产环境配置

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

# 生产环境覆盖配置
SITEURL = ''
RELATIVE_URLS = False

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

DELETE_OUTPUT_DIRECTORY = False
