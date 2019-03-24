# coding=UTF-8
# scale_conversion.py

"""
- id 压缩方案, 用于生成标签暗码
    - 把id转成36进制
    - 4位可用 36 ** 4   = 1679616 情况
- 提供36转10进制func
"""


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


def baseNto10(s, n=36):
    """
        N进制 -> 十进制
    """
    chars = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    depth = res = 0
    for char in s[::-1]:
        res += chars.index(char) * (n ** depth)
        depth += 1
    return res
