# -*- encoding: utf-8 -*-

from osv import fields, osv
import logging
import httplib
import urllib
import json

_logger = logging.getLogger(__name__)

"""
    API 创蓝短信接口
    www.cl2009.com
"""
HOST = '222.73.117.156'
PORT = 80

TEST_HOST = '222.73.117.169'
TEST_PORT = 80


class cl_adapter(osv.osv_memory):
    _name = 'nt.chuanglan.sms'

    # 发送短信
    def send_message(self, cr, uid, mobile_list, msg, needstatus=True, extno=False):
        REST = '/msg/HttpBatchSendSM'

        """
            mobile_list : 手机号列表
            msg : 信息文本
            needstatus : 必填参数。是否需要状态报告，取值true或false，true，表明需要状态报告；false不需要状态报告
            extno : 可选参数，扩展码，用户定义扩展码，3位
        """
        ICP = self.pool.get('ir.config_parameter')

        is_dev = ICP.get_param(cr, uid, 'nt_cl2009.is_dev') or True

        if is_dev:
            account = ICP.get_param(cr, uid, 'nt_cl2009.test_account') or ''
            pswd = ICP.get_param(cr, uid, 'nt_cl2009.test_pswd') or ''
            host = HOST
            port = PORT
        else:
            account = ICP.get_param(cr, uid, 'nt_cl2009.account') or ''
            pswd = ICP.get_param(cr, uid, 'nt_cl2009.pswd') or ''
            host = TEST_HOST
            port = TEST_PORT

        post_body = {
            'account': account,
            'pswd': pswd,
            'mobile': ','.join(mobile_list),
            'msg': msg,
            'needstatus': needstatus,
        }
        if extno:
            post_body['extno'] = extno
        url = REST + '?' + urllib.urlencode(post_body)
        post_body = json.dumps(post_body)
        return self.send_post_request(cr, uid, host, url, port, post_body)


    # 发送短信
    def get_balances(self, cr, uid):
        REST = '/msg/QueryBalance'

        ICP = self.pool.get('ir.config_parameter')

        is_dev = ICP.get_param(cr, uid, 'nt_cl2009.is_dev')

        if is_dev == 'True':
            account = ICP.get_param(cr, uid, 'nt_cl2009.test_account') or ''
            pswd = ICP.get_param(cr, uid, 'nt_cl2009.test_pswd') or ''
            host = HOST
            port = PORT
        else:
            account = ICP.get_param(cr, uid, 'nt_cl2009.account') or ''
            pswd = ICP.get_param(cr, uid, 'nt_cl2009.pswd') or ''
            host = TEST_HOST
            port = TEST_PORT

        post_body = {
            'account': account,
            'pswd': pswd,
        }
        url = REST + '?' + urllib.urlencode(post_body)
        post_body = json.dumps(post_body)
        return self.send_post_request(cr, uid, host, url, port, post_body)

    def send_post_request(self, cr, uid, host, url, port, post_body):
        conn = None
        try:
            headers = {"Content-Type": "text/plain","charset": "utf-8"}
            conn = httplib.HTTPConnection(host, port)
            print host, port, url
            conn.request("POST", url, post_body, headers)
            res = conn.getresponse().read()
            print res
            return res
        except Exception, ex:
            _logger.error(ex)
        finally:
            if conn:
                conn.close()