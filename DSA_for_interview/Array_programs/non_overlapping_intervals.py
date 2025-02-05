'''
Given N set of time intervals, the task is to find the intervals which don’t overlap with the given set of intervals.
'''

class Solution:
    def findFreeinterval(self,arr):
        res = []
        for i in range(1, len(arr)):
            prevEnd = arr[i-1][1]
            curStart = arr[i][0]
            if prevEnd < curStart:
                res.append([prevEnd , curStart])
        return res


arr = [[1, 3], [2, 4],
       [3, 5], [7, 9]]
print(Solution().findFreeinterval(arr))