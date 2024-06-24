'''
You are given N ropes. A cut operation is performed on ropes such that all of them are reduced by the length
of the smallest rope. Display the number of ropes left after every cut operation until the length of each
rope is zero.
'''
class Solution:
    def RopeCutting(self,arr,n):
        arr.sort()
        res=[]
        while len(arr)>0:
            val=arr.pop(0)
            i=0
            while i<len(arr):
                if arr[i]-val==0:
                    arr.pop(i)
                else:
                    arr[i]=arr[i]-val
                    i+=1
            if len(arr)!=0:
                res.append(len(arr))
        return res


arr=[5, 1, 6, 9, 8, 11, 2, 2, 6, 5]
n=10
print(Solution().RopeCutting(arr,n))


