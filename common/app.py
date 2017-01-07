# Common Markdex by Michael AJ
# common/app.py

import sys

if not sys.version.split(' ')[0].startswith('3'):
	exit('Your python version is not hatal.\nCMDX requires python3.')
A = sys.getdefaultencoding()
B = sys.getfilesystemencoding()
C = A in ('utf-8') and B in ('utf-8', 'mbcs')
if not C:
	print('>>>> Encoding:', A)
	print('>>>> Filesystem:', B)
del A, B, C

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
