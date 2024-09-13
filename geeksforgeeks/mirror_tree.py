'''
Given a Binary Tree, convert it into its mirror.
'''


class Node:
    def _init_(self, val):
        self.right = None
        self.data = val
        self.left = None


class Solution:
    def mirror(self, root):
        if root is None:
            return None
        left = Solution().mirror(root.left)
        right = Solution().mirror(root.right)
        root.left = right
        root.right = left
        return root
