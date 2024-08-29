'''
On a 2D plane, we place n stones at some integer coordinate points. Each coordinate point may have at most one stone.
A stone can be removed if it shares either the same row or the same column as another stone that has not been removed.
Given an array stones of length n where stones[i] = [xi, yi] represents the location of the ith stone, return the
largest possible number of stones that can be removed.
'''
class Solution:
    def removestones(self,stones):
        parent = {}

        def find(x):
            if parent.setdefault(x, x) != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            parent[find(x)] = find(y)

        for x, y in stones:
            union(x, ~y)  # union by row and column

        return len(stones) - len({find(x) for x in parent})

stones = [[0, 0], [0, 2], [1, 1], [2, 0], [2, 2]]
print(Solution().removestones(stones))