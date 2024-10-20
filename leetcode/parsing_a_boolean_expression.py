'''
A boolean expression is an expression that evaluates to either true or false. It can be in one of the
following shapes:
't' that evaluates to true.
'f' that evaluates to false.
'!(subExpr)' that evaluates to the logical NOT of the inner expression subExpr.
'&(subExpr1, subExpr2, ..., subExprn)' that evaluates to the logical AND of the inner expressions subExpr1,
subExpr2, ..., subExprn where n >= 1.
'|(subExpr1, subExpr2, ..., subExprn)' that evaluates to the logical OR of the inner expressions subExpr1,
subExpr2, ..., subExprn where n >= 1.
Given a string expression that represents a boolean expression, return the evaluation of that expression.
It is guaranteed that the given expression is valid and follows the given rules.
'''
class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        def evaluate(operator, operands):
            if operator == '!':
                return not operands[0]
            elif operator == '&':
                return all(operands)
            elif operator == '|':
                return any(operands)
        stack = []
        for char in expression:
            if char == ',':
                continue
            elif char in 'tf':
                stack.append(True if char == 't' else False)
            elif char in '!&|':
                stack.append(char)
            elif char == '(':
                stack.append('(')
            elif char == ')':
                operands = []
                while stack and stack[-1] != '(':
                    operands.append(stack.pop())
                stack.pop()
                operator = stack.pop()
                stack.append(evaluate(operator, operands[::-1]))
        return stack[0]


expression = "&(|(f))"
print(Solution().parseBoolExpr(expression))