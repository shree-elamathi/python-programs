'''
You are given a non-empty array of integers nums. Every integer appears twice except for one.

Return the integer that appears only once.

You must implement a solution with O(n) runtime complexity and use only O(1) extra space.
'''


class Solution:
    def singleNumber(self, nums) :
        lst = []

        for i in nums:
            if i not in lst:
                lst.append(i)
            else:
                lst.remove(i)

        return lst[0]


nums = [3,2,3]
print(Solution().singleNumber(nums))


