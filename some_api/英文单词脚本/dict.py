# # -*- encoding: utf-8 -*-

# ==================
# 用法, python dict.py yourword
#
#
# ==================


import sys
reload(sys)
sys.setdefaultencoding('utf-8') 
import json
import requests
"""
	1. 用法,pyhton dict.py English
"""
def send_post():
	if len(sys.argv) < 2:
		print u"命令参考: python dict.py yourword"
		return ""
	word = sys.argv[1]
	print word,':'
	url_prefix = "https://api.shanbay.com/bdc/search/?word="
	url = url_prefix + word
	response = requests.get(url)
	res = response.json()
	data = res.get('data',False)
	if data:
		pronunciations_uk = data['pronunciations']['uk']
		pronunciations_us = data['pronunciations']['us']
		definition = data['definition']
		return definition
	else:
		return u"无此单词"

print send_post()
