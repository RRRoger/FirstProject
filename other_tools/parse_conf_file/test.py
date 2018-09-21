# -*- encoding: utf-8 -*-

import ConfigParser
import string, os, sys

cf = ConfigParser.ConfigParser()
cf.read("test.conf")
# 返回所有的section
s = cf.sections()
print 'section:', s

o = cf.options("db")
print 'options:', o

v = cf.items("db")
print 'db:', v

v = dict(cf.items("db"))
print 'db:', v

