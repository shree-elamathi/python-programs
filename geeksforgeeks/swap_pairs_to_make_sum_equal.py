'''
Given two arrays of integers a[] and b[] of size n and m, the task is to check if a pair of values
(one value from each array) exists such that swapping the elements of the pair will make the sum of
two arrays equal.
'''
a=[1, 2, 3]
b=[10, 20, 30]
class Solution:
    def swap_pair(self,a,b):
        sum_a = sum(a)
        sum_b = sum(b)
        diff = sum_a - sum_b
        if diff % 2 != 0:
            return -1
        b = set(b)
        target = diff // 2
        for ele in a:
            if (ele - target) in b:
                return 1
        else:
            return -1


print(Solution().swap_pair(a,b))