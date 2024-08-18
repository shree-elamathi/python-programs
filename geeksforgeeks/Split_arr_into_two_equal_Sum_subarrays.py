'''
Given an array of integers arr, return true if it is possible to split it in two subarrays (without reordering the
elements), such that the sum of the two subarrays are equal. If it is not possible then return false.
'''
class Solution:
    def canSplit(self, arr):
        total_sum=sum(arr)
        left_sum=0
        for i in range(len(arr)-1):
            left_sum+=arr[i]
            right_sum=total_sum-left_sum
            if left_sum==right_sum:
                return True
        return False
arr=[4, 3, 2, 1]
print(Solution().canSplit(arr))