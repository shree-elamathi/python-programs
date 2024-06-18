'''
You have n jobs and m workers. You are given three arrays: difficulty, profit, and worker where:
difficulty[i] and profit[i] are the difficulty and the profit of the ith job, and
worker[j] is the ability of jth worker (i.e., the jth worker can only complete a job with difficulty at most
worker[j]).
Every worker can be assigned at most one job, but one job can be completed multiple times.
For example, if three workers attempt the same job that pays $1, then the total profit will be $3. If a worker
cannot complete any job, their profit is $0.
Return the maximum profit we can achieve after assigning the workers to the jobs.
'''
class Solution:
    def maxProfitAssignment(self,difficulty,profit,worker):
        Tot_profit=0
        for i in worker: #To traverse through worker
            pro = 0  # Temporary profit
            for j in range(len(difficulty)): #To traverse through difficulty and profit
                if i>=difficulty[j]: #
                    pro=max(pro,profit[j])
            Tot_profit+=pro
        return Tot_profit
difficulty=[2,4,6,8,10]
profit=[10,20,30,40,50]
worker = [4,5,6,7]
print(Solution().maxProfitAssignment(difficulty,profit,worker))