'''
Given a Binary Tree, return Left view of it. Left view of a Binary Tree is set of nodes visible when tree is visited
from Left side. The task is to complete the function leftView(), which accepts root of the tree as argument. If no
left view is possible, return an empty tree.
'''
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def leftView(self, root: TreeNode):
        if not root:
            return []

        left_view = []
        queue = deque([(root, 0)])  # (node, level)
        max_level = -1

        while queue:
            node, level = queue.popleft()

            # If this is the first node we're encountering at this level
            if level > max_level:
                left_view.append(node.val)
                max_level = level

            # Add left and right children to the queue
            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))

        return left_view
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)
root.left.right.left = TreeNode(7)

solution = Solution()
result = solution.leftView(root)
print(result)