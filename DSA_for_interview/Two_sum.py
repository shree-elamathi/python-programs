'''
Given an array arr[] of positive integers and another integer target. Determine if there exists two distinct
indices such that the sum of there elements is equals to target.
'''
class Solution:
    def twoSum(self, arr, target):
        res = set()
        for num in arr:
            ans = target - num
            if ans in res:
                return True
            res.add(num)
        return False

arr = [1, 4, 45, 6, 10, 8]
target = 16
print(Solution().twoSum(arr, target))