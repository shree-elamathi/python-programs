'''
Given a string str of length N, consisting of ‘(‘ and ‘)‘ only, the task is to check whether it is balanced or not.
'''

class Solution:
    def isBalanced(self, exp):
        count = 0
        flag = True
        for i in exp:
            if count < 0:
                flag = False
                break
            if i == "(":
                count += 1
            else:
                count -= 1
        if flag == False:
            return False
        return True


exp = "())((())"
print(Solution().isBalanced(exp))