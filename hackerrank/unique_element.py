#Given an array of integers, where all elements but one occur twice, find the unique element.
def unique(arr):
    arr.sort()
    n=len(arr)
    arr.append(0)
    i=0
    j=1
    while i<n and j<=n:
        if arr[i]==arr[j]:
            i+=2
            j+=2
        else:
            return (arr[i])
arr=[1,2,3,4,3,2,1]
print(unique(arr))