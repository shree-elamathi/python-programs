'''
Given an unsorted array arr containing both positive and negative numbers. Your task is to create an array of
alternate positive and negative numbers without changing the relative order of positive and negative numbers.
Note: Array should start with a positive number and 0 (zero) should be considered a positive element.
'''
class Solution:
    def rearrange(self,arr):
        neg=[]
        pos=[]
        x=len(arr)
        for i in arr:
            if i<0:
                neg.append(i)
            else:
                pos.append(i)
        arr.clear()
        i=0
        while i<x:
            if len(neg)==0:
                arr.extend(pos)
                return arr
            elif len(pos)==0:
                arr.extend(neg)
                return arr
            elif i%2!=0:
                arr.append(neg.pop(0))
                i+=1
            elif i%2==0:
                arr.append(pos.pop(0))
                i+=1
        return arr

arr =  [9, 4, -2, -1, 5, 0, -5, -3, 2]
print(Solution().rearrange(arr))