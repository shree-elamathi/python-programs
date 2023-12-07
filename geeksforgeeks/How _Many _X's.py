#Given two integers L, R, and digit X. Find the number of occurrences of X in all
#the numbers in the range (L, R) excluding L and R.
class solution:
    def countX(self,L,R,X):
        list=[]
        for i in range(L+1,R):
            j=str(i)
            list.append(j)
        a=0
        x=str(X)
        for k in list:
            a+=k.count(x)
        return a

print(solution().countX(10,19,1))