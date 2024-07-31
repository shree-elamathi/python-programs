'''
Given an array of strings arr. Return the longest common prefix among all strings present in the array. If there's
no prefix common in all the strings, return "-1".
'''
class Solution:
    def longestCommonPrefix(self,arr):
        if len(arr) == 1:
            return arr[0]
        arr.sort(key=len)
        pre = ""
        for i in arr[0]:
            pre += i
            for j in range(1, len(arr)):
                x = arr[j]
                if pre != x[:len(pre)]:
                    if len(pre) > 1:
                        return pre[:-1]
                    else:
                        return -1

arr= ["geeksforgeeks", "geeks", "geek", "geezer"]
print(Solution().longestCommonPrefix(arr))