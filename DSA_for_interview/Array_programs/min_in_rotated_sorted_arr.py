'''
A sorted array of distinct elements arr[] is rotated at some unknown point, the task is to find the minimum
element in it.
'''


class Solution:
    def findMin(self, arr):
        lo, hi = 0, len(arr) - 1
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if (arr[lo]<arr[hi]):
                return arr[lo]
            if (arr[hi]<arr[mid]):
                lo = mid + 1
            if (arr[mid]<=arr[hi]):
                high = mid
        return min


arr = []
print(Solution().findMin(arr))