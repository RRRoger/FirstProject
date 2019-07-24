# -*- encoding: utf-8 -*-

from adapter import *
import json
import datetime

FULL_DIR = 'excels'  # 生成excel存放路劲
FILE_NAME = u'data'  # 生成excel内部sheet文件名
DATA_PATH = './data.txt'  # json数据存放的文件名

with open(DATA_PATH, 'r') as content_file:
    #  获得json文本
    content = content_file.read()
try:
    DATA = json.loads(content)
except:
    DATA = eval(content)

# HEADERS 表头信息, 
"""
    name 中文显示名称
    alias json里面的key
    seq 每个key在excel里面的排序
    group 聚合函数: 
        sum 该key对应的数据求和, avg 该key对应的数据求平均
"""

HEADERS = [
    # 表头名称, 对应key值, 表头排序, (聚合函数 sum, avg)
    (u'商品', 'prod_no', 0, ''),
    (u'进入互道时间', 'nt_create_date', 0, ''),
    (u'下单时间', 'created_at', 0, ''),
    (u'订单号', 'order_no', 0, ''),
    (u'数量', 'quantity', 0, ''),
]

HEADERS = [{'name':r[0] or r[1], 'alias':r[1], 'seq':r[2], 'group':r[3]} for r in HEADERS]

HEADERS = sorted(HEADERS, key=lambda x: x['seq'])
excel_data = format_data(HEADERS, DATA)
base64_data = excel_data_getter(u'主数据', excel_data)
file_name = FILE_NAME + '-' + datetime.datetime.utcnow().strftime('%Y%m%d%H%M%S') + '.xlsx'
full_path = save_file(FULL_DIR, file_name, base64_data)
print u'生成excel, 路径:', full_path




