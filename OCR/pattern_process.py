#!/usr/bin/env python
# encoding: utf-8
'''
@author: yihuixiong
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: deamoncao100@gmail.com
@software: garner
@file: pattern_process.py
@time: 2019/3/10 14:29
@desc:
'''
import re

def list2pattern(list):
    """convert list 2 a pattern"""
    s = "|".join(list)
    return re.compile('(?:{pattern})'.format(pattern = s))

def get_word_position(pattern, sentence):
    """根据pattern 返回结果"""
    result = pattern.finditer(sentence)
    return [ (x.group(),x.start(),x.end())for x in result]


class Pattern():
    def __init__(self, entity_list, property_list):
        self._entity_list = entity_list
        self._property_list = property_list
        self._entity_pattern = list2pattern(self._entity_list)
        self._property_pattern = list2pattern(self._property_list)

    def match_keywords(self,sentence):

        # 非元组捕获语
        entity_result = list2pattern(self._entity_pattern, sentence)
        property_result = list2pattern(self._property_pattern, sentence)

def read_from_txt(path):
    word_list = []
    with open(path, "rt") as f:
        word_list = [ x[:-1].strip() for x in f]




    return  word_list

if __name__ == '__main__':
    entity_list = read_from_txt("")
    pattern = Pattern(entity_list= )

    