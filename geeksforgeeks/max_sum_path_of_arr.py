'''
Given two sorted arrays of distinct integers arr1 and arr2. Each array may have some elements in common with the other
array. Find the maximum sum of a path from the beginning of any array to the end of any array. You can switch from one
array to another array only at the common elements.
Note:  When we switch from one array to other,  we need to consider the common element only once in the result.
'''
class Solution:
    def maxPathSum(self, arr1, arr2):
        i,j=0,0
        sum1,sum2=0,0
        result=0
        while i<len(arr1) and j<len(arr2):
            if arr1[i]<arr2[j]:
                sum1+=arr1[i]
                i+=1
            elif arr1[i]>arr2[j]:
                sum2+=arr2[j]
                j+=1
            else:
                result+=max(sum1,sum2)+arr1[i]
                sum1,sum2=0,0
                i+=1
                j+=1

        while i<len(arr1):
            sum1+=arr1[i]
            i+=1

        while j<len(arr2):
            sum2+=arr2[j]
            j+=1

        result+=max(sum1,sum2)
        return result

arr1 = [2, 3, 7, 10, 12]
arr2 = [1, 5, 7, 8]
print(Solution().maxPathSum(arr1,arr2))