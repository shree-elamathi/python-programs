'''
Given a array of positive integers arr, where each element denotes the maximum length of jump you can cover. Find
out if you can make it to the last index starting from the first index of the list, return true if you can reach the
last index.
'''

class Solution:
    def canReach(self, arr):
        farthest = 0
        n = len(arr)

        for i in range(n):
            if i > farthest:
                return False
            farthest = max(farthest, i + arr[i])
            if farthest >= n - 1:
                return True

        return False

arr = [2, 3, 1, 1, 4]
print(Solution().canReach(arr))