# Common Markdex by Michael AJ
# common/app.py

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
