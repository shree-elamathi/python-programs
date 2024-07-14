'''
Given an array arr consisting of only 0's and 1's in random order. Modify the array in-place to segregate 0s onto
the left side and 1s onto the right side of the array.
'''
class Solution:
    def segregate0and1(self, arr):
        if 0 or 1 not in arr:
            return arr
        for i in arr:
            if i==1:
                arr.remove(i)
                arr.append(i)
        return arr
#To avoid complexity just sort the array and return

arr=[0, 0, 1, 1, 0]
print(Solution().segregate0and1(arr))