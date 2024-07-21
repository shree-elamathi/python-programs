'''
Given an array arr. The task is to find and return the maximum product possible with the subset of elements present
in the array.
'''
class Solution:
    def findMaxProduct(self, arr):
        m = 1000000007
        if len(arr)==1:
            return arr[0]
        arr.sort()
        negative=[x for x in arr if x<0]
        positive=[x for x in arr if x>0]
        if len(negative)==0 and len(positive)==0:
            return 0
        if len(positive)==0 and len(negative)==1 and 0 in arr:
            return 0
        pro=1
        if len(negative)%2!=0:
            negative.pop()
        all_num=negative+positive
        if not all_num:
            return 0
        for num in all_num:
            pro=(pro*num) % m
        return pro%m

arr=[-1]
print(Solution().findMaxProduct(arr))