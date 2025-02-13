'''
Given an array arr containing the lengths of the different ropes, we need to connect these ropes to form one rope.
The cost to connect two ropes is equal to sum of their lengths. The task is to connect the ropes with minimum cost.
'''
import heapq


class solution:
    def minCost(self, arr):
        heapq.heapify(arr)
        cost = 0
        while len(arr) > 0:
            small = heapq.heappop(arr)
            sec_small = heapq.heappop(arr)
            val = small + sec_small
            cost += val
            heapq.heappush(arr, val)
        return cost
