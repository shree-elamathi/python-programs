'''
Given an array arr[] such that each element is in the range [0 - 9], find the minimum possible sum of two numbers
formed using the elements of the array. All digits in the given array must be used to form the two numbers.
Return a string without leading zeroes.
'''


class Solution:
    def minSum(self, arr):
        arr.sort()
        if len(arr) == 1:
            return arr[0]
        val1 = ""
        val2 = ""
        for i in range(0, len(arr), 2):
            val1 += str(arr[i])
        for i in range(1, len(arr), 2):
            val2 += str(arr[i])
        val1 = int(val1)
        val2 = int(val2)
        return val1 + val2


arr = [6, 8, 4, 5, 2, 3]
print(Solution().minSum(arr))