'''
Given an array arr[] of n integers, construct a product array res[] (of the same size) such that res[i] is
equal to the product of all the elements of arr[] except arr[i].
'''

class Solution:
    def productExceptSelf(self, arr):
        prod = 1
        Flag = False
        zero = 0
        for num in arr:
            if num != 0:
                prod *= num
            else:
                Flag = True
                zero+=1
        if Flag and zero<=1:
            for i in range(len(arr)):
                if arr[i]==0:
                    arr[i] = prod
                else:
                    arr[i] = 0
        elif zero>1:
            for i in range(len(arr)):
                arr[i] = 0
            return arr
        else:
            for i in range(len(arr)):
                arr[i] = prod // arr[i]
        return arr

arr = [10, 3, 5, 6, 2]
print(Solution().productExceptSelf(arr))