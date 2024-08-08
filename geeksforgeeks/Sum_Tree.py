'''
Given a Binary Tree. Check for the Sum Tree for every node except the leaf node. Return true if it is a Sum Tree
otherwise, return false.
A SumTree is a Binary Tree where the value of a node is equal to the sum of the nodes present in its left subtree
and right subtree. An empty tree is also a Sum Tree as the sum of an empty tree can be considered to be 0. A leaf
node is also considered a Sum Tree.
'''
class Solution:
    def is_sum_tree(self,node):
        def checksumtree(node):
            if node is None:
                return True,0
            if node.left is None and node.right is None:
                return True,node.data
            leftIsSumTree,leftsum=checksumtree(node.left)
            rightIsSumTree, rightsum=checksumtree(node.right)
            currentIsSumTree=(leftIsSumTree and rightIsSumTree and node.data==leftsum+rightsum)
            return currentIsSumTree,leftsum+rightsum+node.data
        result, _=checksumtree(node)
        return result