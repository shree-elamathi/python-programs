'''
Given the root of a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the
original BST is changed to the original key plus the sum of all keys greater than the original key in BST.
As a reminder, a binary search tree is a tree that satisfies these constraints:
The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
'''
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.val == key:
            return root
        elif root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root

class Solution:
    def bstToGst(self,root):
        def rit(node,total):
            if not node:
                return total
            if node:
                total=rit(node.right,total)
                total+=node.val
                node.val=total
                return rit(node.left,total)
        rit(root,0)
        return root
def inorder(root):
    if root:
        inorder(root.right)
        print(root.val)
        inorder(root.left)


if __name__=='__main__':
    root = Node(4)
    root = insert(root, 0)
    root = insert(root, 1)
    root = insert(root, 2)
    root = insert(root, 3)
    root = insert(root, 5)
    root = insert(root, 6)
    root = insert(root, 7)
    root = insert(root, 8)
ans=(Solution().bstToGst(root))
inorder(ans)