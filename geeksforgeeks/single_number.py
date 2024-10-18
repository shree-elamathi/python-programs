'''
Given an array arr[] of positive integers where every element appears even times except for one. Find that number
occurring an odd number of times.
'''
class Solution:
    def getSingle(self,arr):
        count = {}
        for num in arr:
            count[num] = count.get(num, 0) + 1
        for num, freq in count.items():
            if freq % 2 != 0:
                return num


arr = [1, 1, 2, 2, 2]
print(Solution().getSingle(arr))