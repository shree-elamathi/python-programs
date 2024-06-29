'''
You are given a positive integer n representing the number of nodes of a Directed Acyclic Graph (DAG). The
nodes are numbered from 0 to n - 1 (inclusive).
You are also given a 2D integer array edges, where edges[i] = [fromi, toi] denotes that there is a
unidirectional edge from fromi to toi in the graph.
Return a list answer, where answer[i] is the list of ancestors of the ith node, sorted in ascending order.
A node u is an ancestor of another node v if u can reach v via a set of edges.
'''
from collections import defaultdict
class Solution:
    def getAncestors(self,n, edges):
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
        ancestors = [set() for _ in range(n)]
        def dfs(node, start):
            for neighbor in graph[node]:
                if start not in ancestors[neighbor]:
                    ancestors[neighbor].add(start)
                    dfs(neighbor, start)
        for i in range(n):
            dfs(i, i)
        result = [sorted(list(ancestor_set)) for ancestor_set in ancestors]
        return result

n=9
edges=[[8,3],[6,3],[1,6],[7,0],[8,5],[2,1],[4,0],[2,3],[0,3],[5,3],[7,4],[4,1]]
print(Solution().getAncestors(n,edges))