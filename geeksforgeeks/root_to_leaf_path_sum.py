'''

'''
class Solution:
    def hasPathSum(self, root, target):
        def inorder(root):
            nonlocal ans, found
            if not root:
                return
            if sum(ans) == target:
                found = True
                return
            ans.append(root.data)
            inorder(root.left)
            if found:
                return
            inorder(root.right)
            if found:
                return
        ans = []
        found = False
        inorder(root)
        return True
