'''
Given an unsorted array Arr of length N. Your task is to find the maximum difference between the successive
elements in its sorted form.
Return 0 if the array contains less than 2 elements.
'''
class Solution:
    def maxSortedAdjacentDiff(self,arr, n):
        arr.sort()
        gap=0
        for i in range(n-1):
            temp_gap=abs(arr[i]-arr[i+1])
            gap=max(gap,temp_gap)
        return gap

arr=[1, 10, 5]
n=3
print(Solution().maxSortedAdjacentDiff(arr,n))