# -*- coding: utf-8 -*-
"""
Created on Sun Aug 13 14:46:04 2017

@author: wilkenshuang
"""

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxArea=0
        left,right=0,len(height)-1
        while left<right:
            Weight=right-left
            Height=min(height[left],height[right])
            maxArea=max(Weight*Height,maxArea)
            if height[left]<=height[right]:
                left=left+1
            elif height[left]>height[right]:
                right=right-1
        return maxArea