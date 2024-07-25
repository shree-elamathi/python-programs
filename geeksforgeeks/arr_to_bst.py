'''
Given a sorted array. Convert it into a Height Balanced Binary Search Tree (BST). Return the root of the BST.
Height-balanced BST means a binary tree in which the depth of the left subtree and the right subtree of every node
never differ by more than 1.
Note: The driver code will check the BST, if it is a Height-balanced BST, the output will be true otherwise the output
will be false.
'''
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


class Solution:
    def Form_BST(self,nums,left,right):
        if left>right:
            return None
        mid=left+(right-left)//2
        node=Node(nums[mid])
        node.left=self.Form_BST(nums,left,mid-1)
        node.right=self.Form_BST(nums,mid+1,right)
        return node
    def sortedArrayToBST(self, nums):
        root=self.Form_BST(nums,0,len(nums)-1)
        return root
nums=[1,2,3,4,5,6,7,8]
ans=Solution().sortedArrayToBST(nums)
inorder(ans)
