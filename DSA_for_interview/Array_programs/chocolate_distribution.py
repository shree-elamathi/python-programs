'''
Given an array arr[] of positive integers, where each value represents the number of chocolates in a packet.
Each packet can have a variable number of chocolates. There are m students, the task is to distribute
chocolate packets among m students such that -
      i. Each student gets exactly one packet.
     ii. The difference between maximum number of chocolates given to a student and minimum number of
     chocolates given to a student is minimum and return that minimum possible difference.
'''

class Solution:

    def findMinDiff(self, arr,M):
        arr.sort()
        min_val = arr[-1]
        left,right = 0, M-1
        while right < len (arr):
            min_val = min(min_val , arr[right]- arr[left])
            right+=1
            left+=1
        return min_val

arr = [3, 4, 1, 9, 56, 7, 9, 12]
m = 5
print(Solution().findMinDiff(arr,m))