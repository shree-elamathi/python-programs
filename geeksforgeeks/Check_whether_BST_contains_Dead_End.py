# Given a Binary Search Tree that contains unique positive integer values greater than 0.
# The task is to complete the function isDeadEnd which returns true if the BST contains a dead end
# else returns false. Here Dead End means a leaf node, at which no other node can be inserted.

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

def inorder(root,values=None)->list:
    if values is None:
        values=[]
    if root:
        inorder(root.left,values)
        values.append(root.val)
        inorder(root.right,values)
    return values

def leafnodes(root: Node,leafnode=None)->list:
    if leafnode is None:
        leafnode=[]
    if not root:
        return leafnode
    if (not root.left and not root.right):
        leafnode.append(root.val)
        return leafnode
    if root.left:
        leafnodes(root.left,leafnode)
    if root.right:
        leafnodes(root.right,leafnode)
    return leafnode
def isDeadEnd( root):
    arr1=leafnodes(root)
    arr2=inorder(root)
    a=0
    for i in arr1:
        if i==1 and i+1 in arr2:
            a+=1
        elif i+1 in arr2 and i-1 in arr2:
            a+=1
        else:
            a=a
    if a>0:
        return True
    else:
        return False


if __name__=='__main__':
    root = Node(8)
    root = insert(root, 7)
    root = insert(root, 10)
    root = insert(root, 2)
    root = insert(root, 9)
    root = insert(root, 13)
print(isDeadEnd(root))
