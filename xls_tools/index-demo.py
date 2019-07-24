# -*- encoding: utf-8 -*-

from adapter import *
import json
import datetime

FULL_DIR = 'excels'
FILE_NAME = u'data'
DATA_PATH = './data-demo.txt'

with open(DATA_PATH, 'r') as content_file:
    content = content_file.read()

DATA = json.loads(content)

HEADERS = [
    {'name': u'用户名称', 'alias': 'xtyhxm', 'seq': 0, 'group':''},
    {'name': u'用户代码', 'alias': 'xtyhdm', 'seq': 1, 'group':''},
    {'name': u'用户代码', 'alias': 'xtyhdm', 'seq': 2, 'group':''},
]
HEADERS = sorted(HEADERS, key=lambda x: x['seq'])
excel_data = format_data(HEADERS, DATA)
base64_data = excel_data_getter(u'主数据', excel_data)
file_name = FILE_NAME + '-' + datetime.datetime.utcnow().strftime('%Y%m%d%H%M%S') + '.xlsx'
full_path = save_file(FULL_DIR, file_name, base64_data)
print '生成excel, 路径:', full_path




