# Common Markdex by Michael AJ
# common/uri.py

from common.shared import *
from os.path import isdir, isfile

class uri:
    def __init__(self, request_uri, scratch = None):
        if request_uri.startswith('/'):
            request_uri = request_uri[1:]
        if request_uri == '' or request_uri.endswith('/'):
            type = 'dir'
        else:
            type = 'document'

        if scratch:
            if scratch == 'index':
                if config.uri_extname:
                    request_uri += 'index.md'
                else:
                    request_uri += 'index'
                type = 'document'
            elif scratch == 'static':
                path = config.static_folder + '/' + request_uri
                exists = isfile(path)
                type = 'static'
                request_uri = 'static' + request_uri

        if type == 'document':
            if config.uri_extname:
                path = config.doc_root + '/' + request_uri
            else:
                path = config.doc_root + '/' + request_uri + '.md'
            exists = isfile(path)
            if not exists:
                if isdir(config.doc_root + '/' + request_uri):
                    type = 'dir'
                    if not request_uri.endswith('/'): request_uri += '/'
        if type == 'dir':
            path = config.doc_root + '/' + request_uri
            exists = isdir(path)
        self.request_uri = request_uri
        self.type = type
        self.path = path
        self.exists = exists

import sys
sys.modules[__name__] = uri
