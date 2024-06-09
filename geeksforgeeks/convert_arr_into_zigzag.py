'''
Given an array arr of distinct elements of size n, the task is to rearrange the elements of the array in a
zig-zag fashion so that the converted array should be in the below form:
arr[0] < arr[1]  > arr[2] < arr[3] > arr[4] < . . . . arr[n-2] < arr[n-1] > arr[n].
Note: Modify the given arr[] only, If your transformation is correct, the output will be 1 else the
output will be 0.
'''
class Solution:
    def zigzag(self,n,arr):
        for i in range(n):
            for j in range(i+1,n):
                if i%2==0:
                    if arr[i]<arr[j]:
                        break
                    else:
                        val=arr[i]
                        arr[i]=arr[j]
                        arr[j]=val
                        print(arr)
                        break
                else:
                    if arr[i]>arr[j]:
                        break
                    else:
                        val = arr[i]
                        arr[i] = arr[j]
                        arr[j] = val
                        break
        return arr
n=5
arr=[4, 7, 3, 8, 2]
print(Solution().zigzag(n,arr))