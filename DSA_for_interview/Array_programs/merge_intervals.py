'''
Given an array of Intervals arr[][], where arr[i] = [starti, endi]. The task is to merge all of the
overlapping Intervals.
'''


class Solution:
    def mergeOverlap(self, arr):
        arr.sort()
        resIndx = 0
        res=[]
        print(arr)
        for i in range(len(arr)):
            if arr[resIndx][1] >= arr[i][0]:
                arr[resIndx][1] = max(arr[resIndx][1], arr[i][1])
            else:
                resIndx += 1
                arr[resIndx] = arr[i]
        print(arr)
        for i in range(resIndx+1):
            res.append([arr[i][0],arr[i][1]])
        return res


arr = [[1,3],[2,4],[6,8],[9,10]]
print(Solution().mergeOverlap(arr))
