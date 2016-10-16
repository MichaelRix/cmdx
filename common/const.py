# Common Markdex by Michael AJ
# common/const.py

class const():
	__lock__ = False
	def __setattr__(self, key, value):
		if self.__lock__:
			raise AttributeError
		# if key in self.__dict__:
		#     raise AttributeError
		else: self.__dict__[key] = value

import sys
sys.modules[__name__] = const()
