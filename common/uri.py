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
                    request_uri = request_uri + 'index.md'
                else:
                    request_uri = request_uri + 'index'
                type = 'document'
            elif scratch == 'static':
                self.path = config.static_folder + '/' + request_uri
                self.exists = isfile(self.path)
                type = 'static'
                request_uri = 'static' + request_uri
        self.request_uri = request_uri
        if type == 'document':
            if config.uri_extname:
                self.path = config.doc_root + '/' + request_uri
            else:
                self.path = config.doc_root + '/' + request_uri + '.md'
            self.type = 'document'
            self.exists = isfile(self.path)
            if not self.exists:
                if isdir(config.doc_root + '/' + request_uri):
                    type = 'dir'
        if type == 'dir':
            self.path = config.doc_root + '/' + request_uri
            self.type = 'dir'
            self.exists = isdir(self.path)

import sys
sys.modules[__name__] = uri
