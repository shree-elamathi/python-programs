'''
You are given an array of length n which was originally sorted in ascending order. It has now been rotated
between 1 and n times. For example, the array nums = [1,2,3,4,5,6] might become:

[3,4,5,6,1,2] if it was rotated 4 times.
[1,2,3,4,5,6] if it was rotated 6 times.
Notice that rotating the array 4 times moves the last four elements of the array to the beginning. Rotating the
array 6 times produces the original array.

Assuming all elements in the rotated sorted array nums are unique, return the minimum element of this array.
'''


class Solution:
    def findMin(self, arr):
        minVal = arr[0]
        lo, hi = 0, len(arr) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if (arr[mid] < minVal):
                minVal = arr[mid]
            if (arr[lo] < minVal):
                minVal = arr[lo]
            if (arr[hi] < minVal):
                minVal = arr[hi]
            if (arr[mid] >= arr[lo]):
                lo = mid + 1
            else:
                hi = mid - 1

        return minVal

arr = [2, 3, 4, 5, 6, 1]
print(Solution().findMin(arr))