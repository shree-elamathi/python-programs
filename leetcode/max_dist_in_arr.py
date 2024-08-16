'''
You are given m arrays, where each array is sorted in ascending order.
You can pick up two integers from two different arrays (each array picks one) and calculate the distance. We define
the distance between two integers a and b to be their absolute difference |a - b|.
Return the maximum distance.
'''
class Solution:
    def maxDistance(self,arrays):
        min_arr = []
        max_arr = []
        max_dist = 0
        for arr in arrays:
            min_arr.append(min(arr))
            max_arr.append(max(arr))
        for i in range(len(min_arr)):
            for j in range(len(max_arr)):
                if j == i:
                    continue
                max_dist = max(max_dist, abs(min_arr[i] - max_arr[j]))
        return max_dist

arrays = [[1,2,3],[4,5],[1,2,3]]
print(Solution().maxDistance(arrays))