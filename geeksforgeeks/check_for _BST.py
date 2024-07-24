'''
Given the root of a binary tree. Check whether it is a BST or not.
Note: We are considering that BSTs can not contain duplicate Nodes.
A BST is defined as follows:
The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
'''
class Solution:
    def isBST(self,root):
        arr=Solution().inorder(root)
        arr1=sorted(arr)
        if arr==arr1 and len(arr)==len(set(arr)):
            return "true"
        return "false"
    def inorder(self,root,values=None):
        if values is None:
            values=[]
        if root:
            Solution().inorder(root.left,values)
            values.append(root.data)
            Solution().inorder(root.right,values)
        return values
print(Solution().isBST(root=None))