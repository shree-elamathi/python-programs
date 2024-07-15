'''
You are given a 2D integer array descriptions where descriptions[i] = [parenti, childi, isLefti] indicates that
parenti is the parent of childi in a binary tree of unique values. Furthermore,
If isLefti == 1, then childi is the left child of parenti.
If isLefti == 0, then childi is the right child of parenti.
Construct the binary tree described by descriptions and return its root.
The test cases will be generated such that the binary tree is valid.
'''
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
class Solution:
    def createBinaryTree(self,descriptions):
        nodes = {}
        children = set()
        for parent, child, isLeft in descriptions:
            if parent not in nodes:
                nodes[parent] = Node(parent)
            if child not in nodes:
                nodes[child] = Node(child)
            if isLeft:
                nodes[parent].left = nodes[child]
            else:
                nodes[parent].right = nodes[child]
            children.add(child)
        all_nodes = set(nodes.keys())
        root_val = list(all_nodes - children)[0]
        return nodes[root_val]


descriptions=[[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]]
print(Solution().createBinaryTree(descriptions))