'''
Given a binary tree root and a linked list with head as the first node.
Return True if all the elements in the linked list starting from the head correspond to some downward path connected
in the binary tree otherwise return False.
In this context downward path means a path that starts at some node and goes downwards.
'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSubPath(self,root,head):
        if not root:
            return False
            # Check if the linked list matches starting from the current root node
        if self.dfs(root, head):
            return True
            # Recur for left and right subtree
        return self.isSubPath(head, root.left) or self.isSubPath(head, root.right)

    def dfs(self, node, head):
        # If the linked list is fully traversed, return True
        if not head:
            return True
        # If the tree node is null or values don't match, return False
        if not node or node.val != head.val:
            return False
        # Recur for both left and right children
        return self.dfs(node.left, head.next) or self.dfs(node.right, head.next)
