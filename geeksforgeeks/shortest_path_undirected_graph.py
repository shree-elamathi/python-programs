'''
You are given an Undirected Graph having unit weight of the edges, find the shortest path from src to all the vertex
and if it is unreachable to reach any vertex, then return -1 for that vertex.
'''
from collections import deque
class Solution:
    def shortestPath(self, edges, n, m, src):
        adj_list = [[] for _ in range(n)]
        for edge in edges:
            u, v = edge
            adj_list[u].append(v)
            adj_list[v].append(u)
        dist=[-1]*n
        dist[src]=0
        queue=deque([src])
        while queue:
            u=queue.popleft()
            for v in adj_list[u]:
                 if dist[v]==-1:
                     dist[v]=dist[u]+1
                     queue.append(v)
        return dist


n=9
m=10
edges=[[0,1],[0,3],[3,4],[4,5],[5,6],[1,2],[2,6],[6,7],[7,8],[6,8]]
src=0
print(Solution().shortestPath(edges, n, m, src))