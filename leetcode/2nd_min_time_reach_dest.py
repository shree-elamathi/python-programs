'''
A city is represented as a bi-directional connected graph with n vertices where each vertex is labeled from 1 to n
(inclusive). The edges in the graph are represented as a 2D integer array edges, where each edges[i] = [ui, vi]
denotes a bi-directional edge between vertex ui and vertex vi. Every vertex pair is connected by at most one edge,
and no vertex has an edge to itself. The time taken to traverse any edge is time minutes.
Each vertex has a traffic signal which changes its color from green to red and vice versa every change minutes. All
signals change at the same time. You can enter a vertex at any time, but can leave a vertex only when the signal is
green. You cannot wait at a vertex if the signal is green.
The second minimum value is defined as the smallest value strictly larger than the minimum value.
For example the second minimum value of [2, 3, 4] is 3, and the second minimum value of [2, 2, 4] is 4.
Given n, edges, time, and change, return the second minimum time it will take to go from vertex 1 to vertex n.
Notes:
You can go through any vertex any number of times, including 1 and n.
You can assume that when the journey starts, all signals have just turned green.
'''
from collections import deque, defaultdict
import heapq

class Solution:
    def secondMinimum(self,n, edges, time, change):
        # Build the graph using adjacency list
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # Distance array to keep the shortest and second shortest time
        dist = [[float('inf')] * 2 for _ in range(n + 1)]
        dist[1][0] = 0

        # Queue for BFS: (current_time, vertex)
        queue = deque([(0, 1)])

        while queue:
            current_time, node = queue.popleft()

            # Determine the signal wait time if any
            cycles = current_time // change
            if cycles % 2 == 1:  # If we're in the red light period
                wait_time = (cycles + 1) * change - current_time
            else:
                wait_time = 0

            new_time = current_time + wait_time + time

            for neighbor in graph[node]:
                if new_time < dist[neighbor][0]:
                    dist[neighbor][1] = dist[neighbor][0]
                    dist[neighbor][0] = new_time
                    queue.append((new_time, neighbor))
                elif dist[neighbor][0] < new_time < dist[neighbor][1]:
                    dist[neighbor][1] = new_time
                    queue.append((new_time, neighbor))

        return dist[n][1] if dist[n][1] != float('inf') else -1 # If no second minimum path exists

n = 5
edges = [[1, 2], [1, 3], [1, 4], [3, 4], [4, 5]]
time = 3
change = 5
print(Solution().secondMinimum(n, edges, time, change))