#Given five positive integers, find the minimum and maximum values that can be calculated by
# summing exactly four of the five integers. Then print the respective minimum and maximum values
# as a single line of two space-separated long integers.
def minimaxsum(arr):
    val=[]
    val.append(arr[0]+arr[1]+arr[2]+arr[3])
    val.append(arr[0] + arr[1] + arr[2] + arr[4])
    val.append(arr[0] + arr[1] + arr[3] + arr[4])
    val.append(arr[0] + arr[2] + arr[3] + arr[4])
    val.append(arr[1] + arr[2] + arr[3] + arr[4])
    print(min(val),end=" ")
    print(max(val))
arr=[1,2,3,4,5]
minimaxsum(arr)
