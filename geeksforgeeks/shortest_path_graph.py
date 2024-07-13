'''
You are given a weighted undirected graph having n vertices numbered from 1 to n and m edges along with their
weights. Find the shortest path between the vertex 1 and the vertex n,  if there exists a path, and return a list
of integers whose first element is the weight of the path, and the rest consist of the nodes on that path. If no path
exists, then return a list containing a single element -1.
The input list of edges is as follows - {a, b, w}, denoting there is an edge between a and b, and w is the weight of
that edge.
Note: The driver code here will first check if the weight of the path returned is equal to the sum of the weights
along the nodes on that path, if equal it will output the weight of the path, else -2. In case the list contains
only a single element (-1) it will simply output -1.
'''
import heapq
def shortestPath(n,m,edges):
    graph = {i: [] for i in range(1, n + 1)}
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))

    # Dijkstra's algorithm
    min_heap = [(0, 1)]  # (weight, node)
    distances = {i: float('inf') for i in range(1, n + 1)}
    distances[1] = 0
    previous = {i: None for i in range(1, n + 1)}

    while min_heap:
        current_distance, current_node = heapq.heappop(min_heap)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_node
                heapq.heappush(min_heap, (distance, neighbor))

    # Reconstruct path
    if distances[n] == float('inf'):
        return [-1]

    path = []
    current = n
    while current is not None:
        path.append(current)
        current = previous[current]

    path = path[::-1]
    return [distances[n]] + path

edges=[[1, 2, 2], [2, 5, 5], [2, 3, 4], [1, 4, 1], [4, 3, 3], [3, 5, 1]]
n=5
m=6
print(shortestPath(n,m,edges))