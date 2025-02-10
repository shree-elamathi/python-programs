'''
Given an infix expression in the form of string s. Convert this infix expression to a postfix expression.
Infix expression: The expression of the form a op b. When an operator is in between every pair of operands.
Postfix expression: The expression of the form a b op. When an operator is followed for every pair of operands.
Note: The order of precedence is: ^ greater than * equals to / greater than + equals to -. Ignore the right
associativity of ^.
'''


class Solution:
    def prec(self, sym):
        if sym == "^":
            return 3
        elif sym == '*' or sym == '/':
            return 2
        elif sym == '+' or sym == '-':
            return 1
        else:
            return -1

    def InfixtoPostfix(self, s):
        st = []
        res = ""

        for i in range(len(s)):
            c = s[i]

            if (c >= 'a' and c <= 'z') or (c >= 'A' and c <= 'Z') or (c >= '0' and c <= '9'):
                res += c

            elif c == ')':
                while st[-1] != '(':
                    res += st.pop()
                st.pop()

            elif c == '(':
                st.append('(')

            else:
                while st and (self.prec(c) <= self.prec(st[-1])):
                    res += st.pop()
                st.append(c)

        while st:
            res += st.pop()

        return res

exp = "a+b*(c^d-e)^(f+g*h)-i"
print(Solution().InfixtoPostfix(exp))
