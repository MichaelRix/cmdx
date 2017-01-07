# Common Markdex by Michael AJ
# common/config.py

import sys
import common.const as config

config.host = '0.0.0.0'
config.port = 5000

config.doc_root = 'root'
config.static_folder = 'static'
config.template_folder = 'template'

config.uri_extname = False
config.map_style = True
config.list_dir = True

# Have nothing to do with the following

for n in ['doc_root', 'static_folder', 'template_folder']:
	val = config.__getattribute__(n)
	if val.startswith('/'): pass
	else: config.__setattr__(n, 'user/' + val)
config.__lock__ = True

sys.modules[__name__] = config
