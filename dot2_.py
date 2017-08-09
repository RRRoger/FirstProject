# # -*- encoding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8') 

"""
    shell order:
        change `.` to `_`
    append `alias dot2_='python /Users/chenpeng/FirstProject/dot2_.py'` 
        @ ending of file `.bash_profile`
"""

def get_words():
    return sys.argv[1:]

def dot2_():
    words = get_words()
    for i in words:
        abbreviation = ''
        for r in i.split('.'):
            abbreviation += r[0]
        print i.replace('.', '_'), abbreviation
dot2_()

