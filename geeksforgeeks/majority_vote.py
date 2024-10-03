'''
You are given an array of integer nums[] where each number represents a vote to a candidate. Return the candidates
that have votes greater than one-third of the total votes, If there's not a majority vote, return -1.
Note: The answer should be returned in an increasing format.
'''
class Solution:
    def findMajority(self, nums):
        num=set(nums)
        x=len(nums)/3
        res=[]
        for i in num:
            if nums.count(i)>x:
                res.append(i)
        if len(res)==0:
            res.append(-1)
        res.sort()
        return res


nums = [1, 2, 3, 4, 5]
print(Solution().findMajority(nums))