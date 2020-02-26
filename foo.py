import collections as c
import itertools as it
# EmployeeRecord = c.namedtuple('EmployeeRecord', 'name, age, title, department, paygrade')
# EmployeeRecord = c.namedtuple('EmployeeRecord', ['name', 'age', 'title', 'department', 'paygrade'])

# er = EmployeeRecord(name="keith", age=45, title="Boss", department="genius", paygrade="Millionaire")

# er = EmployeeRecord("keith", 45, "Boss", "genius", "Millionaire")
# print(er.age)
# print(er.paygrade)
# print(er._fields)

# namedtuple
# deque
# Counter
# ChainMap
# defaultdictfs
# OrderedDict
# UserDict
# UserList
# UserString

# https://wiki.python.org/moin/UsefulModules
# Django
# Flask
# bottle


# import collections
# import itertools
# import os
# import math
# import html
# import http
# import io
# import json
# import pickle
# import pickletools
# import random
# import re
# import strings
# import time
# import turtle
# import venv
# import webbrowser
# import xml

# %s - String (or any object with a string representation, like numbers)
# %d - Integers
# %f - Floating point numbers
# %.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.
# %x/%X - Integers in hex representation (lowercase/uppercase)
import string

fname = 'Keith'
lname = 'McConchie'
# s = f'Hello {fname} {lname}'

# s = 'Hello {0} {1}'.format(fname, lname)

# print(s)

# print('\t' in string.whitespace)

# errno = 50159747054
# name = 'Bob'
# name2 = 'Ray'

# print('{}, {}, {}'.format('a', 'b', 'c'))
# print("Hello, %s and %s, there is a %x error" % (name, name2, errno))
# valdict = {"name": name, "name2": name2, "errno": errno}
# print("Hello, %(name)s and %(name2)s, there is a %(errno)x error" % valdict)

# print("Hello, {}".format(name))
# print("Hello, {0} and {1}".format(name, name2))
for align, text in zip('<^>', ['left', 'center', 'right']):
    '{0:{fill}{align}16}'.format(text, fill=align, align=align)
