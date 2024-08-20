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

#def countpairs(root1,root2,x):
#  arr1=inorder(root1)
#  arr2=inorder(root2)
#  pairs=[]
#  for i in arr1:
#      for j in arr2:
#          if i+j==x:
#              pairs.append(i)
#              pairs.append(j)
#  return (int(len(pairs)/2))
#def serialize(root):


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
def countpairs(root1,root2,x):
    arr1=inorder(root1)
    n1=len(arr1)
    arr2=inorder(root2)
    n2=len(arr2)
    i=0
    j=-1
    res=0
    while i<n1 and j>=-n2:
        if arr1[i]+arr2[j]==x:
            res+=1
            i+=1
            j-=1
        elif arr1[i]+arr2[j]<x:
            i+=1
        else:
            j-=1
    return res

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
#Given the root of a binary search tree and a number n, find the greatest number in the binary search
# tree that is less than or equal to n.
def findmax(root,n):
    ans=None
    while root:
        if root.val>n:
            root=root.left
        else:
            ans=root.val
            root=root.right
    if ans:
        return ans
    else:
        return -1

#This method is more time complex
#def inorder(root):
#   if root:
#       yield from inorder_generator(root.left)
#       yield root.val
#       yield from inorder_generator(root.right)
#def count(root1,root2,x):
#   arr=[]
#   for i in inorder(root1):
#       for j in inorder(root2):
#           if i+j==x:
#               arr.append(i)
#               arr.append(j)
#   return (int(len(arr)/2))
#Another method
#class Solution:
#   def dfs(self, root, s):
#       if root == None: return
#       s.add(root.data)
#       self.dfs(root.left, s)
#       if root.data < x: self.dfs(root.right, s)
#   def dfs2(self, root, s, x, ans):
#       if root == None: return
#       if x - root.data in s:
#           ans[0] += 1
#       self.dfs2(root.left, s, x, ans)
#       if root.data < x: self.dfs2(root.right, s, x, ans)
#   def countPairs(self, root1, root2, x):
#       s = set()
#       self.dfs(root1, s)
#       ans = [0]
#       self.dfs2(root2, s, x, ans)
#       return ans[0]
'''
Given a binary tree and a node data called target. Find the minimum time required to burn the complete binary tree 
if the target is set on fire. It is known that in 1 second all nodes connected to a given node get burned. That is 
its left child, right child, and parent.
Note: The tree contains unique values.
'''
from collections import deque


class Solution:
    def mark_parents(self, root, parent_map):
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node.left:
                parent_map[node.left] = node
                queue.append(node.left)
            if node.right:
                parent_map[node.right] = node
                queue.append(node.right)

    def find_target(self, root, target):
        if not root:
            return None
        if root.data == target:
            return root
        left = self.find_target(root.left, target)
        if left:
            return left
        return self.find_target(root.right, target)

    def minTime(self, root, target):
        if not root:
            return 0

        # Step 1: Mark the parent pointers for all nodes
        parent_map = {}
        self.mark_parents(root, parent_map)

        # Step 2: Find the target node
        target_node = self.find_target(root, target)

        # Step 3: Perform BFS from the target node to calculate the time
        visited = set()
        queue = deque([(target_node, 0)])  # (node, time)
        visited.add(target_node)
        max_time = 0

        while queue:
            node, time = queue.popleft()
            max_time = max(max_time, time)

            # Check the left child
            if node.left and node.left not in visited:
                queue.append((node.left, time + 1))
                visited.add(node.left)

            # Check the right child
            if node.right and node.right not in visited:
                queue.append((node.right, time + 1))
                visited.add(node.right)

            # Check the parent
            if node in parent_map and parent_map[node] not in visited:
                queue.append((parent_map[node], time + 1))
                visited.add(parent_map[node])

        return max_time

if __name__=='__main__':
    root = Node(10)
    root = insert(root, 20)
    root = insert(root, 30)
    root = insert(root, 60)
    root = insert(root, 40)
print(inorder(root,values=None))
