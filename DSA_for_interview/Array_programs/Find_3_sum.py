'''
Given an array arr[], find all possible triplets i, j, k in the arr[] whose sum of elements is equals to
zero.
Returned triplet should also be internally sorted i.e. i<j<k.
'''

class Solution:
    def findTriplets(self, arr):
        res = set()
        n = len(arr)
        mp = {}
        for i in range(n):
            for j in range(i+1, n):
                s = arr[i] + arr[j]
                if s not in mp:
                    mp[s] = []
                mp[s].append((i,j))
        for i in range(n):
            rem = -arr[i]
            if rem in mp:
                for p in mp[rem]:
                    if p[1] != i and p[0] != i:
                        curr = sorted([i,p[0] , p[1]])
                        res.add(tuple(curr))
        return res


arr =  [0, -1, 2, -3, 1]
print(Solution().findTriplets(arr))