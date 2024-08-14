'''
The distance of a pair of integers a and b is defined as the absolute difference between a and b.
Given an integer array nums and an integer k, return the kth smallest distance among all the pairs nums[i] and
nums[j] where 0 <= i < j < nums.length.
'''
class Solution:
    def count_pairs(self,nums, mid):
        count = 0
        j = 0
        n = len(nums)

        for i in range(n):
            while j < n and nums[j] - nums[i] <= mid:
                j += 1
            count += j - i - 1
        return count
    def smallestDistancePair(self,nums,k):
        nums.sort()
        low, high = 0, nums[-1] - nums[0]

        while low < high:
            mid = (low + high) // 2
            if self.count_pairs(nums,mid)< k:
                low = mid + 1
            else:
                high = mid

        return low
nums = [1,6,1]
k = 3
print(Solution().smallestDistancePair(nums,k))