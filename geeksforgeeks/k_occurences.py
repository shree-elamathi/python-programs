#Given an array arr of size N and an element k.
# The task is to find the count of elements in the array that appear more than n/k times.
class solution:
    def count(self,arr,n,k):
        val=int(n/k)
        arr.sort()
        values=[]
        a=0
        i=0
        j=0
        while i<len(arr) and j<len(arr):
            if arr[i]==arr[j]:
                a=a+1
                j=j+1
            else:
                if a>val:
                    values.append(a)
                a=0
                i=j
        if a>val:
            values.append(a)
        return len(values)

arr=[2,3,3,2]
n=4
k=3
print(solution().count(arr,n,k))