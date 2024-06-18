'''
Geek prepared N questions for developers hiring challenge of the GeeksforGeeks, but the hiring manager wants
only one question in the contest and he asked geek to give the best problem out of N problems. Geek thinks
that all the questions are best and he confused to choose a single problem. So, geek came with a game. Geek
placed all the problems side by side from 1 to N. He takes out the first problem and inserts it at the end
and removes the next first problem from the set. He repeats the same process until a single problem remains.
The task is to find a single last problem.
Input:
1. The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows.
2. The first line of each test case contains a single integer N.
Output: For each test case, print the last problem which remains
'''
class Solution:
    def GeekProblem(self,N):
        lst=[]
        for i in range(1,N+1):
            lst.append(i)
        i=1
        while len(lst)>=1:
            if len(lst)==1:
                return lst[0]
            if i%2!=0:
                val=lst[i-1]
                lst.pop(i-1)
                lst.append(val)
                i-=1
            else:
                lst.pop(i)
                i+=1


#tc=int(input())
#for i in range(tc):
#    N=int(input())
#    print(Solution().GeekProblem(N))
N=4
print(Solution().GeekProblem(N))
