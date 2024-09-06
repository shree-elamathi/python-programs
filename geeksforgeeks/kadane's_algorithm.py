'''
Given an integer array arr[]. Find the contiguous sub-array(containing at least one number) that has the maximum
sum and return its sum.
'''
class Solution:
    def maxSubArraySum(self,arr):
        max_sum = arr[0]
        current_sum = arr[0]
        for i in range(1,len(arr)):
            current_sum=max(arr[i],current_sum+arr[i])
            max_sum=max(max_sum,current_sum)
        return max_sum
arr= [1, 2, 3, -2, 5]
print(Solution().maxSubArraySum(arr))