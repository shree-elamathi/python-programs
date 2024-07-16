'''
You are given the root of a binary tree with n nodes. Each node is uniquely assigned a value from 1 to n. You are
also given an integer startValue representing the value of the start node s, and a different integer destValue
representing the value of the destination node t.

Find the shortest path starting from node s and ending at node t. Generate step-by-step directions of such path as a
string consisting of only the uppercase letters 'L', 'R', and 'U'. Each letter indicates a specific direction:

'L' means to go from a node to its left child node.
'R' means to go from a node to its right child node.
'U' means to go from a node to its parent node.
Return the step-by-step directions of the shortest path from node s to node t.
'''


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def findLCA(root, p, q):
    if not root:
        return None
    if root.val == p or root.val == q:
        return root

    left = findLCA(root.left, p, q)
    right = findLCA(root.right, p, q)

    if left and right:
        return root
    return left if left else right


def findPath(root, value, path):
    if not root:
        return False
    if root.val == value:
        return True

    path.append('L')
    if findPath(root.left, value, path):
        return True
    path.pop()

    path.append('R')
    if findPath(root.right, value, path):
        return True
    path.pop()

    return False


def getDirections(root, startValue, destValue):
    # Find the LCA of startValue and destValue
    lca = findLCA(root, startValue, destValue)

    # Find the path from LCA to startValue
    path_to_start = []
    findPath(lca, startValue, path_to_start)

    # Find the path from LCA to destValue
    path_to_dest = []
    findPath(lca, destValue, path_to_dest)

    # Generate the result path
    # All moves to startValue are 'U'
    result = ['U'] * len(path_to_start)

    # Append the moves to destValue
    result.extend(path_to_dest)

    return ''.join(result)