#Given a sorted array containing only 0s and 1s, find the transition point, i.e.,
# the first index where 1 was observed, and before that, only 0 was observed.
class Solution:
    def transitionPoint( arr, n):
        a=0
        b=0
        c=0
        for i in arr:
            if i==0:
                a+=1
                continue
            else:
                b+=1
                if c==0:
                    c=arr.index(i)
                continue
        if a==n:
            return -1
        elif b==n:
            return 0
        else:
            return c

arr=[0,1,1,1]
n=4
print(Solution.transitionPoint(arr,n))