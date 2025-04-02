'''BFS traversal of a graph'''

class Solution:
    # Function to return Breadth First Search Traversal of given graph.
    def bfs(self, adj):
        vis = [0]*len(adj)
        queue = [0]
        ans = []
        while len(queue)!=0:
            x = queue.pop(0)
            ans.append(x)
            for i in adj[x]:
                if vis[i] == 0:
                    vis[i] = 1
                    queue.append(i)
        return ans

adj = [[1, 2], [0, 2], [0, 1, 3, 4], [2], [2]]
print(Solution().bfs(adj))