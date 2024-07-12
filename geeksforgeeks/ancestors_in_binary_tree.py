'''
Given a Binary Tree and an integer target. Find all the ancestors of the given target.
Note:
The ancestor of node x is node y, which is at the upper level of node x, and x is directly connected
with node y. Consider multiple levels of ancestors to solve this problem.
In case there are no ancestors available, return an empty list.
'''
from collections import deque
class Node:
    def __init__(self,val):
        self.data=val
        self.left=None
        self.right=None

def insert(root,data):
    if root is None:
        root=Node(data)
        return root
    q=deque()
    q.append(root)
    while q:
        temp=q.popleft()
        if temp.left is None:
            temp.left=Node(data)
            break
        else:
            q.append(temp.left)
        if temp.right is None:
            temp.right=Node(data)
            break
        else:
            q.append(temp.right)
    return root
def inorderTraversal(root):
    if not root:
        return
    inorderTraversal(root.left)
    print(root.data, end=" ")
    inorderTraversal(root.right)
def Ancestors(root,target):
    def inorder(root):
        nonlocal ans,found
        if not root:
            return
        if root.data==target:
            found=True
            return
        ans.append(root.data)
        inorder(root.left)
        if found:
            return
        inorder(root.right)
        if found:
            return
        ans.pop()
    ans=[]
    found=False
    inorder(root)
    return ans

def hasPathSum( root, target):
    if not root:
        return False
    if root.right is None and root.left is None:
        if target==root.data:
            return True
    return (hasPathSum(root.left,target-root.data) or hasPathSum(root.right,target-root.data))

if __name__ == "__main__":
    root = None
    # Insertion of nodes
    root = insert(root, 1)
    root = insert(root, 2)
    root = insert(root, 3)
    root = insert(root, 4)
    root = insert(root, 6)
    root = insert(root, 5)
    root = insert(root, 7)
target=13
print(hasPathSum(root,target))
