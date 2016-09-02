# -*- encoding: utf-8 -*-

from osv import fields,osv
import datetime,time
import pytz
import string
import logging
import datetime
import time
import json
import api_shunfeng

_logger = logging.getLogger(__name__)

TEST_HOST = "bsp.sit.sf-express.com"
TEST_PORT = 8080

def utc2local(str_utc_time):
        local_tz = pytz.timezone('Asia/Shanghai')
        utc_tz = pytz.timezone('UTC')
        utc_time = datetime.datetime.strptime(str_utc_time[0:19], '%Y-%m-%d %H:%M:%S')
        utc_time = utc_time.replace(tzinfo=utc_tz)
        local_time = utc_time.astimezone(local_tz)
        return local_time.strftime('%Y-%m-%d %H:%M:%S')

class shunfeng_api(osv.osv_memory):
    _name = 'nt.shunfeng.api'
    #顺丰真是坑爹啊!!!
    
    
    #供应商同步接口
    def vendor_service(self,cr,uid,vendors,context={}):
        ICP = self.pool.get('ir.config_parameter')
        final_data = {}
        VendorRequest = {}
        VendorRequest['CompanyCode'] = ICP.get_param(cr,uid,'nt_shunfeng.company_code') or ''
        VendorRequest['Vendors'] = {}
        VendorRequest['Vendors']['Vendor'] = vendors
        final_data['VendorRequest'] = VendorRequest
#         print final_data,'final_data'
        is_dev_env = False if str(ICP.get_param(cr,uid,'nt_shunfeng.is_dev_env'))=='False' else True
        if is_dev_env:
            accesscode = ICP.get_param(cr,uid,'nt_shunfeng.test_accesscode')
            checkword = ICP.get_param(cr,uid,'nt_shunfeng.test_checkword')
            req = api_shunfeng.vendor_service(final_data,TEST_HOST,TEST_PORT) 
        else:
            accesscode = ICP.get_param(cr,uid,'nt_shunfeng.accesscode')
            checkword = ICP.get_param(cr,uid,'nt_shunfeng.checkword')
            req = api_shunfeng.vendor_service(final_data) 
        req.set_app_info(accesscode , checkword )
        resp_msg = req.getResponse()
        print resp_msg
        return resp_msg
    
    #出库接口
    def sale_order_service(self,cr,uid,order_info,context={}):
        ICP = self.pool.get('ir.config_parameter')
        final_data = {}
        SaleOrderRequest = {}
        SaleOrderRequest['CompanyCode'] = ICP.get_param(cr,uid,'nt_shunfeng.company_code') or ''
        SaleOrderRequest['SaleOrders'] = {}
        SaleOrderRequest['SaleOrders']['SaleOrder'] = order_info
        final_data['SaleOrderRequest'] = SaleOrderRequest
#         print final_data,'final_data'
        is_dev_env = False if str(ICP.get_param(cr,uid,'nt_shunfeng.is_dev_env'))=='False' else True
        if is_dev_env:
            accesscode = ICP.get_param(cr,uid,'nt_shunfeng.test_accesscode')
            checkword = ICP.get_param(cr,uid,'nt_shunfeng.test_checkword')
            req = api_shunfeng.sale_order_service(final_data,TEST_HOST,TEST_PORT) 
        else:
            accesscode = ICP.get_param(cr,uid,'nt_shunfeng.accesscode')
            checkword = ICP.get_param(cr,uid,'nt_shunfeng.checkword')
            req = api_shunfeng.sale_order_service(final_data) 
        req.set_app_info(accesscode , checkword )
        resp_msg = req.getResponse()
        return resp_msg
    
    #库存查询接口,商品sku必选
    def rt_inventory_query_service(self,cr,uid,inventorys,warehouse_code,context={}):
        ICP = self.pool.get('ir.config_parameter')
        final_data = {}
        RTInventoryQueryRequest = {}
        RTInventoryQueryRequest['CompanyCode'] = ICP.get_param(cr,uid,'nt_shunfeng.company_code') or ''
        RTInventoryQueryRequest['WarehouseCode'] = warehouse_code
        RTInventoryQueryRequest['InventoryStatus'] = 10 #10正品 20产品
        RTInventoryQueryRequest['RTInventorys'] = {}
        RTInventoryQueryRequest['RTInventorys']['RTInventory'] = inventorys
        final_data['RTInventoryQueryRequest'] = RTInventoryQueryRequest
#         print final_data,'final_data'
        is_dev_env = False if str(ICP.get_param(cr,uid,'nt_shunfeng.is_dev_env'))=='False' else True
        if is_dev_env:
            accesscode = ICP.get_param(cr,uid,'nt_shunfeng.test_accesscode')
            checkword = ICP.get_param(cr,uid,'nt_shunfeng.test_checkword')
            req = api_shunfeng.rt_inventory_query_service(final_data,TEST_HOST,TEST_PORT) 
        else:
            accesscode = ICP.get_param(cr,uid,'nt_shunfeng.accesscode')
            checkword = ICP.get_param(cr,uid,'nt_shunfeng.checkword')
            req = api_shunfeng.rt_inventory_query_service(final_data) 
        req.set_app_info(accesscode , checkword )
        resp_msg = req.getResponse()
        if 'RTInventoryQueryResponse' in resp_msg and 'RTInventorys' in resp_msg['RTInventoryQueryResponse']:
            return resp_msg['RTInventoryQueryResponse']['RTInventorys']
        else:
            _logger.error('同步库存失败 编号:%s' % warehouse_code)
            return []
    
    #入库单接口
    def purchase_order_service(self,cr,uid,order_info,context={}):
        ICP = self.pool.get('ir.config_parameter')
        final_data = {}
        PurchaseOrderRequest = {}
        PurchaseOrderRequest['CompanyCode'] = ICP.get_param(cr,uid,'nt_shunfeng.company_code') or ''
        PurchaseOrderRequest['PurchaseOrders'] = {}
        PurchaseOrderRequest['PurchaseOrders']['PurchaseOrder'] = order_info
        final_data['PurchaseOrderRequest'] = PurchaseOrderRequest
#         print final_data,'final_data'
        is_dev_env = False if str(ICP.get_param(cr,uid,'nt_shunfeng.is_dev_env'))=='False' else True
        if is_dev_env:
            accesscode = ICP.get_param(cr,uid,'nt_shunfeng.test_accesscode')
            checkword = ICP.get_param(cr,uid,'nt_shunfeng.test_checkword')
            req = api_shunfeng.purchase_order_service(final_data,TEST_HOST,TEST_PORT) 
        else:
            accesscode = ICP.get_param(cr,uid,'nt_shunfeng.accesscode')
            checkword = ICP.get_param(cr,uid,'nt_shunfeng.checkword')
            req = api_shunfeng.purchase_order_service(final_data) 
        req.set_app_info(accesscode , checkword )
        resp_msg = req.getResponse()
        return resp_msg
    

