# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 23:22:49 2017

@author: wilkenshuang
"""

class solution:
    def twosum(self,num,target):
        if len(num)<=1:
            return False
        buff_dict={}
        for i in range(len(num)):
            if num[i] in buff_dict:
                return [buff_dict[num[i]],i]
            else:
                buff_dict[target-num[i]]=i
