'''
Given an array of integers nums and an integer k. A continuous subarray is called nice if there are k odd
numbers on it.
Return the number of nice sub-arrays.
'''
class Solution:
    def numberOfSubarrays(self, nums, k):
        n = len(nums)
        res = 0
        odd_count = 0
        left = 0
        for right in range(n):
            if nums[right] % 2 != 0:
                odd_count += 1
            while odd_count > k:
                if nums[left] % 2 != 0:
                    odd_count -= 1
                left += 1
            if odd_count == k:
                res += 1
                temp = left
                while temp < right and nums[temp] % 2 == 0:
                    res += 1
                    temp += 1
        return res
nums = [1,1,2,1,1]
k = 3
print(Solution().numberOfSubarrays(nums,k))