'''
Given two BSTs, return elements of merged BSTs in sorted form.
'''
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.data = key
class Solution:
    def merge(self,root1,root2):
        arr=[]
        arr=arr+inorder(root1)
        arr=arr+inorder(root2)
        return arr
def inorder(root,values=None)->list:
   if values is None:
       values=[]
   if root:
       inorder(root.left,values)
       values.append(root.data)
       inorder(root.right,values)
   return values

print(Solution().merge())