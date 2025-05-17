'''
You are given the root of a binary tree root. Invert the binary tree and return its root.
'''


class Solution:
    def invertTree(self, root):
        if root:

            #check if the root node has either left or right subtree
            if root.left or root.right:

                #if available then swap them
                new = root.left
                root.left = root.right
                root.right = new

            #After swapping move to the left and right subtree
            self.invertTree(root.left)
            self.invertTree(root.right)

        #Finally return the root after traversing to all the nodes
        return root