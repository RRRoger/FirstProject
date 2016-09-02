'''
Created by auto_sdk on 2016.01.20
'''
from base import RestApi
class rt_inventory_query_service(RestApi):
    def __init__(self,post_body=None,domain='bsp.sit.sf-express.com',port=80):
        RestApi.__init__(self,post_body,domain, port)
        
    def getapiname(self):
        return 'RT_INVENTORY_QUERY_SERVICE'