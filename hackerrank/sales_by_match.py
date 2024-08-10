'''
There is a large pile of socks that must be paired by color. Given an array of integers representing the color of each
sock, determine how many pairs of socks with matching colors there are.
'''
class Solution:
    def sockMerchant(self,n, ar):
        set_socks=set(ar)
        pairs=0
        for i in set_socks:
            c=ar.count(i)
            if c%2==0:
                pairs+=c//2
            else:
                c-=1
                pairs+=c//2
        return pairs
ar= [10, 20, 20, 10, 10, 30, 50, 10, 20]
n=9
print(Solution().sockMerchant(n,ar))