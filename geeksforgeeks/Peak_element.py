#Given an 0-indexed array of integers arr[] of size n, find its peak element. An element is
# considered to be peak if it's value is greater than or equal to the values of its
# adjacent elements (if they exist). Note: The output will be 1 if the index returned by your
# function is correct; otherwise, it will be 0.
class solution:
    def peekelement(self,arr,n):
        if n==1 or arr[0]>=arr[1]:
            return 0
        if arr[n-1]>=arr[n-2]:
            return n-1
        for i in range(1,n-1):
            if arr[i-1]<=arr[i]>=arr[i+1]:
                return i
        return -1

n=3
arr=[1,2,3]
print(solution().peekelement(arr,n))