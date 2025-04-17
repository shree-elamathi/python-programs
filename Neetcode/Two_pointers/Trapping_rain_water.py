'''
You are given an array non-negative integers height which represent an elevation map. Each value height[i] represents
the height of a bar, which has a width of 1.
Return the maximum area of water that can be trapped between the bars.
'''


class Solution:
    def trap(self, height) :
        n = len(height)
        if len(height) < 1:
            return 0
        l , r = 0, n-1
        lm, rm = height[l], height[r]
        trapped_water = 0
        while l < r:
            if lm<rm:
                l += 1
                lm = max(lm, height[l])
                trapped_water += max(0, lm - height[l] )
            else:
                r -= 1
                rm = max(rm, height[r])
                trapped_water += max(0, rm - height[r] )
        return trapped_water


height = [0,2,0,3,1,0,1,3,2,1]
print(Solution().trap(height))