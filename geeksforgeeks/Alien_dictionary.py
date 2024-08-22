'''
Given a sorted dictionary of an alien language having N words and k starting alphabets of standard dictionary. Find the
order of characters in the alien language.
Note: Many orders may be possible for a particular test case, thus you may return any valid order and output will be 1
if the order of string returned by the function is correct else 0 denoting incorrect string returned.
'''
from collections import defaultdict, deque
class Solution:
    def findOrder(self,dict,n,k):
        # Step 1: Create a graph with K nodes (for K characters)
        graph = defaultdict(list)
        in_degree = {chr(i + ord('a')): 0 for i in range(k)}  # Initialize in-degrees to 0

        # Step 2: Build the graph by comparing adjacent words
        for i in range(n - 1):
            word1 = dict[i]
            word2 = dict[i + 1]
            min_len = min(len(word1), len(word2))

            # Find the first character that differs
            for j in range(min_len):
                if word1[j] != word2[j]:
                    graph[word1[j]].append(word2[j])
                    in_degree[word2[j]] += 1
                    break

        # Step 3: Perform a topological sort using Kahn's algorithm (BFS)
        # Initialize the queue with nodes of in-degree 0
        queue = deque([char for char in in_degree if in_degree[char] == 0])
        order = []

        while queue:
            current = queue.popleft()
            order.append(current)

            # Decrease the in-degree of the adjacent nodes
            for neighbor in graph[current]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        # If order contains all characters, return it; otherwise, there was a cycle
        if len(order) == k:
            return "".join(order)
        else:
            return ""

words = ["baa", "abcd", "abca", "cab", "cad"]
N = len(words)
K = 4
print(Solution().findOrder(words, N, K))
