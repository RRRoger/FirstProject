# # -*- encoding: utf-8 -*-
import sys
import re
import requests

reload(sys)
sys.setdefaultencoding('utf-8')


FILE_NAME = 'YOUR_NOTE.txt'


def _to_str(ctx):
    return ctx


def get_word():
    return sys.argv[0]


def send_post():
    word = get_word()
    url_prefix = "https://api.shanbay.com/bdc/search/?word="
    url = url_prefix + word
    response = requests.get(url)
    # print response.text
    res = response.json()
    # try:
    data = res['data']
    pronunciations_uk = data['pronunciations']['uk']
    pronunciations_us = data['pronunciations']['us']
    definition = data['definition']

    fobj = open(FILE_NAME, 'a')
    fobj = open(FILE_NAME, 'r')
    txt = fobj.read()
    print txt
    print r'单词:%s' % word, '========================='
    if re.match(r'单词\:%s' % word, txt):
        print 'asd'
        return definition
    fobj = open(FILE_NAME, 'a')
    fobj.write(u'\n单词:%s' % word)
    fobj.write(u'\n美式发音:%s' % pronunciations_us)
    fobj.write(u'\n英式发音:%s' % pronunciations_uk)
    fobj.write(u'\n中文意思:%s' % definition)
    fobj.write(u'\n')
    fobj.close()
    # except:
    # 	return u'查无此词'
    return definition


print send_post()
