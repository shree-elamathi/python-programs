'''
Given an array of Intervals arr[][], where arr[i] = [starti, endi]. The task is to merge all of the
overlapping Intervals.
'''


class Solution:
    def mergeOverlap(self, arr):
        arr.sort()
        res = []
        i = 0
        j = 1
        n = len(arr)
        print(arr)
        while i < n - 1 and j < n:
            newInterval = [0, 0]
            if arr[i][1] < arr[j][0]:
                res.append(arr[i])
                i += 1
                j += 1
                print(res)
            else:
                newInterval[0] = arr[i][0]
                newInterval[1] = max(arr[i][1], arr[j][1])
                if newInterval not in res:
                    res.append(newInterval)
                j += 1
                arr[i] = newInterval
        return res


arr = [[1,3],[2,4],[6,8],[9,10]]
print(Solution().mergeOverlap(arr))
