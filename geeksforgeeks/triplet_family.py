'''
Given an array arr of integers. Find whether three numbers are such that the sum of two elements equals the
third element.
'''

class Solution:
    def findTriplet(self, arr):
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                if arr[i] + arr[j] in arr:
                    return True
        return False


arr= [1, 2, 3, 4, 5]
print(Solution().findTriplet(arr))