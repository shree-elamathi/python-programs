'''
Given n integer ranges, the task is to return the maximum occurring integer in the given ranges.
If more than one such integer exists, return the smallest one.The ranges are in two arrays l[] and r[].
l[i] consists of the starting point of the range and r[i] consists of the corresponding endpoint of the
range & a maxx which is the maximum value of r[].
For example, consider the following ranges.
l[] = {2, 1, 3}, r[] = {5, 3, 9)
Ranges represented by the above arrays are.
[2, 5] = {2, 3, 4, 5}
[1, 3] = {1, 2, 3}
[3, 9] = {3, 4, 5, 6, 7, 8, 9}
The maximum occurred integer in these ranges is 3.
'''
class Solution:
    def max_occ_int(self,n,l,r,maxx):
        val=[]
        al_counted_val=[]
        count=[]
        for i in range(n):
            for j in range(l[i],r[i]+1):
                val.append(j)
        val=sorted(val)
        for k in val:
            if k not in al_counted_val:
                count.append(val.count(k))
                al_counted_val.append(k)
        ma_val=max(count)
        ind=count.index(ma_val)
        return al_counted_val[ind]



n=4
l= [1,4,3,1]
r= [15,8,5,4]
maxx = 15
print(Solution().max_occ_int(n,l,r,maxx))