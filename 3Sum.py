'''
Problem Description:
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets 
in the array which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.

For example, given array S = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''

class Solution(object):
    def threeSum(self,nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        list=[]
        for i in range(len(nums)-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            l,r=i+1,len(nums)-1
            while l<r:
                Sum=nums[i]+nums[l]+nums[r]
                if Sum<0:
                    l+=1
                elif Sum>0:
                    r-=1
                else:
                  list.append([nums[i],nums[l],nums[r]])
                  while l<r and nums[l]==nums[l+1]:
                        l+=1
                  while l<r and nums[r]==nums[r-1]:
                        r-=1
                  l+=1;r-=1
        return list
