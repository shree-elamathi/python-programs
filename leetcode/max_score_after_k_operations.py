'''
You are given a 0-indexed integer array nums and an integer k. You have a starting score of 0.
In one operation:
choose an index i such that 0 <= i < nums.length,
increase your score by nums[i], and
replace nums[i] with ceil(nums[i] / 3).
Return the maximum possible score you can attain after applying exactly k operations.
The ceiling function ceil(val) is the least integer greater than or equal to val.
'''
import heapq
import math
class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        max_heap = [-num for num in nums]
        heapq.heapify(max_heap)
        score = 0
        for _ in range(k):
            max_val = -heapq.heappop(max_heap)
            score += max_val
            new_val = math.ceil(max_val / 3)
            heapq.heappush(max_heap, -new_val)
        return score



nums = [1,10,3,3,3]
k = 3
print(Solution().maxKelements(nums,k))