'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is
valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
'''

class Solution:
    def isValid(self, s):
        st = []
        for i in s:
            if i =="[" or i == "(" or i == "{":
                st.append(i)
            else:
                if len(st) != 0:
                    if i == "]":
                        if st.pop() != "[":
                            return False
                    elif i == ")":
                        if st.pop() != "(":
                            return False
                    elif i == "}":
                        if st.pop() != "{":
                            return False
                else:
                    return False
        if len(st) == 0:
            return True
        else:
            return False

s = "([{}])"
print(Solution().isValid(s))