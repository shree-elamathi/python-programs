'''
Given a sorted integer array nums and an integer n, add/patch elements to the array such that any number
in the range [1, n] inclusive can be formed by the sum of some elements in the array.
Return the minimum number of patches required.
'''
class Solution:
    def minPatches(self, nums, n):
        miss = 1
        added = 0
        i = 0
        while miss <= n:
            if i < len(nums) and nums[i] <= miss:
                miss += nums[i]
                i += 1
            else:
                miss += miss
                added += 1
        return added

nums=[1,3]
n=6
print(Solution().minPatches(nums,n))