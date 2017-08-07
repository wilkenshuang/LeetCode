# -*- coding: utf-8 -*-
"""
Created on Mon Aug  7 19:47:30 2017

@author: wilkenshuang
"""

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        

        if x<0:
            word=str(abs(x))
            reverse_word=-int(word[::-1])
        else:
            word=str(x)
            reverse_word=int(word[::-1])
        if abs(reverse_word)>2**31:
            return 0    
        return reverse_word