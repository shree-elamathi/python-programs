'''
Given a Binary Tree (BT), convert it to a Doubly Linked List (DLL) in place. The left and right pointers in nodes
will be used as previous and next pointers respectively in converted DLL. The order of nodes in DLL must be the same
as the order of the given Binary Tree. The first node of Inorder traversal (leftmost node in BT) must be the head node
of the DLL.
Note: h is the tree's height, and this space is used implicitly for the recursion stack.
'''
class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None

class Solution:
    def __init__(self):
        self.head=None
        self.left=None
    def bToDLL(self,root):
        self.inorder(root)
        return self.head
    def inorder(self,root):
        if root:
            self.inorder(root.left)

            if self.head is None:
                self.head=Node(root.data)
                self.left=self.head
            else:
                new_node=DllNode(root.data)
                self.left.right=new_node
                new_node.left=self.left
                self.left=new_node

            self.inorder(root.right)


