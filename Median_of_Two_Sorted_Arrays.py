# -*- coding: utf-8 -*-
"""
Created on Mon Aug  7 15:01:30 2017

@author: wilkenshuang
"""

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums1.extend(nums2)
        full=nums1
        full.sort()
        n=len(full)
        integer,remainder=divmod(n,2)
        if remainder==1:
            median_ind=int((n+1)/2-1)
            median=full[median_ind]
        else:
            median1_ind=int(n/2)
            median2_ind=int(n/2-1)
            median=float(full[median1_ind]+full[median2_ind])/2
        return median