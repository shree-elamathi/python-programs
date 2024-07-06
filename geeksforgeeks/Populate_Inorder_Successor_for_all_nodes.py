'''
Given a Binary Tree, complete the function to populate the next pointer for all nodes. The next pointer
for every node should point to the Inorder successor of the node.
You do not have to return or print anything. Just make changes in the root node given to you.
Note: The node having no in-order successor will be pointed to -1. You don't have to add -1 explicitly,
the driver code will take care of this.
'''
class Node:
    def __init__(self, val):
        self.right = None
        self.val = val
        self.left = None
        self.next = None
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

def populate(root):
    def inorder(node):
        nonlocal prev
        if not node:
            return
        inorder(node.left)
        if prev:
            prev.next=node
        prev=node
        inorder(node.right)
    prev=None
    inorder(root)


if __name__=='__main__':
    root = Node(10)
    root = insert(root, 8)
    root = insert(root, 12)
    root = insert(root, 3)