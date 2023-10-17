A = [7, 3, 2, 4, 9, 12, 56]
N = 7
M = 3
class Solution:
    def findMinDiff(self, A,N,M):
        A.sort()
        a=[]
        if M==0:
            return 0
        i=0
        j=M-1
        while N>i>=0 and N>j>=M-1:
            diff=A[j]-A[i]
            i+=1
            j+=1
            a.append(diff)
        a.sort()
        print(a[0])
                

ob=Solution()
ob.findMinDiff(A,N,M)
        
