'''
Given the root of a binary search tree, return a balanced binary search tree with the same node values. If
there is more than one answer, return any of them.
A binary search tree is balanced if the depth of the two subtrees of every node never differs by more than 1.
'''
class Node:
    def __init__(self,key):
        self.val=key
        self.left=None
        self.right=None
class Solution:
    def balanceBST(self,root):
        def inorder(node):
            return inorder(node.left)+[node.val]+inorder(node.right) if node else []
        def sortedArrtoBST(arr):
            if not arr:
                return None
            mid=len(arr)//2
            node=Node(arr[mid])
            node.left=sortedArrtoBST(arr[:mid])
            node.right=sortedArrtoBST(arr[mid+1:])
            return node
        return sortedArrtoBST(inorder(root))

