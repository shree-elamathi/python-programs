'''
Given a string, the task is to find the maximum consecutive repeating character in a string.
Note: We do not need to consider the overall count, but the count of repeating that appears in one place.
'''


class Solution:
    def maxRepeating(self,string):
        if len(string) == 1:
            return string[0]
        n = len(string)
        res = string[0]
        count = 0
        cur_count = 1
        for i in range(n):
            if (i<n-1 and string[i] == string[i+1]):
                cur_count += 1
            else:
                if cur_count > count:
                    count = cur_count
                    res= string[i]
                cur_count = 1
        return res


string = "geeekkkkk"
print(Solution().maxRepeating(string))




