'''
You are given a string s that consists of lower case English letters and brackets.
Reverse the strings in each pair of matching parentheses, starting from the innermost one.
Your result should not contain any brackets.
'''
class Solution:
    def reverseParentheses(self,s):
        stack = []
        for char in s:
            if char == ')':
                # If we encounter a closing parenthesis, start building the substring to reverse
                substring = []
                while stack and stack[-1] != '(':
                    substring.append(stack.pop())
                stack.pop()  # Remove the opening parenthesis
                stack.extend(substring)# Add the reversed substring back to the stack
            else:
                stack.append(char)

        return ''.join(stack)


s="(ed(et(oc))el)"
print(Solution().reverseParentheses(s))