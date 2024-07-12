'''

'''
class Solution:
    def hasPathSum(root, target):
        if not root:
            return False
        if root.right is None and root.left is None:
            if target == root.data:
                return True
        return (Solution().hasPathSum(root.left, target - root.data) or Solution().hasPathSum(root.right, target - root.data))

