'''
You are given a sorted array arr[] of unique integers, an integer k, and a target value x. Return exactly k
elements from the array closest to x, excluding x if it exists.

An element a is closer to x than b if:

|a - x| < |b - x|, or
|a - x| == |b - x| and a > b (i.e., prefer the larger element if tied)

Return the k closest elements in order of closeness.
'''

class Solution:
    def printKClosest(self, arr, k, x):
        newArr =[]
        newSet = {}
        res = []
        for i in arr:
            newArr.append(abs(i-x))
        for i in range(len(arr)):
            if newArr[i] not in newSet:
                newSet[newArr[i]] = [arr[i]]
            else:
                newSet[newArr[i]].append(arr[i])
        newArr.sort()
        for i in range(len(arr)):
            if (len(res) >= k):
                return res
            if (newArr[i] != 0):
                res.append(max(newSet[newArr[i]]))
                newSet[newArr[i]].remove(max(newSet[newArr[i]]))


arr = [1, 3, 5, 7, 9]
k = 2
x = 6
print(Solution().printKClosest(arr,k,x))