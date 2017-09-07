#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/9/7 19:47
# @Author  : Wilkenshuang
# @File    : test.py
# @Software: PyCharm Community Edition

'''
Question description:
Given an array of strings, group anagrams together.

For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"], 
Return:

[
  ["ate", "eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note: All inputs will be in lower-case.
'''

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        buff_dic={}
        for i in sorted(strs):
            sortedItem=''.join(sorted(i))
            buff_dic[sortedItem]=buff_dic.get(sortedItem,[])+[i]
        return buff_dic.values()
