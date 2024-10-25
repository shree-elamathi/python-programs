'''
Given an array arr of distinct integers. Rearrange the array in such a way that the first element is the largest and
the second element is the smallest, the third element is the second largest and the fourth element is the second
smallest, and so on.
'''
class Solution:
    def alternateSort(self,arr):
        arr.sort(reverse=True)
        n=len(arr)
        x=(n//2)
        arr1=arr[:x+1]
        arr2=arr[x+1:]
        arr2.sort()
        for i in range(1,len(arr),2):
            if len(arr2)>0:
                arr1.insert(i,arr2.pop(0))
            else:
                return arr1
        return arr1


arr = [7, 1, 2, 3, 4, 5, 6]
print(Solution().alternateSort(arr))