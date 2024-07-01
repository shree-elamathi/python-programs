'''
Given a Linked List Representation of Complete Binary Tree. Your task is to construct the Binary tree from
the given linkedlist and return the root of the tree.
The result will be judged by printing the level order traversal of the Binary tree.
Note: The complete binary tree is represented as a linked list in a way where if the root node is stored at
position i, its left, and right children are stored at position 2*i+1, and 2*i+2 respectively. H is the
height of the tree and this space is used implicitly for the recursion stack.
'''
class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None
class Tree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def convert(head):
    treeNode=Tree(head.data)
    head=head.next
    stack=deque([treeNode])
    rootNode=treeNode
    while len(stack) and head:
        treeNode=stack.pop(left)
        first=head.data
        treeNode.left=Tree(first)
        stack.append(treeNode.left)
        if head.next:
            second=head.next.data
            treeNode.right=Tree(second)
            stack.append(treeNode.right)
            head=head.next.next
        else:
            head=head.next
    return rootNode
