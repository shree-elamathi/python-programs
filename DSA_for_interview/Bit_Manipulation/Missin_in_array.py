'''
You are given an array arr of size n - 1 that contains distinct integers in the range from 1 to n (inclusive).
This array represents a permutation of the integers from 1 to n with one element missing. Your task is to identify
and return the missing element.
'''


class Solution:
    def missingNumber(self, arr):
        n = len(arr) + 1
        arr_sum = sum(arr)
        new_sum = (n * (n + 1)) // 2
        ans = new_sum - arr_sum
        return ans


arr = [1, 2, 3, 5]
print(Solution().missingNumber(arr))
