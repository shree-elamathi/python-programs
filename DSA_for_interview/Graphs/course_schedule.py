'''
There are a total of n tasks you have to pick, labelled from 0 to n-1. Some tasks may have prerequisite tasks,
for example to pick task 0 you have to first finish tasks 1, which is expressed as a pair: [0, 1]
Given the total number of n tasks and a list of prerequisite pairs of size m. Find a ordering of tasks you
should pick to finish all tasks.
Note: There may be multiple correct orders, you just need to return any one of them. If it is impossible to
finish all tasks, return an empty array. Driver code will print "No Ordering Possible", on returning an empty
array. Returning any correct order will give the output as 1, whereas any invalid order will give the output 0.


'''


class Solution:
    def findOrder(self, n, m, prerequisites):
        from collections import defaultdict
        adj = defaultdict(list)
        for course, pre in prerequisites:
            adj[pre].append(course)

        vis = [0] * n
        order = []
        cycle = False

        def dfs(node):
            nonlocal cycle
            if vis[node] == 1:
                cycle = True
                return
            if vis[node] == 2:
                return

            vis[node] = 1
            for neighbor in adj[node]:
                dfs(neighbor)
            vis[node] = 2
            order.append(node)

        for i in range(n):
            if (vis[i] == 0):
                dfs(i)

        return order[::-1] if not cycle else []


n = 2
m = 1
prerequisites = [[1, 0]]
print(Solution().findOrder(n,m,prerequisites))
