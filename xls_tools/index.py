# -*- encoding: utf-8 -*-

from adapter import *
import json
import datetime

FULL_DIR = 'excels'  # 生成excel存放路劲
FIEL_NAME = u'data'  # 生成excel内部sheet文件名
DATA_PATH = './data.txt'  # json数据存放的文件名

with open(DATA_PATH, 'r') as content_file:
    #  获得json文本
    content = content_file.read()

DATA = json.loads(content)

# HEADERS 表头信息, 
"""
    name 中文显示名称
    alias json里面的key
    seq 每个key在excel里面的排序
    group 聚合函数: 
        sum 该key对应的数据求和, avg 该key对应的数据求平均
"""
HEADERS = [
    {'name': u'用户名称', 'alias': 'xtyhxm', 'seq': 0, 'group':''},
    {'name': u'用户代码', 'alias': 'xtyhdm', 'seq': 1, 'group':''},
    {'name': u'用户代码', 'alias': 'xtyhdm', 'seq': 2, 'group':''},
]
HEADERS = sorted(HEADERS, key=lambda x: x['seq'])
excel_data = format_data(HEADERS, DATA)
base64_data = excel_data_getter(u'主数据', excel_data)
file_name = FIEL_NAME + '-' + datetime.datetime.utcnow().strftime('%Y%m%d%H%M%S') + '.xls'
full_path = save_file(FULL_DIR, file_name, base64_data)
print u'生成excel, 路径:', full_path




