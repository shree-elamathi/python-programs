'''
Given an array arr[] and a target, your task is to find all unique combinations in the array where the sum is equal
to target. The same number may be chosen from the array any number of times to make target.

You can return your answer in any order.
'''


class Solution:
    def combinationSum(self, arr, target):
        arr = sorted(set(arr))
        result = []

        def backtrack(start, target, path):
            if target == 0:
                result.append(list(path))
                return
            for i in range(start, len(arr)):
                if arr[i] > target:
                    break
                path.append(arr[i])
                backtrack(i, target - arr[i], path)
                path.pop()

        backtrack(0, target, [])
        return result


arr = [2, 4, 6, 8]
target = 8
print(Solution().combinationSum(arr,target))