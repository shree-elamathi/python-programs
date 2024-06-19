'''
You are given a perimeter & the area. Your task is to return the maximum volume that can be made in the form
of a cuboid from the given perimeter and surface area.
Note: Round off to 2 decimal places and for the given parameters, it is guaranteed that an answer always exists.
'''
import math


class Solution:
    def maxVolume(self, perimeter, area):
        d = perimeter * perimeter - 24 * area
        l = (perimeter - math.sqrt(d)) / 12
        h = (perimeter / 4) - 2 * l
        return l * l * h
p=22
a=15
print(Solution().maxVolume(p,a))