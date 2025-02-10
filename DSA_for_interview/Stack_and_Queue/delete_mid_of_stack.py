'''
Given a stack s, delete the middle element of the stack without using any additional data structure.

Middle element:- floor((size_of_stack+1)/2) (1-based indexing) from the bottom of the stack.

Note: The output shown by the compiler is the stack from top to bottom.
'''
import math


class Solution:
    def deleteMid(self, stack):
        v = []
        n = len(stack)
        target = math.floor(n/2)
        for i in range(n):
            if i == target:
                continue
            v.append(stack[i])
        return v

stack = [10, 20, 30, 40, 50]
print(Solution().deleteMid(stack))