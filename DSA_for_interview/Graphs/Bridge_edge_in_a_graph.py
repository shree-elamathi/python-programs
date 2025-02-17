''''
Given a Graph of V vertices and E edges and another edge(c - d), the task is to find if the given edge is a Bridge.
i.e., removing the edge disconnects the graph.
'''


class Solution:
    def isBridge(self, V, adj, c, d):
        # Check if c and d are valid vertices
        if not (0 <= c < V) or not (0 <= d < V):
            return 0  # Invalid edge index, return 0

        def dfs(node, visited):
            visited[node] = 1
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    dfs(neighbor, visited)

        # Count components before removing edge
        visited = [0] * V
        components_before = 0
        for i in range(V):
            if not visited[i]:
                dfs(i, visited)
                components_before += 1

        # Remove edge (c, d) safely
        if d in adj[c]:
            adj[c].remove(d)
        if c in adj[d]:
            adj[d].remove(c)

        # Count components after removing edge
        visited = [0] * V
        components_after = 0
        for i in range(V):
            if not visited[i]:
                dfs(i, visited)
                components_after += 1

        # If number of components increases, it's a bridge
        return 1 if components_after > components_before else 0


V = 2
adj = [[1], [0]]
c = 0
d = 1
print(Solution().isBridge(V, adj, c, d))
