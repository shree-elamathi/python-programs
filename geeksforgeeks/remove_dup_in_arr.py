'''
Given an array arr consisting of positive integers numbers, remove all duplicates numbers.
'''


class Solution:
    def removeDuplicates(self, arr):
        arr1 = []
        for i in arr:
            if i not in arr1:
                arr1.append(i)
        return arr1


arr = [2, 2, 3, 3, 7, 5]
print(Solution().removeDuplicates(arr))