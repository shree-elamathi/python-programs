'''
You are given an array of integers nums of length n and a positive integer k.
The power of an array is defined as:
Its maximum element if all of its elements are consecutive and sorted in ascending order.
-1 otherwise.
You need to find the power of all
subarrays
 of nums of size k.
Return an integer array results of size n - k + 1, where results[i] is the power of nums[i..(i + k - 1)].
'''


class Solution:
    def resultsArray(self, nums, k):
        res = []
        if k == 1:
            return nums
        for i in range(len(nums) - k + 1):
            temp_arr = nums[i:i + k]
            flag = False
            for j in range(k - 1):
                if not flag and j > 0:
                    break
                if temp_arr[j + 1] == temp_arr[j] + 1:
                    flag = True
                else:
                    flag = False
            if not flag:
                res.append(-1)
            else:
                res.append(max(temp_arr))
        return res


nums = [1,2,3,4,3,2,5]
k = 3
print(Solution().resultsArray(nums,k))