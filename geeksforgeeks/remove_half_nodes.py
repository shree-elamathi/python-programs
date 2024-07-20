'''
You are given a binary tree and you need to remove all the half nodes (which have only one child). Return the root
node of the modified tree after removing all the half-nodes.
Note: The output will be judged by the inorder traversal of the resultant tree, inside the driver code.
'''
class Solution:
    def RemoveHalfNodes(self,node):
        if node is None:
            return None
        node.left = Solution().RemoveHalfNodes(node.left)
        node.right = Solution().RemoveHalfNodes(node.right)
        if node.left is None and node.right is not None:
            return node.right
        if node.right is None and node.left is not None:
            return node.left
        return node
def inorder_traversal(node, result):
    if node:
        inorder_traversal(node.left, result)
        result.append(node.value)
        inorder_traversal(node.right, result)
