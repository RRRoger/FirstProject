'''
Created by auto_sdk on 2016.01.20
'''
from base import RestApi
class ClothesProcess(RestApi):
    def __init__(self,post_body=None,domain='wmsedi.wuliusys.com',port=80):
        RestApi.__init__(self,post_body,domain, port)
        
    def getapiname(self):
        return '/clothes/ClothesProcessV2'