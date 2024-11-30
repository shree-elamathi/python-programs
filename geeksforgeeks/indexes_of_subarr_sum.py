'''
Given an unsorted array arr containing only non-negative integers, your task is to find a continuous subarray
(a contiguous sequence of elements) whose sum equals a specified value target. You need to return the 1-based indices
of the leftmost and rightmost elements of this subarray.
'''


class Solution:
    def subArraySum(self, arr, target):
        n = len(arr)
        res = []
        for i in range(len(arr)):
            sum1 = arr[i]
            if arr[i] == target:
                res.append(i + 1)
                res.append(i + 1)
                return res
            for j in range(i + 1, len(arr)):
                sum1 += arr[j]
                if sum1 == target:
                    res.append(i + 1)
                    res.append(j + 1)
                    return res
                if sum1 > target:
                    break
        res.append(-1)
        return res


arr = [1,2,3,7,5]
target = 12
print(Solution().subArraySum(arr,target))
