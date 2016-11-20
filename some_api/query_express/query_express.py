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
                #自行申请 --!http://www.aikuaidi.cn/api/?type=2
                'key': '********************',
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

    res = get_express_info(billno, kuaidi_code, 'desc', 'json')
    res = json.loads(res)
    data = res.get('data', {})
    if isinstance(data,list):
	    data = data[::-1]
    if data:
        for r in data:
            print u'时间:%s' % r.get('time')
            print u'进度:%s' % r.get('content')

        print u'祝你快递在中途爆炸,BOOM!'
    else:
        print u'我猜你是输错了,或者该运单号没有信息!!'
        print u'别瞎试,这是要钱的!!'
except:
    print u'使用方法:在终端输入'
    print u'    python query_express.pyc 你的单号 快递代码'
    print u'  查询快递代码地址: http://www.aikuaidi.cn/api/?type=2'
