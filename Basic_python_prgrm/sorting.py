#Bubble sorting
def bubbleSort(arr,n):
    for i in range(n-1):
        print(i,"i")
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr

def selectionSort(arr,n):
    for i in range(n-1):
        min_index=i
        for j in range(i+1,n-1):
            if arr[j]<arr[min_index]:
                min_index=j
        arr[min_index],arr[i]=arr[i],arr[min_index]

a=[9,5,4,7,3,8,1,6]
n=len(a)
bubbleSort(a,n)
print(a)
