'''
Given an array arr of n integers. Your task is to write a program to find the maximum value of ∑arr[i]*i, where
i = 0, 1, 2,., n-1. You are allowed to rearrange the elements of the array.
Note: Since the output could be large, print the answer modulo 109+7.
'''
class Solution:
    def Maximize(self,arr):
        arr.sort()
        MOD=1000000007
        val=0
        for i in range(len(arr)):
            val+=(arr[i]*i)
        return val%MOD
arr = [5, 3, 2, 4, 1]
print(Solution().Maximize(arr))