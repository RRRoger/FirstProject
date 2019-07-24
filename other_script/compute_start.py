# -*- encoding: utf-8 -*-

def _get_stars(date):
    res = ''
    star_key = {
        1: ('摩羯座', '水瓶座'),
        2: ('水瓶座', '双鱼座'),
        3: ('双鱼座', '白羊座'),
        4: ('白羊座', '金牛座'),
        5: ('金牛座', '双子座'),
        6: ('双子座', '巨蟹座'),
        7: ('巨蟹座', '狮子座'),
        8: ('狮子座', '处女座'),
        9: ('处女座', '天秤座'),
        10: ('天秤座', '天蝎座'),
        11: ('天蝎座', '射手座'),
        12: ('射手座', '摩羯座'),
    }
    month = int(date[:2])
    day = int(date[3:])
    if day < 20:
        res = star_key[month][0]
    else:
        res = star_key[month][1]
    return res

print _get_stars('10-26')