#!/usr/bin/python3
#-*- coding: utf-8 -*-
# Common Markdex by Michael AJ
# Reconstructed on 30th, Sept. 2016

if __name__ != '__main__': exit()

import sys
if not sys.version.split(' ')[0].startswith('3'):
	exit('Your python version is not hatal.\nCMDX **requires** python3.')

from common.shared import *
from common import *

app.start()
