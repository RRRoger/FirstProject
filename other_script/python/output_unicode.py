# coding=UTF-8
# scale_conversion.py


def base10toN(num, n=36):
    """
        十进制 -> N进制
    """
    chars = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    res = ''
    current = num
    while current != 0:
        res = chars[current % n] + res
        current = current / n
    return res


def format_16(num, length=8, n=16):
    """
    id转成定长16位字符, 8位, 少的用0补齐
    :param num:
    :param length:
    :return:
    """
    return ('0' * length + base10toN(num, n))[-length:]

RANGE = [126976,127123]

def output_unicode(_range):
    _range[1] += 1
    # print _range
    for i in range(*_range):
        # print format_16(i)
        uni = format_16(i)
        s = u'\\U%s' % uni
        # print i, uni, 
        # try:
        #     exec "print u'%s'" % s
        # except:
        #     print "print u'%s'" % s
        # print "print u'i=%s;uni=%s;s=\"%s\"'" % (i, uni, s)
        exec "print u'%s'," % (s, )


if __name__ == '__main__':
    # output_unicode(RANGE)
    output_unicode(RANGE)

