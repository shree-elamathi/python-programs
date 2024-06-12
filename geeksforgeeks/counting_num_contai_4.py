'''
You are given a number n, Return the count of total numbers from 1 to n containing 4 as a digit.
'''
class Solution:
    def countnumwith4(self,n):
        count=0
        for i in range(1,n+1):
            if "4" in str(i):
                count+=1
        return count
n=14
print(Solution().countnumwith4(n))