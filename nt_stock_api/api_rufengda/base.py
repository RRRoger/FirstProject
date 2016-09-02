# -*- coding: utf-8 -*-
try: import httplib
except ImportError:
    import http.client as httplib
import urllib
import time
import hashlib
import json
import logging
from openerp.osv import osv

_logger = logging.getLogger(__name__)

N_REST = '/api'

"""
    如风达接口封装 by chenpeng
"""

#请求报文+“|”+加密密钥(由如风达提供给商家)
def get_token(secret,post_body):
    #===========================================================================
    # '''获得token
    # @param secret: 签名需要的密钥
    # @param post_body: 支持list,dict,string
    # '''
    #===========================================================================
    rule_str = "%s|%s" % (post_body,secret)
    token = hashlib.md5(rule_str.encode('utf-8')).hexdigest().upper()
    return token


class RestApi(object):
    #===========================================================================
    # Rest api的基类
    #===========================================================================
    
    def __init__(self, post_body ,host='wmsedi.wuliusys.com', port = 80):
        #=======================================================================
        # Args @param host: 请求的域名或者ip
        #      @param port: 请求的端口
        #=======================================================================
        self.__host = host
        self.__port = port
        self.__post_body = post_body

    def getapiname(self):
        return ""

    def get_request_header(self):
        return {"Content-Type":"text/json","charset": "utf-8"}
    
    def set_app_info(self, identity , secret):
        #=======================================================================
        # 设置请求的app信息
        # @param appinfo: import top
        #                 appinfo top.appinfo(identity,secret)
        #=======================================================================
        self.__identity = identity
        self.__secret = secret

    def getResponse(self, authrize=None, timeout=30):
        #=======================================================================
        # 获取response结果
        #=======================================================================
        connection = httplib.HTTPConnection(self.__host, self.__port, False, timeout)
        connection.connect()
        header = self.get_request_header()
        body = json.dumps(self.__post_body)
        token = get_token(self.__secret,body)
#         print 'token',token
        sys_parameters = {
            'token':token,
            'identity':self.__identity
        }

        url = N_REST + self.getapiname() + "?" + urllib.urlencode(sys_parameters)
        connection.request('POST', url, body=body, headers=header)
        print body
        response = connection.getresponse()
        if response.status is not 200:
            raise osv.except_osv(u"错误", 'invalid http status ' + str(response.status) + ',detail body:' + response.read())
        result = response.read()
        jsonobj = json.loads(result)
        if isinstance(jsonobj,dict):
            _logger.info(jsonobj)
            if 'IsSuccess' in jsonobj:
                if jsonobj.get('IsSuccess',False):
                    return jsonobj.get('ResultData',{})
                else:
                    if 'Message' in jsonobj:
                        raise osv.except_osv(u"错误", "Message:%s" % jsonobj.get('Message',False))
                    if 'ErrorMessage' in jsonobj:
                        raise osv.except_osv(u"错误", "ErrorMessage:%s" % jsonobj.get('ErrorMessage',False))
        _logger.info(jsonobj)
        return jsonobj

#test
# req = RestApi([{"OutStoreNo":"JS2015121403115224"}, {"OutStoreNo":"JS2015082810142882"}],host="219.141.203.181",port = 8125)
# req.set_app_info('08d6a8c5-2a4d-415a-abbc-7936b9699882','996a3c87-64a9-4a77-b845-2f1c126ed14b')
# print req.getResponse()
