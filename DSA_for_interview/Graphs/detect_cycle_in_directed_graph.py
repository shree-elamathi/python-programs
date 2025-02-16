'''
Given a Directed Graph with V vertices (Numbered from 0 to V-1) and E edges, check whether it contains any
cycle or not.
The graph is represented as an adjacency list, where adj[i] contains a list of vertices that are directly
reachable from vertex i. Specifically, adj[i][j] represents an edge from vertex i to vertex j.
'''


class Solution:
    def dfs(self, node, adj, vis, pathvis):
        vis[node] = 1
        pathvis[node] = 1

        for num in adj[node]:
            if vis[num] != 1:
                if self.dfs(num, adj, vis, pathvis) == True:
                    return True
            elif (pathvis[num] == 1):
                return True

        pathvis[node] = 0
        return False

    def isCyclic(self, adj) :
        vis = [0] * len(adj)
        pathvis = [0] * len(adj)
        for node in range(len(vis)):
            if vis[node] != 1:
                if self.dfs(node, adj, vis, pathvis) == True:
                    return True
        return False