#Given an array of integers Arr of size N and a number K. Return the maximum sum of a subarray
# of size K.
class solution:
    def maxsum(self,arr,k,n):
        sum=0
        sums=[]
        if n==k:
            for i in arr:
                sum=sum+i
            return sum
        else:
            i=0
            j=k-1
            while i<=len(arr)-k and j <=len(arr):
                ans=0
                for k in range(i,j+1):
                    ans=ans+arr[k]
                sums.append(ans)
                i=i+1
                j=j+1
        return max(sums)




arr=[100, 200, 300, 400]
print(solution().maxsum(arr,2,4))