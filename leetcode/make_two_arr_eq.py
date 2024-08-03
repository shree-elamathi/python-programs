'''
You are given two integer arrays of equal length target and arr. In one step, you can select any non-empty
subarray of arr and reverse it. You are allowed to make any number of steps.
Return true if you can make arr equal to target or false otherwise.
'''
class Solution:
    def canBeEqua(self,target,arr):
        arr.sort()
        target.sort()
        if target==arr:
            return True
        return False

target = [1,2,3,4]
arr = [2,4,1,3]
print(Solution().canBeEqua(target,arr))