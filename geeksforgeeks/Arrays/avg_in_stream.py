'''
Given a stream of incoming numbers, find average or mean of the stream at every point.
'''
class Solution:
    def streamAvg(self,arr,n):
        res=[]
        sum=0
        for i in range(n):
            sum+=arr[i]
            res.append(sum/(i+1))
        return res

arr=[10, 20, 30, 40, 50]
n=5
print(Solution().streamAvg(arr,n))