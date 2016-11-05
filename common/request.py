# Common Markdex by Michael AJ
# common/request.py

from flask import request, Response as response, make_response, render_template, abort, redirect, url_for, send_file, send_from_directory, safe_join

def GET(key):
    return request.args.get(key)

def POST(key):
    return request.form.get(key)

def COOKIE(key):
    return request.cookies.get(key)

def response_redirect(self, location, permanent = False):
    if permanent:
        self.status_code = 301
    else:
        self.status_code = 302
    self.location = location

response.redirect = response_redirect
