'''
Given an array arr[] with repeated elements, the task is to find the maximum distance between two occurrences of an
element.
Note: You may assume that every input array has repetitions.
'''
class Solution:
    def maxDistance(self, arr):
        first_occurrence = {}
        max_distance = 0
        for i in range(len(arr)):
            if arr[i] not in first_occurrence:
                first_occurrence[arr[i]] = i
            else:
                distance = i - first_occurrence[arr[i]]
                max_distance = max(max_distance, distance)
        return max_distance


arr = [1, 1, 2, 2, 2, 1]
print(Solution().maxDistance(arr))