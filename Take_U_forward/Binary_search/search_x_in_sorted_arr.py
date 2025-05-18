'''
Search an element in a sorted array using binary search
'''

class Solution:
    def binarySearch(self, nums, x):
        low = 0
        high = len(nums) - 1

        while low <= high:

            mid = low + ( high - low ) // 2

            if nums[mid] == x:
                return mid

            elif nums[mid] < x:
                low = mid + 1

            else:
                high = mid - 1

        return -1


nums = [2,4,6,8,9,12,14,16]
x = 14
print(Solution().binarySearch(nums,x))