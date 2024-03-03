#Given an array of integers and a positive integer , determine the number of (i,j) pairs where i<j
# and ar[i] + ar[j]  is divisible by k.
def divisibleSumPairs(n, k, ar):
    i=0
    j=1
    count=0
    for i in range(0,len(ar)):
        for j in range(i+1,n):
            s=ar[i]+ar[j]
            if s%k==0:
                count+=1
    return count
n=6
k=5
ar=[1,2,3,4,5,6]
print(divisibleSumPairs(n,k,ar))