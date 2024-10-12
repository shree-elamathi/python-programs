'''
You are given a 2D integer array intervals where intervals[i] = [lefti, righti] represents the inclusive interval
[lefti, righti].You have to divide the intervals into one or more groups such that each interval is in exactly one
group, and no two intervals that are in the same group intersect each other.
Return the minimum number of groups you need to make.
Two intervals intersect if there is at least one common number between them. For example, the intervals [1, 5] and
[5, 8] intersect.
'''
import heapq
class Solution:
    def minGroups(self, intervals):
        intervals.sort()
        heap = []
        for interval in intervals:
            start, end = interval
            if heap and heap[0] < start:
                heapq.heappop(heap)
            heapq.heappush(heap, end)
        return len(heap)


intervals = [[5,10],[6,8],[1,5],[2,3],[1,10]]
print(Solution().minGroups(intervals))