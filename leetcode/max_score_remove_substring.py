'''
You are given a string s and two integers x and y. You can perform two types of operations any number of times.
Remove substring "ab" and gain x points.
For example, when removing "ab" from "cabxbae" it becomes "cxbae".
Remove substring "ba" and gain y points.
For example, when removing "ba" from "cabxbae" it becomes "cabxe".
Return the maximum points you can gain after applying the above operations on s.
'''
class Solution:
    def maximumGain(self,s,x,y):
        score=0
        stack=[]
        if x>y:
            for char in s:
                if stack and stack[-1]=="a" and char=="b":
                    stack.pop()
                    score+=x
                else:
                    stack.append(char)
            s=''.join(stack)
            stack=[]
            for char in s:
                if stack and stack[-1]=="b" and char=="a":
                    stack.pop()
                    score+=y
                else:
                    stack.append(char)
        else:
            for char in s:
                if stack and stack[-1]=="b" and char=="a":
                    stack.pop()
                    score+=y
                else:
                    stack.append(char)
            s=''.join(stack)
            stack=[]
            for char in s:
                if stack and stack[-1]=="a" and char=="b":
                    stack.pop()
                    score+=x
                else:
                    stack.append(char)
        return score

s="aabbaaxybbaabb"
x=5
y=4
print(Solution().maximumGain(s,x,y))