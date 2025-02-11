'''
Given a string str consisting of opening and closing parenthesis '(' and ')'. Find length of the longest valid
parenthesis substring.
A parenthesis string is valid if:
For every opening parenthesis, there is a closing parenthesis.
Opening parenthesis must be closed in the correct order.
'''
class Solution:
    def maxLength(self, str):
        stack=[]
        stack.append(-1)
        max_len=0
        for i,char in enumerate(str):
            if char=="(":
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    max_len = max(max_len, i - stack[-1])
        return max_len

str = "((()"
print(Solution().maxLength(str))