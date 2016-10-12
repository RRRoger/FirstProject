# -*- coding: utf-8 -*-
try:
    import httplib
except ImportError:
    import http.client as httplib
import urllib
import hashlib
import json
import logging
import base64
from openerp.osv import osv
from openerp.tools.xmlutils import parse, unparse

_logger = logging.getLogger(__name__)

N_REST = '/bsp-wms/OmsCommons'
LANG = "zh-CN"

"""
    顺丰接口封装 by chenpeng 2016年08月25日
"""


# 请求报文+加密密钥(由顺丰提供给商家) MD5 + base64
def get_data_digest(checkword, post_body_xml):
    # ===========================================================================
    # '''获得签名验证
    # @param checkword: 签名需要的密钥
    # @param post_body: xml,
    # 先
    # '''
    # ===========================================================================
    rule_str = "%s%s" % (post_body_xml, checkword)
    tmpl = hashlib.md5(rule_str.encode('utf-8')).digest()
    data_digest = base64.encodestring(tmpl)
    return data_digest


class RestApi(object):
    # ===========================================================================
    # Rest api的基类
    # ===========================================================================

    def __init__(self, post_body, host='bsp.sit.sf-express.com', port=8080):  # todo 改成正式环境的域名和端口
        # =======================================================================
        # Args @param host: 请求的域名或者ip
        #      @param port: 请求的端口
        # =======================================================================
        self.__host = host
        self.__port = port
        self.__post_body = post_body

    def getapiname(self):
        return ""

    def get_final_post_body(self):
        # =======================================================================
        # 获得最终请求的post_body(XML)
        # =======================================================================
        final_post_body = {}
        Request = {}
        Request["@service"] = self.getapiname()
        Request["@lang"] = LANG
        Request['Head'] = {}
        Request['Head']['AccessCode'] = self.__accesscode
        Request['Head']['Checkword'] = self.__checkword
        Request['Body'] = self.__post_body
        final_post_body['Request'] = Request
        print final_post_body
        return unparse(final_post_body, full_document=False)

    def get_request_header(self):
        return {'content-type': "application/x-www-form-urlencoded;charset=UTF-8"}

    def set_app_info(self, accesscode, checkword):
        # =======================================================================
        # 设置请求的app信息
        # 设置信息 accesscode 接入编码 , checkword 校验码
        # =======================================================================
        self.__accesscode = accesscode
        self.__checkword = checkword

    def getResponse(self, authrize=None, timeout=30):
        # =======================================================================
        # 获取response结果
        # =======================================================================
        connection = httplib.HTTPConnection(self.__host, self.__port, False, timeout)
        connection.connect()
        header = self.get_request_header()
        post_body_xml = unparse(self.__post_body, full_document=False)
        data_digest = get_data_digest(self.__checkword, post_body_xml)
        #         print 'data_digest',data_digest
        final_post_body_xml = self.get_final_post_body()
        sys_parameters = {
            'data_digest': data_digest,
            'logistics_interface': final_post_body_xml
        }
        print "data_digest =",data_digest
        url = N_REST
        print '\n'
        print 'http://bsp.sit.sf-express.com:8080' + url
        print '\n'
        print "final_post_body_xml =",final_post_body_xml
        print '\n'

        connection.request('POST', url, urllib.urlencode(sys_parameters) , headers=header)
        response = connection.getresponse()
        if response.status is not 200:
            raise osv.except_osv(u"错误",
                                 'invalid http status ' + str(response.status) + ',detail body:' + response.read())
        resp = response.read()
        print '\n'
        print resp
        print '\n'
        result = parse(resp)  # type:xml_str
        jsonobj = json.loads(json.dumps(result))  # xml --> str --> dict
        return jsonobj

# test
# req = RestApi({'ItemQueryRequest':{'CompanyCode':'ZX08310101','SkuNoList':[{'SkuNo':'SKU'},]}})
# req.set_app_info('DEbxgTDbvsE6sJN8NZMy4w==','kgSTey5AFFxxnyTjxSM9WDYPgMxYonN5')
# print req.getResponse()
