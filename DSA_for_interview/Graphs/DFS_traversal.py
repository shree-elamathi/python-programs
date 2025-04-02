'''DFS traversal of a graph'''


class Solution:

    # Function to return a list containing the DFS traversal of the graph.
    def dfs(self, adj):
        vis = [0] * len(adj)
        vis[0] = 1
        ans = []

        def df(node):
            vis[node] = 1
            ans.append(node)
            for neighbour in adj[node]:
                if vis[neighbour] != 1:
                    df(neighbour)

        df(0)
        return ans

adj = [[2, 3, 1], [0], [0, 4], [0], [2]]
print(Solution().dfs(adj))