# -*- coding: utf-8 -*-
import re

"""
简单的集合处理函数
"""

# 集合常用符号 ∪, ∩, ∞

INF_PLUS = float('inf') # 正无穷
INF_MINES = float('-inf') # 负无穷

rule = "(-∞, -600]∪[600, +∞)"

_map = {
    '(': ' < ',
    '[': ' <= ',
    ')': ' < ',
    ']': ' <= ',
}

replace_str = {
    ' ': '',
    '∪': ' or ',
    '∩': 'and ',
    '-∞': ' INF_MINES ',
    '+∞': ' INF_PLUS ',
}

def test(num, rule=''):
    
    for key, val in replace_str.items():
        rule = rule.replace(key, val)

    cols = re.findall(r'[\(\[].*?[\)\]]', rule)
    for x in cols:
        el = re.findall(r'([\(\[])(.*?),(.*?)([\)\]])', x)[0]
        # print(el[0])
        expression = "%s %s %s %s %s" % (el[1], _map[el[0]], num, _map[el[3]], el[2])
        print("%s : %s" % (expression, eval(expression)))

    return False

test(0, rule)
# print(re.findall(r'[\(\[].*?[\)\]]', rule))



