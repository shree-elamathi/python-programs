'''
Given an array arr[] with non-negative integers representing the height of blocks. If the width of each block is 1,
compute how much water can be trapped between the blocks during the rainy season.
'''


class Solution:
    def maxWater(self, arr):
        if len(arr) < 3:
            return 0
        left, right = 0, len(arr) - 1
        left_max, right_max = arr[left], arr[right]
        trapped_water = 0
        while left < right:
            if left_max < right_max:
                left += 1
                left_max = max(left_max, arr[left])
                trapped_water += max(0, left_max - arr[left])
            else:
                right -= 1
                right_max = max(right_max, arr[right])
                trapped_water += max(0, right_max - arr[right])
        return trapped_water


arr = [3, 0, 1, 0, 4, 0, 2]
print(Solution().maxWater(arr))
