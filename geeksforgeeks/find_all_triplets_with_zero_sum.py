'''
Given an array arr[], find all possible indices [i, j, k] of triplets [arr[i], arr[j], arr[k]] in the array whose sum
is equal to zero. Return indices of triplets in any order and all the returned triplets indices should also be
internally sorted, i.e., for any triplet indices [i, j, k], the condition i < j < k should hold.
Note: Try to solve this using the O(n2) approach.
'''
#User function Template for python3
class Solution:
    def findTriplets(self, arr):
        from collections import defaultdict
        n = len(arr)
        def collect(i):
            target, m = -arr[i], defaultdict(list)
            for j in range(i+1, n):
                if target - arr[j] in m:
                    for idx in m[target-arr[j]]:
                        yield i, idx, j
                m[arr[j]].append(j)
        for i in range(n):
            yield from collect(i)


arr = [0, -1, 2, -3, 1]
print(Solution().findTriplets(arr))