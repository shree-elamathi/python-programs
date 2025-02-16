'''
Given an array arr[] of non-negative integers. Find the length of the longest sub-sequence such that elements
in the subsequence are consecutive integers, the consecutive numbers can be in any order.
'''


class Solution:
    def longestConsecutive(self, arr):
        helper = {}
        for num in arr:
            if num in helper:
                helper[num] += 1
            else:
                helper[num] = 1
        length = 0
        for num in arr:
            temp = 1
            x = num + 1
            while x in helper:
                temp += 1
                x += 1
            length = max(temp, length)
        return length


arr = [2, 6, 1, 9, 4, 5, 3]
print(Solution().longestConsecutive(arr))