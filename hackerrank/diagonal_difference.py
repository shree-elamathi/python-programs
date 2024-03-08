#Given a square matrix, calculate the absolute difference between the sums of its diagonals.
def diff(arr,n):
    i=0
    j=0
    sum1=0
    sum2=0
    while i<n and j<n:
        sum1+=arr[i][j]
        i+=1
        j+=1
    i=0
    j=n-1
    while i<n and j>-1:
        sum2+=arr[i][j]
        i+=1
        j-=1
    return abs(sum1-sum2)
arr=[[1,2,3],[4,5,6],[9,8,9]]
n=3
print(diff(arr,n))

