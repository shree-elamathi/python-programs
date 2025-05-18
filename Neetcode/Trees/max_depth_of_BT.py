'''
Given the root of a binary tree, return its depth.

The depth of a binary tree is defined as the number of nodes along the longest path from the root node down
to the farthest leaf node.
'''


class Solution:
    def maxDepth(self, root) :
        if root:
            l = self.maxDepth(root.left)
            r = self.maxDepth(root.right)

            return 1 + max(l, r)

        else:
            return 0