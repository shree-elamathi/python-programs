'''
Given a sorted array arr[] of positive integers, find the smallest positive integer such that it cannot be
represented as the sum of elements of any subset of the given array set.
'''
class Solution:
    def findSmallest(self, arr):
        res=1
        for num in arr:
            if num>res:
                break
            res+=num
        return res


arr = [1, 2, 3]
print(Solution().findSmallest(arr))