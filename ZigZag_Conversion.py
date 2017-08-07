# -*- coding: utf-8 -*-
"""
Created on Mon Aug  7 20:17:52 2017

@author: wilkenshuang
"""

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if len(s)<=numRows or numRows==1:
            return s
        L = [''] * numRows
        index, step = 0, 1
        for x in s:
            L[index]+=x
            if index==0:
                step=1
            elif index==numRows-1:
                step=-1
            index+=step
        return ''.join(L)
    