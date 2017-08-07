# -*- coding: utf-8 -*-
"""
Created on Sun Aug  6 22:08:03 2017

@author: wilkenshuang
"""

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start=maxLength=0
        usedChar={}
        for i in range (len(s)):
            if s[i] in usedChar and start<=usedChar[s[i]]:
                start=usedChar[s[i]]+1
            else:
                maxLength=max(maxLength,i-start+1)
            usedChar[s[i]]=i
        return maxLength