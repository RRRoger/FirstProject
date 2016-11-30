# # -*- encoding: utf-8 -*-


import sys
reload(sys)
sys.setdefaultencoding('utf-8') 
import json
import requests
"""
	1. 用法,pyhton dict.py English

	2.可以批量查询英文单词信息 pyhton dict.py English1 English2 English3
		update at 2016-11-26 00:28:53

"""
def send_post():
	if len(sys.argv) < 2:
		print u"命令参考: python dict.py yourword"
		return ""
	words = sys.argv[1:]
	# print words
	for word in words:
		print word,':'
		url = "https://api.shanbay.com/bdc/search/?word=" + word
		response = requests.get(url)
		res = response.json()
		data = res.get('data',False)
		if data:
			pronunciations_uk = data['pronunciations']['uk']
			pronunciations_us = data['pronunciations']['us']
			definition = data['definition']
			print definition
			print u"英式发音:",pronunciations_uk
			print u"美式发音:",pronunciations_us
			print ""
		else:
			print u"无此单词"
			print ""
	return ""

send_post()
