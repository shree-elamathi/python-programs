'''
There are n students in a class numbered from 0 to n - 1. The teacher will give each student a problem starting with
the student number 0, then the student number 1, and so on until the teacher reaches the student number n - 1. After
that, the teacher will restart the process, starting with the student number 0 again.
You are given a 0-indexed integer array chalk and an integer k. There are initially k pieces of chalk. When the
student number i is given a problem to solve, they will use chalk[i] pieces of chalk to solve that problem. However,
if the current number of chalk pieces is strictly less than chalk[i], then the student number i will be asked to
replace the chalk.
Return the index of the student that will replace the chalk pieces.
'''
class Solution:
    def chalkReplacer(self,chalk,k):
        chalk_sum=sum(chalk)
        if k%chalk_sum==0:
            return 0
        else:
            k=k%chalk_sum
        for i in range(len(chalk)):
            if k<chalk[i]:
                return i
            elif k==0:
                return i+1
            else:
                k-=chalk[i]
        '''
        naive approach
        i=1
        while k>=chalk[i-1]:
            if i==len(chalk):
                i=0
            k-=chalk[i-1]
            i+=1
        return i-1
        '''


chalk=[1]
k=25
print(Solution().chalkReplacer(chalk,k))
