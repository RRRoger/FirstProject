#!/usr/bin/env python
# encoding: utf-8
'''
    API 根据快递单号,查询快递信息
    http://www.aikuaidi.cn/rest/?key={key}&order={order}&id={id}&ord={ord}&show={show}
'''
import urllib
import httplib
import json
import sys

try:
    billno = sys.argv[1]
    kuaidi_code = sys.argv[2]
    HOST = 'www.aikuaidi.cn'
    PORT = 80
    REST = '/rest'

    def get_express_info(order, kuaidi_id, sort='desc', show='json'):
        '''
            key :  ikuaidi_key
            order : 快递单号
            kuaidi_id : 快递代号,like rufengda
            ord : 排序规则
            show : 返回类型  json/xml/html
        '''
        conn = None

        try:
            conn = httplib.HTTPConnection(HOST, PORT)
            headers = {'Content-Type': 'application/json', 'charset': 'utf-8'}
            post_body = {
                # 自行申请 --!http://www.aikuaidi.cn/api/?type=2
                # 'key': '********************',
                'key': '58b1418f2a5e4b658d6d8c550c8f7229',
                'order': order,
                'id': kuaidi_id,
                'ord': sort,
                'show': show
            }
            url = REST + '?' + urllib.urlencode(post_body)
            conn.request('POST', url, json.dumps(post_body), headers)
            return conn.getresponse().read()
        except Exception:
            ex = None
            print ex
        finally:
            if conn:
                conn.close()

    res = get_express_info(billno, kuaidi_code, 'asc', 'json')
    res = json.loads(res)
    num = res.get('num', 0)  # 今天已使用次数
    # updateTime = res.get('updateTime', 0)  # 最近更新时间
    c_name = res.get('name', 0)  # 快递公司
    message = res.get('message', 0)  # 其他信息
    order = res.get('order', {}) # 快递单号
    data = res.get('data', {})
    if num:
            print u'今天已使用次数 [%s]' % num
    # if updateTime:
    #     print u'最新更新时间 [%s]' % updateTime
    if c_name:
        print u'快递公司 [%s]' % c_name
    if message:
        print u'其他信息 [%s]' % message
    if order:
        print u'快递单号 [%s]' % order
    print ''
    if data:
        # print data
        # print u'剩余次数[%s]' % data.get('num')
        for r in data:
            print u'时间:%s' % r.get('time')
            print u'进度:%s' % r.get('content')

        print u'祝你快递在中途爆炸,BOOM!'
    else:
        print u'我猜你是输错了,或者该运单号没有信息!!'
except Exception, e:
    print u'错误信息:%s' % e
    print u'使用方法:在终端输入'
    print u'    python query_express.py 你的单号 快递代码'
    print u'  查询快递代码地址: http://www.aikuaidi.cn/api/?type=2'
