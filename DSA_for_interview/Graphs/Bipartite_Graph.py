'''
Given an adjacency list of a graph adj. Check whether the graph is bipartite or not.

A bipartite graph can be colored with two colors such that no two adjacent vertices share the same color. This means
we can divide the graph’s vertices into two distinct sets where:

All edges connect vertices from one set to vertices in the other set.
No edges exist between vertices within the same set.
'''


# any odd length cycle in a graph cannot be a bipartite graph
# even length cycle in a graph is a bipartite graph
# any linear graph is a bipartite graph
class Solution:
    def dfs(self,node, col, color, adj):
        color[node] = col
        for neighbor in adj[node]:
            if (color[neighbor] == -1):
                if (dfs(neighbor,not col, color, adj) == False):
                    return False
            elif (color[neighbor] == col):
                return False
        return True

    def isBipartite(self, adj):
        color = [-1] * len(adj)
        for i in range(len(adj)):
            if (color[i] == -1):
                if (self.dfs(i, 0, color,adj)) == False :
                    return False
        return True

