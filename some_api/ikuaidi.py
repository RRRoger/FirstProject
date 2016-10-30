# # -*- encoding: utf-8 -*-
"""
    API 根据快递单号,查询快递信息
    http://www.aikuaidi.cn/rest/?key={key}&order={order}&id={id}&ord={ord}&show={show}
"""
import urllib
import httplib
import json
HOST = 'www.aikuaidi.cn'
PORT = 80
REST = '/rest'
def get_express_info(order,kuaidi_id,sort='desc',show='json'):
    """
        key : 系统参数 ikuaidi_key
        order : 快递单号
        kuaidi_id : 快递代号,like rufengda
        ord : 排序规则
        show : 返回类型  json/xml/html
    """
    conn = None
    try:
        conn = httplib.HTTPConnection(HOST,PORT)
        headers = {"Content-Type":"application/json","charset": "utf-8"}
        post_body = {
            'key':'58b1418f2a5e4b658d6d8c550c8f7229', #ikuaidi提供的key,请去ikuaidi申请,去掉后面的//即可
            'order':order,
            'id':kuaidi_id,
            'ord':sort,
            'show':show
        }
        url = REST + '?' + urllib.urlencode(post_body)
        print url
        conn.request("POST", url, json.dumps(post_body),headers)
        return conn.getresponse().read()#buffering=True
    except Exception,ex:
        print ex
    finally:
        if conn:
            conn.close()
print get_express_info('883137683969763372 ','yuantong','desc','json')
