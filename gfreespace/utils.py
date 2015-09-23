#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Eduard Trott
# @Date:   2015-09-08 09:23:57
# @Email:  etrott@redhat.com
# @Last modified by:   etrott
# @Last Modified time: 2015-09-23 10:45:02

from __future__ import unicode_literals, absolute_import

import logging
import os

# EXTERNALLY INSTALLED
import yaml

# Load logging before anything else
logging.basicConfig(format='>> %(message)s')
logr = logging.getLogger('gfreespace')

''' Load the config file so modules can import and reuse '''
dir_path = os.path.dirname(os.path.realpath(__file__))
dir_path = os.path.abspath(os.path.join(dir_path, '..'))
CONFIG_FILE = os.path.expanduser('~/.gfreespace/config')
if os.path.exists(CONFIG_FILE):
    with open(CONFIG_FILE) as _:
        config = yaml.load(_)
else:
    config = {}
