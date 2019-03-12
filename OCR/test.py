#!/usr/bin/env python
# encoding: utf-8
'''
@author: yihuixiong
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: deamoncao100@gmail.com
@software: garner
@file: test.py
@time: 2019/3/8 14:56
@desc:
'''
import re
import unicodedata
import sys
reload(sys)
sys.setdefaultencoding('utf8')

L = ['aa' , 'fm', 'ha', '你好', '易惠雄']
s = "|".join(L)

s1 = '(?:{name})'.format(name = s)

print s1
result = re.finditer(s1,'aakjbafakjca你好a易惠雄aca')

print [(x.group(), x.start(), x.end()) for x in result]
