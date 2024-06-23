'''
Given a string str, the task is to find the bracket numbers, i.e., for each bracket in str, return i if the
bracket is the ith opening or closing bracket to appear in the string.
'''
class Solution:
    def bracketNumbers(self, str):
        arr=[]
        open=1
        stack=[]
        for i in str:
            if i=="(":
                arr.append(open)
                stack.append(open)
                open+=1
            elif i==")":
                arr.append(stack.pop())
        return arr

str="((iy)rc(uv()(z((e())))u)()(()(())(e)((qb)(v((i))((pv))bw(uu)bg)))m()(l)(()(k)q)()(((n(n)))j)("
print(Solution().bracketNumbers(str))