# coding=UTF-8
# scale_conversion.py

"""
- id 压缩方案, 用于生成标签暗码
    - 把id转成36进制
    - 4位可用 36 ** 4   = 1679616 情况
- 提供36转10进制func
"""

CHARS = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def base10toN(num, n=36):
    """
        十进制 -> N进制
    """
    chars = CHARS
    res = ''
    current = num
    while current != 0:
        res = chars[current % n] + res
        current = current / n
    return res


def baseNto10(s, n=36):
    """
        N进制 -> 十进制
    """
    chars = CHARS
    depth = res = 0
    for char in s[::-1]:
        res += chars.index(char) * (n ** depth)
        depth += 1
    return res



if __name__ == '__main__':
    J = 36
    number = 10000

    num_char = base10toN(number, J)
    new_num = baseNto10(num_char, J)

    print "origin number", number
    print "number char", num_char
    print "number after converse", new_num

# 0PR2KKCWX
# 0PR2KMI2F
# 0PUAC8SMV
# 0PU9SPS01
# 0D2VMJ9Q9
# 0CRE66I9S
# 3JLXPT2PS
# 3JLXPT2PR



