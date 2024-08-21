'''
Given an array arr. Your task is to find the minimum and maximum elements in the array.
Note: Return an array that contains two elements the first one will be a minimum element and the second will be a
maximum of an array.
'''
class Solution:
    def get_min_max(self, arr):
        min_a=arr[0]
        max_a=arr[0]
        res=[]
        for i in arr:
            if i<min_a:
                min_a=i
            elif i>max_a:
                max_a=i
        res.append(min_a)
        res.append(max_a)
        return res
arr=[3, 2, 1, 56, 10000, 167]
print(Solution().get_min_max(arr))