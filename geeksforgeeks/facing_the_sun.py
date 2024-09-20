'''
Given an array height representing the heights of buildings. You have to count the buildings that will see the
sunrise (Assume the sun rises on the side of the array starting point).
Note: The height of the building should be strictly greater than the height of the buildings left in order to see the
sun.
'''
class Solution:
    def countBuildings(self, height):
        max_height=height[0]
        c=1
        for i in height:
            if i>max_height:
                max_height=i
                c+=1
        return c


height = [2, 3, 4, 5]
print(Solution().countBuildings(height))