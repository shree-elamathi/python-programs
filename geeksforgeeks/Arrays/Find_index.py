'''
Given an unsorted array arr[] of n integers and a key which is present in this array. You need to write a
program to find the start index( index where the element is first found from left in the array ) and end
index( index where the element is first found from right in the array ).(0 based indexing is used)
If the key does not exist in the array then return -1 for both start and end index in this case.
'''
class Solution:
    def findindex(self,arr,n,key):
        res=[]
        for i in range(n):
            if arr[i]==key:
                res.append(i)
                break
        for j in range(n-1,-1,-1):
            if arr[j]==key:
                res.append(j)
                break
        if len(res)==2:
            return res
        else:
            res.append(-1)
            res.append(-1)
            return res

arr=[1, 2, 3, 4, 5, 5]
n=6
key=5
print(Solution().findindex(arr,n,key))