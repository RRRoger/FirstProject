_author__ = 'CQC'
# -*- coding:utf-8 -*-
 
import urllib
import urllib2
import re
 
class Spider:
 
    def __init__(self):
        self.siteURL = 'http://mm.taobao.com/json/request_top_list.htm'
 
    def getPage(self,pageIndex):
        url = self.siteURL + "?page=" + str(pageIndex)
        print url
        request = urllib2.Request(url)
        response = urllib2.urlopen(request)
        xx = response.read()
        return xx.decode('gbk')
 
    def getContents(self,pageIndex):
        page = self.getPage(pageIndex)
        # print page
        pattern = re.compile('<div class="list-item".*?pic-word.*?<a href="(.*?)".*?<img src="(.*?)".*?<a class="lady-name.*?>(.*?)</a>.*?<strong>(.*?)</strong>.*?<span>(.*?)</span>',re.S)
        items = re.findall(pattern,page)
        print items
        for item in items:
            print item[0],item[1],item[2],item[3],item[4]
 
# spider = Spider()
# spider.getContents(2)
pattern = re.compile('1(.*?)2(.*?)3(.*?)4',re.S)
print re.S
print re.M
print re.I 
x = re.findall(pattern,'1qwe2asd3asd41qwe2asd3asd41qwe2asd3asd4')
print type(x)
print x
