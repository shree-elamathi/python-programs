'''
Given an expression string x. Examine whether the pairs and the orders of {,},(,),[,] are correct in exp.
For example, the function should return 'true' for exp = [()]{}{[()()]()} and 'false' for exp = [(]).

Note: The driver code prints "balanced" if function return true, otherwise it prints "not balanced".
'''
class Solution:
    def ispar(self, x):
        matching_brackets = {')': '(', '}': '{', ']': '['}
        stack = []

        for char in x:
            if char in matching_brackets.values():
                stack.append(char)
            elif char in matching_brackets.keys():
                if stack == [] or stack.pop() != matching_brackets[char]:
                    return False
        return stack == []


exp = "()[]"
solution = Solution()
if solution.ispar(exp):
    print("balanced")
else:
    print("not balanced")