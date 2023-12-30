#Given an array of N elements and L and R, print the number of sub-arrays such that the value of the maximum array
# element in that subarray is at least L and at most R.
class solution:
    def countsubarr(self,a,n,L,R):
        x=0
        i=0
        j=1
        while i<len(a):
            if a[i]>=L and a[i]<=R:
                x=x+1
                i=i+1
            else:
                i=i+1
        return x
a=[2, 0, 11, 3, 0]
n=5
L=1
R=10
print(solution().countsubarr(a,n,L,R))
