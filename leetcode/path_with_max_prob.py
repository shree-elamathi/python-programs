'''
You are given an undirected weighted graph of n nodes (0-indexed), represented by an edge list where edges[i] = [a, b]
is an undirected edge connecting the nodes a and b with a probability of success of traversing that edge succProb[i].
Given two nodes start and end, find the path with the maximum probability of success to go from start to end and
return its success probability.
If there is no path from start to end, return 0. Your answer will be accepted if it differs from the correct answer
by at most 1e-5.
'''
from typing import List
import heapq
from collections import defaultdict


class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int,
                       end_node: int) -> float:
        # Build the graph as an adjacency list
        graph = defaultdict(list)
        for i in range(len(edges)):
            a, b = edges[i]
            prob = succProb[i]
            graph[a].append((b, prob))
            graph[b].append((a, prob))

        # Max-Heap/Priority Queue to store the maximum probability so far
        max_heap = [(-1.0, start_node)]  # Start with the start node and probability 1 (negative for max-heap)
        # Probabilities array to store the best probability to reach each node
        probs = [0.0] * n
        probs[start_node] = 1.0

        while max_heap:
            curr_prob, node = heapq.heappop(max_heap)
            curr_prob = -curr_prob  # Convert back to positive

            # If we reached the end node, return the probability
            if node == end_node:
                return curr_prob

            # Explore neighbors
            for neighbor, edge_prob in graph[node]:
                new_prob = curr_prob * edge_prob
                if new_prob > probs[neighbor]:
                    probs[neighbor] = new_prob
                    heapq.heappush(max_heap, (-new_prob, neighbor))

        # If there's no path from start_node to end_node
        return 0.0


# Example usage:
solution = Solution()
n = 3
edges = [[0, 1], [1, 2], [0, 2]]
succProb = [0.5, 0.5, 0.2]
start_node = 0
end_node = 2
print(solution.maxProbability(n, edges, succProb, start_node, end_node))  # Expected output: 0.25
