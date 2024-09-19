'''
Given a string expression of numbers and operators, return all possible results from computing all the different
possible ways to group numbers and operators. You may return the answer in any order.
The test cases are generated such that the output values fit in a 32-bit integer and the number of different results
does not exceed 104.
'''


class Solution:
    def diffWaysToCompute(self, expression: str)
        memo = {}
        def helper(expr):
            if expr in memo:
                return memo[expr]
            if expr.isdigit():
                return [int(expr)]

            res = []
            for i in range(len(expr)):
                if expr[i] in "+-*":
                    left_results = helper(expr[:i])
                    right_results = helper(expr[i + 1:])
                    for left in left_results:
                        for right in right_results:
                            if expr[i] == '+':
                                res.append(left + right)
                            elif expr[i] == '-':
                                res.append(left - right)
                            elif expr[i] == '*':
                                res.append(left * right)
            memo[expr] = res
            return res
        return helper(expression)


sol = Solution()
expression = "2*3-4*5"
print(sol.diffWaysToCompute(expression))
