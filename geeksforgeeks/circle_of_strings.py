'''
Given an array arr of lowercase strings, determine if the strings can be chained together to form a circle.
A string X can be chained together with another string Y if the last character of X is the same as the first character
of Y. If every string of the array can be chained with exactly two strings of the array(one with the first character
and the second with the last character of the string), it will form a circle.
For example, for the array arr[] = {"for", "geek", "rig", "kaf"} the answer will be Yes as the given strings can be
chained as "for", "rig", "geek" and "kaf"
'''
from collections import defaultdict


class Solution:
    def isCircle(self, arr):
        graph = defaultdict(list)
        in_degree = defaultdict(int)
        out_degree = defaultdict(int)

        # Step 2: Build the graph based on first and last characters
        for word in arr:
            first, last = word[0], word[-1]
            graph[first].append(last)
            out_degree[first] += 1
            in_degree[last] += 1

        # Step 3: Check if in-degree matches out-degree for all characters
        for char in set(in_degree.keys()).union(out_degree.keys()):
            if in_degree[char] != out_degree[char]:
                return 0

        # Step 4: Check if all characters form a single strongly connected component
        def dfs(char, visited):
            visited.add(char)
            for neighbor in graph[char]:
                if neighbor not in visited:
                    dfs(neighbor, visited)

        # Find all unique characters in the graph
        all_chars = set(in_degree.keys()).union(out_degree.keys())
        visited = set()

        # Start DFS from any node with outgoing edges
        dfs(list(graph.keys())[0], visited)

        # If all characters have been visited, then it is strongly connected
        if len(visited) != len(all_chars):
            return 0

        return 1

sol = Solution()
arr = ["for", "geek", "rig", "kaf"]
print(sol.isCircle(arr))
