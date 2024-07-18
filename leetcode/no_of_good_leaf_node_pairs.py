'''
You are given the root of a binary tree and an integer distance. A pair of two different leaf nodes of a binary tree
is said to be good if the length of the shortest path between them is less than or equal to distance.
Return the number of good leaf node pairs in the tree.
'''
class Solution:
    def countPairs(self,root,distance):
        def dfs(node):
            if not node:
                return []
            if not node.left and not node.right:
                return [(0, node)]
            left_leaves = dfs(node.left)
            right_leaves = dfs(node.right)
            for d1, l1 in left_leaves:
                for d2, l2 in right_leaves:
                    if d1 + d2 + 2 <= distance:
                        result[0] += 1
            return [(d + 1, l) for d, l in left_leaves + right_leaves]
        result = [0]
        dfs(root)
        return result[0]
