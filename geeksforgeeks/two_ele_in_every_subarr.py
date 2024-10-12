'''
Given an array of integers arr, the task is to find and return the maximum sum of the smallest and second smallest
element among all possible subarrays of size greater than one. If it is not possible, then return -1.
'''
class Solution:
    def pairWithMaxSum(self, arr):
        if len(arr)<2:
            return "-1"
        max_sum=arr[0]+arr[1]
        for i in range(1,len(arr)-1):
            cur_sum=arr[i]+arr[i+1]
            max_sum=max(max_sum,cur_sum)
        return max_sum


arr = [4, 3, 1, 5, 6]
print(Solution().pairWithMaxSum(arr))