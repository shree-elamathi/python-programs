'''
You are given a positive integer k. You are also given:
a 2D integer array rowConditions of size n where rowConditions[i] = [abovei, belowi], and
a 2D integer array colConditions of size m where colConditions[i] = [lefti, righti].
The two arrays contain integers from 1 to k.
You have to build a k x k matrix that contains each of the numbers from 1 to k exactly once. The remaining cells
should have the value 0.
The matrix should also satisfy the following conditions:
The number abovei should appear in a row that is strictly above the row at which the number belowi appears for all i
from 0 to n - 1.
The number lefti should appear in a column that is strictly left of the column at which the number righti appears for
all i from 0 to m - 1.
Return any matrix that satisfies the conditions. If no answer exists, return an empty matrix.
'''
def buildMatrix(k, rowConditions, colConditions):
    from collections import defaultdict, deque

    def topological_sort(edges, k):
        indegree = [0] * (k + 1)
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            indegree[v] += 1
        queue = deque([i for i in range(1, k + 1) if indegree[i] == 0])
        order = []
        while queue:
            node = queue.popleft()
            order.append(node)
            for neighbor in graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        return order if len(order) == k else []

    row_order = topological_sort(rowConditions, k)
    col_order = topological_sort(colConditions, k)

    if not row_order or not col_order:
        return []

    row_pos = {num: i for i, num in enumerate(row_order)}
    col_pos = {num: i for i, num in enumerate(col_order)}

    matrix = [[0] * k for _ in range(k)]
    for num in range(1, k + 1):
        r = row_pos[num]
        c = col_pos[num]
        matrix[r][c] = num

    return matrix

k = 3
rowConditions = [[1, 2], [2, 3]]
colConditions = [[1, 2], [2, 3]]
print(buildMatrix(k, rowConditions, colConditions))
