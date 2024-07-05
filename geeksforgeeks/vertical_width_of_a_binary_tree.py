'''
Given a Binary Tree. You need to find and return the vertical width of the tree.
'''
def verticalWidth(root):
    if not root:
        return 0
    min_p=max_p=0
    def traverse(node,pos):
        nonlocal min_p,max_p
        if not node:
            return
        min_p=min(min_p,pos)
        max_p=max(max_p,pos)
        traverse(node.left,pos-1)
        traverse(node.right,pos+1)
    traverse(root,0)
    return max_p-min_p+1
