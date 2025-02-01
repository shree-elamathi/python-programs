'''
Given an array arr[] of non-negative integers, where each element arr[i] represents the height of the
vertical lines, find the maximum amount of water that can be contained between any two lines, together
with the x-axis.

Note: In the case of a single vertical line it will not be able to hold water.
'''

#arr[] = [1, 5, 4, 3]

class Solution:
    def maxWater(self, arr):
        # naive approach
        max_amt = 0
        if len(arr)<2:
            return max_amt
        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                length = min(arr[i],arr[j])
                breadth = j - i
                max_amt = max(max_amt, length*breadth)
        return max_amt

    def maxWater2(self,arr):
        # advanced approach
        max_amt = 0
        left,right=0,len(arr)-1
        if len(arr) < 2:
            return max_amt
        while left < right:
            length = min(arr[left], arr[right])
            breadth = right - left
            max_amt = max(max_amt, length * breadth)
            if arr[right]<arr[left]:
                right -= 1
            else:
                left += 1
        return max_amt


arr = [3, 1, 2, 4, 5]
print(Solution().maxWater2(arr))