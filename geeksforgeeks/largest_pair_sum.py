'''
Find the largest pair sum in an array of distinct integers.
'''
class Solution:
    def pairsum(self, arr):
        arr.sort()
        x=arr[-1]+arr[-2]
        return x


arr = [12, 34, 10, 6, 40]
print(Solution().pairsum(arr))