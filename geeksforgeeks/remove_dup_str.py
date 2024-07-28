'''
Given a string str without spaces, the task is to remove all duplicate characters from it, keeping only the first
occurrence.
Note: The original order of characters must be kept the same.
'''
class Solution:
    def removeDups(self, str):
        arr=[]
        for i in str:
            if i not in arr:
                arr.append(i)
        return (''.join(arr))

str="gfg"
print(Solution().removeDups(str))