'''
Given a two-dimensional integer array arr of dimensions n x n, consisting solely of zeros and ones, identify
the row or column (using 0-based indexing) where all elements form a palindrome. If multiple palindromes are
identified, prioritize the palindromes found in rows over those in columns. Within rows or columns, the
palindrome with the smaller index takes precedence. The result should be represented by the index followed by
either 'R' or 'C', indicating whether the palindrome was located in a row or column. The output should be
space-separated. If no palindrome is found, return the string -1.
'''
class Solution:
    def pattern(self,arr):
        #first iteration to check rows
        for each in arr:
            #sending each row as an array
            res=palindrome(each)
            if res:
                return (str(arr.index(each))+" R")
        #second iteration to check through columns
        for i in range(len(arr)):
            #convert column into arr and passing to palindrome()
            col=[]
            for j in range(len(arr[0])):
                col.append(arr[j][i])
            res= palindrome(col)
            if res:
                return (str(i)+" C")
        return "-1"

def palindrome(arr):
    i=0
    j=len(arr)-1
    while i<len(arr) and j>-1:
        if arr[i]!=arr[j]:
            return 0
        i+=1
        j-=1
    return 1

arr= [[1, 0], [1, 0]]
print(Solution().pattern(arr))