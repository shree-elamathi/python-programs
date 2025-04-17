'''
You are given an integer array heights where heights[i] represents the height of the i th bar.
You may choose any two bars to form a container. Return the maximum amount of water a container can store.
'''


class Solution:
    def maxArea(self, arr) :
        n = len(arr)
        trapped_water = 0
        l, r = 0, n-1
        lm , rm = arr[l] , arr[r]
        while l < r:
            if lm < rm:
                val = min(lm, rm)
                trapped_water = max(trapped_water, val * (r - l))
                l += 1
                lm = arr[l]
            else:
                val = min(lm, rm)
                trapped_water = max(trapped_water, val * (r - l))
                r -= 1
                rm = arr[r]
        return trapped_water


height = [1,2]
print(Solution().maxArea(height))