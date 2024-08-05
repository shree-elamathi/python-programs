'''
Given a binary tree, return an array where elements represent the bottom view of the binary tree from left to right.

Note: If there are multiple bottom-most nodes for a horizontal distance from the root, then the latter one in the
level traversal is considered. For example, in the below diagram, 3 and 4 are both the bottommost nodes at a
horizontal distance of 0, here 4 will be considered.
'''
from collections import deque, defaultdict
class Solution:
    def bottomView(self, root):
        if not root:
            return []

            # Queue for level order traversal (node, horizontal distance)
        queue = deque([(root, 0)])

        # Dictionary to store the last node at each horizontal distance
        hd_node_map = {}

        while queue:
            node, hd = queue.popleft()

            # Update the node for this horizontal distance
            hd_node_map[hd] = node.val

            # Enqueue left and right children with updated horizontal distances
            if node.left:
                queue.append((node.left, hd - 1))
            if node.right:
                queue.append((node.right, hd + 1))

        # Extract the bottom view from the map, sorted by horizontal distance
        bottom_view = [hd_node_map[hd] for hd in sorted(hd_node_map)]

        return bottom_view