'''
Given an integer array nums and an integer k, return true if nums has a good subarray or false otherwise.
A good subarray is a subarray where:
its length is at least two, and
the sum of the elements of the subarray is a multiple of k.
Note that:
A subarray is a contiguous part of the array.
An integer x is a multiple of k if there exists an integer n such that x = n * k. 0 is always a multiple of k.
'''
class Solution:
    def check_subarr(self,nums,k):
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                arr=nums[i:j+1]
                if sum(arr)%k==0:
                    return True
        return False
k=13
nums=[23,2,6,4,7]
print(Solution().check_subarr(nums,k))