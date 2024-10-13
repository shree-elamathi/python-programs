'''
You have k lists of sorted integers in non-decreasing order. Find the smallest range that includes at least one
number from each of the k lists.
We define the range [a, b] is smaller than range [c, d] if b - a < d - c or a < c if b - a == d - c.
'''
import heapq


class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        min_heap = []
        current_max = float('-inf')

        # Step 1: Add the first element of each list to the heap
        for i in range(len(nums)):
            heapq.heappush(min_heap, (nums[i][0], i, 0))
            current_max = max(current_max, nums[i][0])

        # Step 2: Initialize the smallest range [min_range_start, min_range_end]
        min_range_start, min_range_end = float('-inf'), float('inf')

        # Step 3: Process the heap
        while min_heap:
            current_min, row, idx = heapq.heappop(min_heap)

            # If current range is smaller, update the result
            if current_max - current_min < min_range_end - min_range_start:
                min_range_start, min_range_end = current_min, current_max

            # If we have exhausted one list, we can break out
            if idx + 1 == len(nums[row]):
                break

            # Add the next element from the same list to the heap
            next_val = nums[row][idx + 1]
            heapq.heappush(min_heap, (next_val, row, idx + 1))
            current_max = max(current_max, next_val)

        return [min_range_start, min_range_end]