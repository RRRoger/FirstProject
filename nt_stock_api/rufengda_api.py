# -*- encoding: utf-8 -*-

from osv import fields,osv
import datetime,time
import pytz
import string
import logging
import datetime
import time
import json
import api_rufengda

_logger = logging.getLogger(__name__)

TEST_HOST = "219.141.203.181"
TEST_PORT = 8125

def utc2local(str_utc_time):
        local_tz = pytz.timezone('Asia/Shanghai')
        utc_tz = pytz.timezone('UTC')
        utc_time = datetime.datetime.strptime(str_utc_time[0:19], '%Y-%m-%d %H:%M:%S')
        utc_time = utc_time.replace(tzinfo=utc_tz)
        local_time = utc_time.astimezone(local_tz)
        return local_time.strftime('%Y-%m-%d %H:%M:%S')

class rufengda_api(osv.osv_memory):
    _name = 'nt.rufengda.api'
    
    #订单操作日志接口
    def get_order_status(self,cr,uid,post_body,context={}):
        ICP = self.pool.get('ir.config_parameter')
        is_dev_env = False if str(ICP.get_param(cr,uid,'nt_rufengda.is_dev_env'))=='False' else True
        if is_dev_env:
            identity = ICP.get_param(cr,uid,'nt_rufengda.test_identity')
            secret = ICP.get_param(cr,uid,'nt_rufengda.test_secret')
            req = api_rufengda.GetOrderStatus(post_body,TEST_HOST,TEST_PORT) 
        else:
            identity = ICP.get_param(cr,uid,'nt_rufengda.identity')
            secret = ICP.get_param(cr,uid,'nt_rufengda.secret')
            req = api_rufengda.GetOrderStatus(post_body) 
        req.set_app_info(identity,secret)
        resp_msg = req.getResponse()
        return resp_msg
    
    #出库接口
    def out_store_apply(self,cr,uid,post_body,context={}):
        ICP = self.pool.get('ir.config_parameter')
        is_dev_env = False if str(ICP.get_param(cr,uid,'nt_rufengda.is_dev_env'))=='False' else True
        if is_dev_env:
            identity = ICP.get_param(cr,uid,'nt_rufengda.test_identity')
            secret = ICP.get_param(cr,uid,'nt_rufengda.test_secret')
            req = api_rufengda.OutStoreApplay(post_body,TEST_HOST,TEST_PORT) 
        else:
            identity = ICP.get_param(cr,uid,'nt_rufengda.identity')
            secret = ICP.get_param(cr,uid,'nt_rufengda.secret')
            req = api_rufengda.OutStoreApplay(post_body) 
        req.set_app_info(identity,secret)
        resp_msg = req.getResponse() #list
        for res in resp_msg:
            if 'ErrorMessage' in res:
                _logger.error("如风达订单导入ErrorMessage:%s" % res['ErrorMessage'])
        return resp_msg
    
    #订单取消接口
    def out_store_cancel(self,cr,uid,post_body,context={}):
        ICP = self.pool.get('ir.config_parameter')
        is_dev_env = False if str(ICP.get_param(cr,uid,'nt_rufengda.is_dev_env'))=='False' else True
        if is_dev_env:
            identity = ICP.get_param(cr,uid,'nt_rufengda.test_identity')
            secret = ICP.get_param(cr,uid,'nt_rufengda.test_secret')
            req = api_rufengda.OutStoreCancel(post_body,TEST_HOST,TEST_PORT) 
        else:
            identity = ICP.get_param(cr,uid,'nt_rufengda.identity')
            secret = ICP.get_param(cr,uid,'nt_rufengda.secret')
            req = api_rufengda.OutStoreCancel(post_body) 
        req.set_app_info(identity,secret)
        resp_msg = req.getResponse()
        return resp_msg
    
    #入库单接收接口
    def purchase_create(self,cr,uid,post_body,context={}):
        ICP = self.pool.get('ir.config_parameter')
        is_dev_env = False if str(ICP.get_param(cr,uid,'nt_rufengda.is_dev_env'))=='False' else True
        if is_dev_env:
            identity = ICP.get_param(cr,uid,'nt_rufengda.test_identity')
            secret = ICP.get_param(cr,uid,'nt_rufengda.test_secret')
            req = api_rufengda.PurchaseCreate(post_body,TEST_HOST,TEST_PORT) 
        else:
            identity = ICP.get_param(cr,uid,'nt_rufengda.identity')
            secret = ICP.get_param(cr,uid,'nt_rufengda.secret')
            req = api_rufengda.PurchaseCreate(post_body) 
        req.set_app_info(identity,secret)
        resp_msg = req.getResponse()
        return resp_msg
           
    #入库单状态改变接口
    def purchas_status_change(self,cr,uid,post_body,context={}):
        ICP = self.pool.get('ir.config_parameter')
        is_dev_env = False if str(ICP.get_param(cr,uid,'nt_rufengda.is_dev_env'))=='False' else True
        if is_dev_env:
            identity = ICP.get_param(cr,uid,'nt_rufengda.test_identity')
            secret = ICP.get_param(cr,uid,'nt_rufengda.test_secret')
            req = api_rufengda.PurchasStatusChange(post_body,TEST_HOST,TEST_PORT) 
        else:
            identity = ICP.get_param(cr,uid,'nt_rufengda.identity')
            secret = ICP.get_param(cr,uid,'nt_rufengda.secret')
            req = api_rufengda.PurchasStatusChange(post_body) 
        req.set_app_info(identity,secret)
        resp_msg = req.getResponse()
        return resp_msg
    
    #库存查询接口        
    def inventory_query(self,cr,uid,post_body,context={}):
        ICP = self.pool.get('ir.config_parameter')
        is_dev_env = False if str(ICP.get_param(cr,uid,'nt_rufengda.is_dev_env'))=='False' else True
        if is_dev_env:
            identity = ICP.get_param(cr,uid,'nt_rufengda.test_identity')
            secret = ICP.get_param(cr,uid,'nt_rufengda.test_secret')
            req = api_rufengda.InventoryQuery(post_body,TEST_HOST,TEST_PORT) 
        else:
            identity = ICP.get_param(cr,uid,'nt_rufengda.identity')
            secret = ICP.get_param(cr,uid,'nt_rufengda.secret')
            req = api_rufengda.InventoryQuery(post_body) 
        req.set_app_info(identity,secret)
        resp_msg = req.getResponse()
        return resp_msg
    
    #供应商同步接口
    def supplier_sync(self,cr,uid,post_body,context={}):
        ICP = self.pool.get('ir.config_parameter')
        is_dev_env = False if str(ICP.get_param(cr,uid,'nt_rufengda.is_dev_env'))=='False' else True
        if is_dev_env:
            identity = ICP.get_param(cr,uid,'nt_rufengda.test_identity')
            secret = ICP.get_param(cr,uid,'nt_rufengda.test_secret')
            req = api_rufengda.SupplierSync(post_body,TEST_HOST,TEST_PORT) 
        else:
            identity = ICP.get_param(cr,uid,'nt_rufengda.identity')
            secret = ICP.get_param(cr,uid,'nt_rufengda.secret')
            req = api_rufengda.SupplierSync(post_body) 
        req.set_app_info(identity,secret)
        resp_msg = req.getResponse()
        return resp_msg
    
    #基础信息接口
    def clothes_process(self,cr,uid,post_body,context={}):
        ICP = self.pool.get('ir.config_parameter')
        is_dev_env = False if str(ICP.get_param(cr,uid,'nt_rufengda.is_dev_env'))=='False' else True
        if is_dev_env:
            identity = ICP.get_param(cr,uid,'nt_rufengda.test_identity')
            secret = ICP.get_param(cr,uid,'nt_rufengda.test_secret')
            req = api_rufengda.ClothesProcess(post_body,TEST_HOST,TEST_PORT) 
        else:
            identity = ICP.get_param(cr,uid,'nt_rufengda.identity')
            secret = ICP.get_param(cr,uid,'nt_rufengda.secret')
            req = api_rufengda.ClothesProcess(post_body) 
        req.set_app_info(identity,secret)
        resp_msg = req.getResponse()
        return resp_msg
    
    #运单信息接口
    def get_waybillno_status(self,cr,uid,post_body,context={}):
        ICP = self.pool.get('ir.config_parameter')
        is_dev_env = False if str(ICP.get_param(cr,uid,'nt_rufengda.is_dev_env'))=='False' else True
        if is_dev_env:
            identity = ICP.get_param(cr,uid,'nt_rufengda.test_identity')
            secret = ICP.get_param(cr,uid,'nt_rufengda.test_secret')
            req = api_rufengda.GetWaybillNoStatus(post_body,TEST_HOST,TEST_PORT) 
        else:
            identity = ICP.get_param(cr,uid,'nt_rufengda.identity')
            secret = ICP.get_param(cr,uid,'nt_rufengda.secret')
            req = api_rufengda.GetWaybillNoStatus(post_body) 
        req.set_app_info(identity,secret)
        resp_msg = req.getResponse()
        return resp_msg
    
