'''
Given an array arr of integers, find all the elements that occur more than once in the array. If no element repeats,
return an empty array.
'''


class Solution:
    def findDuplicates(self, arr):
        newSet = {}
        for i in arr:
            if i not in newSet:
                newSet[i] = 1
            else:
                newSet[i] = newSet[i] + 1

        res = []
        for key in newSet.keys():
            if newSet[key] > 1:
                res.append(key)

        return res


arr = [2, 3, 1, 2, 3]
print(Solution().findDuplicates(arr))