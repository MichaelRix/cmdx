# Common Markdex by Michael AJ
# common/fs.py

from common.shared import *
from os import listdir
from os.path import isdir, isfile

def read(filename, fileop = 'r'):
    try:
        if ('b' in fileop):
            f = open(filename, fileop)
        else:
            f = open(filename, fileop, encoding = 'utf-8')
        data = f.read()
        return data
    except:
        raise

def list(directory):
    dirs, files = [], []
    if not directory.endswith('/'):
        directory += '/'
    if isdir(directory):
        for name in listdir(directory):
            if isdir(directory + name):
                dirs.append(name)
            elif isfile(directory + name) and name.endswith('.md'):
                if config.uri_extname: files.append(name)
                else: files.append(name[:-3])
        dirs.sort()
        files.sort()
        return {'dirs': dirs, 'files': files}
