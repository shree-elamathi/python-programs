'''
find the floor (largest number in an array which is less than or equal to target) and ceil (smallest number in an array
which is greater than or equal to target)
'''

class Solution:
    def floorAndCeil(self, arr, x, n):
        low = 0
        high = n - 1
        floor = -1

        while low <= high:
            mid = low + (high - low) // 2

            if arr[mid] <= x:
                floor = arr[mid]
                low = mid + 1

            else:
                high = mid - 1

        low = 0
        high = n - 1
        ceil = -1

        while low <= high:
            mid = low + (high - low) // 2

            if arr[mid] >= x:
                ceil = arr[mid]
                high = mid - 1

            else:
                low = mid + 1

        print(floor, ceil)


arr = [10,20,30,40,50]
x = 25
n = len(arr)
Solution().floorAndCeil(arr,x,n)