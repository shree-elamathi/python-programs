'''
Given an unsorted array arr and a number k which is smaller than the size of the array. Return true if the array
contains any duplicate within k distance throughout the array else false.
'''


class Solution:
    def checkDuplicatesWithinK(self, arr, k):
        seen = set()
        for i in range(len(arr)):
            if arr[i] in seen:
                return True
            seen.add(arr[i])
            if i >= k:
                seen.remove(arr[i - k])
        return False


arr = [1, 2, 3, 4, 1, 2, 3, 4]
k = 3
print(Solution().checkDuplicatesWithinK(arr,k))
