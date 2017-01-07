# Common Markdex by Michael AJ
# common/mark.py

import re
from markdown import markdown, Extension

class HTML5(Extension):
    def extendMarkdown(self, md, md_globals):
        md.output_format = 'html5'

def add_indiv_replace(text):
    return re.sub(r'\<div(.*?)\>', r'<div\g<1> markdown="1">', text)

def remove_indiv_replace(html):
    return re.sub(r'\<div(.*?)\x20markdown="1"\>', r'<div\g<1>>', html)

def gfm(text):
    rlist = [   (r'```(\w+)\n([^`]*)```', r'<pre language="\g<1>">\n\g<2></pre>'),
                (r'```([^`]*)```', r'<pre>\g<1></pre>'),
                (r'~~([^~]+)~~', r'<del>\g<1></del>'),
                (r'\-\x20\[\x20\][\x20]{0,1}([^\n]*)', r'- <input type="checkbox">\g<1>'),
                (r'\-\x20\[x\][\x20]{0,1}([^\n]*)', r'- <input type="checkbox" checked>\g<1>')];
    for r in rlist:
        text = re.sub(r[0], r[1], text)
    return text

def down(text):
    gfmed_text = gfm(text)
    gfmed_text = add_indiv_replace(gfmed_text)
    html = markdown(gfmed_text, extensions = ['markdown.extensions.extra', HTML5()])
    html = remove_indiv_replace(html)
    return html
