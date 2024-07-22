'''
Given a binary tree. Find the size of its largest subtree which is a Binary Search Tree.
Note: Here Size equals the number of nodes in the subtree.
'''
class Solution:
    def largestBst(self, root):
        self.max_size = 0
        self._largestBSTUtil(root)
        return self.max_size

    def _largestBSTUtil(self, node):
        # Base case: An empty tree is a BST of size 0
        if not node:
            return (0, float('inf'), float('-inf'), True)

        # Recursively get info from left and right subtrees
        l_size, l_min, l_max, l_is_bst = self._largestBSTUtil(node.left)
        r_size, r_min, r_max, r_is_bst = self._largestBSTUtil(node.right)

        # Check if the current node forms a BST
        if l_is_bst and r_is_bst and l_max < node.data < r_min:
            current_size = 1 + l_size + r_size
            self.max_size = max(self.max_size, current_size)
            current_min = min(node.data, l_min)
            current_max = max(node.data, r_max)
            return (current_size, current_min, current_max, True)
        else:
            return (0, 0, 0, False)


if __name__ == "__main__":
    tree = BinaryTree()
    keys = [1,4,4,6,8]

    for key in keys:
        tree.insert(key)