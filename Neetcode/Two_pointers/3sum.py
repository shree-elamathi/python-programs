'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] where nums[i]+nums[j]+nums[k] == 0,
and the indices i, j and k are all distinct.
The output should not contain any duplicate triplets. You may return the output and the triplets in any order.
'''


class Solution:
    def threeSum(self, nums):
        nums.sort()
        ans = []
        n = len(nums)
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i+1, n-1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s > 0:
                    r -= 1
                elif s < 0:
                    l += 1
                else:
                    ans.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    if l < r and nums[l] == nums[l-1]:
                        l += 1
                    if l < r and nums[r] == nums[r+1]:
                        r -= 1
        return ans


nums = [0,0,0]
print(Solution().threeSum(nums))