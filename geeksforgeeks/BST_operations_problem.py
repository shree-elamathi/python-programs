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
#Given two BSTs containing N1 and N2 distinct nodes respectively and given a value x, your task is to complete
# the function countPairs(), that returns the count of all pairs of (a, b), where a belongs to one BST
# and b belongs to another BST, such that a + b = x.

def countpairs(root1,root2,x):
   arr1=inorder(root1)
   arr2=inorder(root2)
   pairs=[]
   for i in arr1:
       for j in arr2:
           if i+j==x:
               pairs.append(i)
               pairs.append(j)
   return (int(len(pairs)/2))


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

#This method is more time complex
def inorder(root):
    if root:
        yield from inorder_generator(root.left)
        yield root.val
        yield from inorder_generator(root.right)

def count(root1,root2,x):
    arr=[]
    for i in inorder(root1):
        for j in inorder(root2):
            if i+j==x:
                arr.append(i)
                arr.append(j)
    return (int(len(arr)/2))



if __name__=='__main__':
    root = Node(8)
    root = insert(root, 7)
    root = insert(root, 10)
    root = insert(root, 2)
    root = insert(root, 9)
    root = insert(root, 13)
print(isDeadEnd(root))
