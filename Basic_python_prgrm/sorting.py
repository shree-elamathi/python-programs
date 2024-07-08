#Bubble sorting
def bubbleSort(arr,n):
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr

a=[9,5,4,7,3,8,1,6]
n=len(a)
bubbleSort(a,n)
print(a)
