'''
Suppose LeetCode will start its IPO soon. In order to sell a good price of its shares to Venture Capital,
LeetCode would like to work on some projects to increase its capital before the IPO. Since it has limited
resources, it can only finish at most k distinct projects before the IPO. Help LeetCode design the best way
to maximize its total capital after finishing at most k distinct projects.
You are given n projects where the ith project has a pure profit profits[i] and a minimum capital of
capital[i] is needed to start it.
Initially, you have w capital. When you finish a project, you will obtain its pure profit and the profit
will be added to your total capital.
Pick a list of at most k distinct projects from given projects to maximize your final capital, and return
the final maximized capital.
The answer is guaranteed to fit in a 32-bit signed integer.
'''
class Solution:
    def findMaximizedCapital(self,k, w, profits, capital):
        projects = sorted(zip(profits, capital), key=lambda x: x[1])
        i, curr_cap = 0, w
        for _ in range(k):
            while i < len(projects) and projects[i][1] <= curr_cap:
                max_profit, max_cap = 0, 0
                max_idx = i
                for j in range(i, len(projects)):
                    if projects[j][1] <= curr_cap and projects[j][0] > max_profit:
                        max_profit, max_cap = projects[j]
                        max_idx = j
                if max_profit > 0:
                    curr_cap += max_profit
                    projects.pop(max_idx)
                else:
                    break
            else:
                break
        return curr_cap
k = 2
w = 0
profits = [1,2,3]
capital = [0,1,1]
print(Solution().findMaximizedCapital(k,w,profits,capital))