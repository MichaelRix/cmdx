# Common Markdex by Michael AJ
# common/route.py

import common.app as app

def add(rule, func, **kwargs):
    if len(func.__dict__) == 0:
        func.methods = ['GET']
    app.add_url_rule(rule, func.__name__, func, **kwargs)

def map():
    return app.url_map
