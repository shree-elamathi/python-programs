St=[4,3,9,6]
a=[]
class Solution:
    def reverse(self,St):
        a=[]
        while len(St)!=0:
            a.append(St.pop())
        for i in a:
            print(i,end=" ")
    
ob=Solution()
ob.reverse(St)




