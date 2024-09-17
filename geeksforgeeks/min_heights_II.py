'''
Given an array arr[] denoting heights of N towers and a positive integer K.
For each tower, you must perform exactly one of the following operations exactly once.
Increase the height of the tower by K
Decrease the height of the tower by K
Find out the minimum possible difference between the height of the shortest and tallest towers after you have
modified each tower.
You can find a slight modification of the problem here.
Note: It is compulsory to increase or decrease the height by K for each tower. After the operation, the resultant
array should not contain any negative integers.
'''


class Solution:
    def getMinDiff(self, arr, K):
        n = len(arr)
        if n == 1:
            return 0

        arr.sort()

        ans = arr[-1] - arr[0]

        for i in range(1, n):
            if arr[i] - k < 0:
                continue

            maxi = max(arr[i - 1] + k, arr[-1] - k)
            mini = min(arr[0] + k, arr[i] - k)

            ans = min(ans, maxi - mini)

        return ans


k = 4
arr = [2, 4, 3, 9, 9, 10, 9, 7, 1, 2]
print(Solution().getMinDiff(arr, k))
