# Common Markdex by Michael AJ
# common/index.py

import common.route as route
import common.uri as uri
import common.fs as fs
import common.mark as mark
from common.shared import *
from common.request import *

def f_favicon_ico():
    u = uri('favicon.ico', 'static')
    if (u.exists):
        return send_file(u.path, mimetype = 'image/x-icon')
    else:
        abort(404)
route.add('/favicon.ico', f_favicon_ico)

def f_style_css():
    u = uri('style.css', 'static')
    if (u.exists):
        return send_file(u.path, mimetype = 'text/css')
    else:
        abort(404)
if config.map_style:
    route.add('/style.css', f_style_css)

def m_render(u, is_index = False):
    filename = u.path
    markdown = fs.read(filename)
    html = mark.down(markdown)
    return render_template('document.html', uri = u.request_uri, html = html, is_index = is_index)

def m_listdir(u):
    path = u.path
    content = fs.list(path)
    if u.request_uri != '': content['dirs'].insert(0, '..')
    return render_template('list.html', uri = u.request_uri, content = content)

def i_dir_entry(u):
    if u.exists:
        index = uri(u.request_uri, 'index')
        if index.exists:
            return m_render(index, True)
        else:
            if config.list_dir:
                return m_listdir(u)
            else:
                abort(403)
    else:
        return abort(404)

def i_doc_entry(u):
    if u.exists:
        return m_render(u)
    else:
        return abort(404)

def i_entry(request_uri):
    u = uri(request_uri)
    if u.type == 'dir':
        return i_dir_entry(u)
    elif u.type == 'document':
        return i_doc_entry(u)
route.add('/<path:request_uri>', i_entry)

def i_root():
    return i_dir_entry(uri(''))
route.add('/', i_root)
