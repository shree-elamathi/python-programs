'''
Given an integer array nums, find the maximum possible bitwise OR of a subset of nums and return the number of
different non-empty subsets with the maximum bitwise OR.
An array a is a subset of an array b if a can be obtained from b by deleting some (possibly zero) elements of b.
Two subsets are considered different if the indices of the elements chosen are different.
The bitwise OR of an array a is equal to a[0] OR a[1] OR ... OR a[a.length - 1] (0-indexed).
'''


class Solution:
    def countMaxOrSubsets(self, nums):
        max_or = 0
        for num in nums:
            max_or |= num

        def count_subsets(i, current_or):
            if i == len(nums):
                return 1 if current_or == max_or else 0
            include = count_subsets(i + 1, current_or | nums[i])
            exclude = count_subsets(i + 1, current_or)
            return include + exclude
        return count_subsets(0, 0)


nums = [3,1]
print(Solution().countMaxOrSubsets(nums))