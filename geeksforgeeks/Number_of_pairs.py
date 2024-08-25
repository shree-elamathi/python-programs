'''
Given two positive integer arrays arr and brr, find the number of pairs such that xy > yx (raised to power of) where x
is an element from arr and y is an element from brr.
'''
class Solution:
    def countPairs(self, arr, brr):
        pairs=[]
        for x in arr:
            for y in brr:
                xy=[x**y,y**x]
                pairs.append(xy)
        res=0
        for pair in pairs:
            if pair[0]>pair[1]:
                res+=1
        return res
arr =  [2, 3, 4, 5]
brr= [1, 2, 3]
print(Solution().countPairs(arr,brr))
