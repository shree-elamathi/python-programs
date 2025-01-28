'''
Given an array arr[] of n elements that contains elements from 0 to n-1, with any of these numbers appearing
any number of times. The task is to find the repeating numbers.
Note: The repeating element should be printed only once.
'''

class Solution:
    def findDuplicates(self,arr):
        freqMap = {}
        res = []
        for num in arr:
            freqMap[num] = freqMap.get(num,0) + 1

        for key , value in freqMap.items():
            if value>1:
                res.append(key)

        if not res:
            res.append(-1)

        for num in res:
            print(num , end = " ")

arr = [1, 2, 3, 6, 3, 6, 1]
Solution().findDuplicates(arr)