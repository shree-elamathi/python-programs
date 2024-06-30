''''
Alice and Bob have an undirected graph of n nodes and three types of edges:
Type 1: Can be traversed by Alice only.
Type 2: Can be traversed by Bob only.
Type 3: Can be traversed by both Alice and Bob.
Given an array edges where edges[i] = [typei, ui, vi] represents a bidirectional edge of type typei between
nodes ui and vi, find the maximum number of edges you can remove so that after removing the edges, the graph
can still be fully traversed by both Alice and Bob. The graph is fully traversed by Alice and Bob if
starting from any node, they can reach all other nodes.
Return the maximum number of edges you can remove, or return -1 if Alice and Bob cannot fully traverse the
graph.
'''


class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [1] * size

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1
            return True
        return False


def maxNumEdgesToRemove(n, edges):
    alice_uf = UnionFind(n)
    bob_uf = UnionFind(n)
    removed_edges = 0
    edges.sort(reverse=True, key=lambda x: x[0])

    # First, add all type 3 edges
    for edge in edges:
        if edge[0] == 3:
            u, v = edge[1] - 1, edge[2] - 1
            alice_added = alice_uf.union(u, v)
            bob_added = bob_uf.union(u, v)
            if not alice_added and not bob_added:
                removed_edges += 1

    # Add type 1 and type 2 edges
    for edge in edges:
        u, v = edge[1] - 1, edge[2] - 1
        if edge[0] == 1:
            if not alice_uf.union(u, v):
                removed_edges += 1
        elif edge[0] == 2:
            if not bob_uf.union(u, v):
                removed_edges += 1

    # Check if both Alice and Bob can traverse the entire graph
    if len({alice_uf.find(i) for i in range(n)}) > 1 or len({bob_uf.find(i) for i in range(n)}) > 1:
        return -1

    return removed_edges


n = 4
edges = [[3, 1, 2], [3, 2, 3], [1, 1, 3], [1, 2, 4], [1, 1, 4], [2, 3, 4]]
print(maxNumEdgesToRemove(n, edges))
