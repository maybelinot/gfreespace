#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Eduard Trott
# @Date:   2015-09-08 09:23:57
# @Email:  etrott@redhat.com
# @Last modified by:   etrott
# @Last Modified time: 2015-10-19 09:57:53

from __future__ import unicode_literals, absolute_import

import logging
import os

# EXTERNALLY INSTALLED
import yaml

from oauth2client import file, client, tools

# Load logging before anything else
logging.basicConfig(format='>> %(message)s')
logr = logging.getLogger('gfreespace')

''' Load the config file so modules can import and reuse '''
dir_path = os.path.dirname(os.path.realpath(__file__))
dir_path = os.path.abspath(os.path.join(dir_path, '..'))
CONFIG_FILE = os.path.expanduser('~/.gfreespace')
if os.path.exists(CONFIG_FILE):
    with open(CONFIG_FILE) as _:
        config = yaml.load(_)
else:
    config = {}


CLIENT_SECRET_FILE = os.path.expanduser('~/.gdrive_private')

DEFAULT_TOKEN = os.path.expanduser('~/.oauth/calendar.json')

SCOPES = ('https://www.googleapis.com/auth/calendar '
          'https://apps-apis.google.com/a/feeds/calendar/resource/')


def get_credentials():
    """
    FIXME DOCs
    Taken from:
    https://developers.google.com/drive/web/quickstart/python
    """
    try:
        import argparse
        flags = argparse.ArgumentParser(
            parents=[tools.argparser]).parse_known_args()[0]
    except ImportError:
        flags = None
        logr.error(
            'Unable to parse oauth2client args; `pip install argparse`')


    store = file.Storage(DEFAULT_TOKEN)

    credentials = store.get()
    if not credentials or credentials.invalid:

        flow = client.flow_from_clientsecrets(
            CLIENT_SECRET_FILE, SCOPES)
        flow.redirect_uri = client.OOB_CALLBACK_URN
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else:  # Needed only for compatability with Python 2.6
            credentials = tools.run(flow, store)
        logr.info('Storing credentials to ' + DEFAULT_TOKEN)

    return credentials
