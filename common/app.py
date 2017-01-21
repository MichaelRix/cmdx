# Common Markdex by Michael AJ
# common/app.py

import sys

A = sys.getdefaultencoding()
B = sys.getfilesystemencoding()
print('>>>> Encoding:', A, '' if A in ('utf-8') else '*' )
print('>>>> Filesystem:', B, '' if B in ('utf-8', 'mbcs') else '*')
del A, B

from common.shared import *
from flask import Flask

app = Flask('__main__',
	static_folder = config.static_folder,
	template_folder = config.template_folder)

def start():
    app.run(host = config.host, port = config.port, debug = 'debug' in argv)

app.start = start

import sys
sys.modules[__name__] = app
