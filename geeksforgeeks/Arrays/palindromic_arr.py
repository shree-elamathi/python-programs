'''
Given a Integer array A[] of n elements. Your task is to complete the function PalinArray. Which will return 1
if all the elements of the Array are palindrome otherwise it will return 0.
'''
class Solution:
    def PalinArr(self,arr,n):
        for ele in arr:
            word=str(ele)
            rev=word[::-1]
            if str(ele)!=rev:
                return 0
        return 1
n=5
arr=[111,222,333,444,555]
print(Solution().PalinArr(arr,n))