'''
Given a binary tree, your task is to find all duplicate subtrees from the given binary tree.
Duplicate Subtree : Two trees are duplicates if they have the same structure with the same node values.
Note:  Return the root of each tree in the form of a list array & the driver code will print the tree in
pre-order tree traversal in lexicographically increasing order.
'''
class Solution:
    def printAllDups(self,root):
        def duplify(root):
            if root:
                t=(root.val,duplify(root.left),duplify(root.right))
                trees[t]=trees.get(t,0)+1
                if trees[t]==2:
                    res.append(root)
                return t
        trees={}
        res=[]
        duplify(root)
        return res