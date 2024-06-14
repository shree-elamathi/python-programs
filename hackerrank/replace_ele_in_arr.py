'''
Replace each even number in an array with two of the same number.
'''
class Solution:
    def replaceele(self,arr):
        i=0
        while i<len(arr):
            if arr[i]%2==0:
                arr.insert(i+1,arr[i])
                i+=2
            else:
                i+=1
        return arr

arr=[1,2,5,6,8]
print(Solution().replaceele(arr))