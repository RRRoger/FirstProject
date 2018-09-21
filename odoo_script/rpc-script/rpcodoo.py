 # -*- encoding: utf-8 -*-
import xmlrpclib
import datetime
import json
import xlrd  
import re 
import ssl
import ConfigParser
import string, os, sys

ssl_ctx = ssl.create_default_context()
ssl_ctx.check_hostname = False
ssl_ctx.verify_mode = ssl.CERT_NONE

_30 = '_30'
LOCALHOST = 'localhost'

ENV = _30
PATH = "./rpc.conf"

cf = ConfigParser.ConfigParser()
cf.read(PATH)
confs = dict(cf.items(ENV))
print confs

for i in ['username', 'db', 'host', 'https', 'userpass', 'port']:
    exec "%s = confs.get('%s')" % (i.upper(), i)


if HTTPS=='1':
    sock_common = xmlrpclib.ServerProxy ('https://%s/xmlrpc/common' % (HOST,), verbose=False, use_datetime=True, context=ssl_ctx)
    uid = sock_common.login(DB, USERNAME, USERPASS)
    sock = xmlrpclib.ServerProxy('https://%s/xmlrpc/object' % (HOST,), verbose=False, use_datetime=True, context=ssl_ctx)
else:
    sock_common = xmlrpclib.ServerProxy ('http://%s:%s/xmlrpc/common' % (HOST,PORT))
    uid = sock_common.login(DB, USERNAME, USERPASS)
    sock = xmlrpclib.ServerProxy('http://%s:%s/xmlrpc/object' % (HOST,PORT))
    

res = {}
res = sock.execute(DB, uid, USERPASS, 'hr.employee', 'read', [1,2,3,4,5,6], ['name'])
print res
