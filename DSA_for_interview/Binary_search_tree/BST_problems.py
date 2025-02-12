class TreeNode:
    def __init__(self, val):
        self.right = None
        self.left = None
        self.val = val


class BST:
    def insert(self, root, key):
        if root is None:
            return TreeNode(key)

        if key < root.val:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        return root

    def buildBST(self, arr):
        root = None
        for num in arr:
            root = self.insert(root, num)
        return root

    def preorder(self, root):
        if root:
            print(root.val, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.val, end=" ")
            self.inorder(root.right)

    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.val, end=" ")

    # function to return the depth of BST
    def maxDepth(self, root):
        if root:
            l = self.maxDepth(root.left)
            r = self.maxDepth(root.right)
            return 1 + max(l, r)

    def BFS(self, root):
        res = []
        if root is None:
            return 0
        Queue = []
        Queue.append(root)
        while Queue:
            level = len(Queue)
            ans = []
            for i in range(level):
                node = Queue.pop(0)
                ans.append(node.val)
                if node.left:
                    Queue.append(node.left)
                if node.right:
                    Queue.append(node.right)
            res.append(ans)
        return res

    # Function to check whether a Binary Tree is BST or not.
    def is_bst(self, node, min_val, max_val):
        if node is None:
            return True
        if not (min_val < node.data < max_val):
            return False
        return self.is_bst(node.left, min_val, node.data) and self.is_bst(node.right, node.data, max_val)

    def isBST(self, root):
        return self.is_bst(root, float('-inf'), float('inf'))

    # to find maximum path sum
    def findMaxSumHelper(self, root, new_values):
        if root:
            self.findMaxSumHelper(root.left, new_values)
            self.findMaxSumHelper(root.right, new_values)
            if root.right != None and root.left != None:
                res = max(root.left.val, root.right.val)
                new_values.append(root.val + root.left.val + root.right.val)
            elif root.left:
                res = root.left.val
            elif root.right:
                res = root.right.val
            else:
                return
            root.val = max(root.val + res, root.val)

    def helper1(self, root, values):
        if root:
            self.helper1(root.left, values)
            values.append(root.val)
            self.helper1(root.right, values)
        return

    def findMaxSum(self, root):
        if root is None:
            return 0
        values = []
        new_values = []
        self.findMaxSumHelper(root, new_values)
        self.helper1(root, values)
        if new_values:
            return max(max(values), max(new_values))
        return max(values)

    # optimized approach to find the max path sum
    def MaxPathSum(self, root):
        maxi = 0
        val = self.helper(root, maxi)
        return val

    def helper(self, root, maxi):
        if root is None:
            return 0
        leftSum = self.helper(root.left, maxi)
        rightSum = self.helper(root.right, maxi)
        maxi = max(maxi, leftSum + rightSum + root.val)
        return root.val + max(leftSum, rightSum)

    # function to flip binary tree
    def flipBinaryTree(self, root):
        if root is None:
            return root
        if root.left is None and root.left is None:
            return root
        flippedroot = self.flipBinaryTree(root.left)
        root.left.left = root.right
        root.left.right = root
        root.left = root.right = None

        return flippedroot

    #function to find kth smallest element in BST

    def kthSmallest(self, root, k):
        stack = []
        current = root

        while True:
            while current:
                stack.append(current)
                current = current.left  # Move left (smaller values)

            if not stack:
                return -1  # Edge case: k is out of bounds

            current = stack.pop()
            k -= 1  # Decrease k, since we found the next smallest element

            if k == 0:
                return current.data  # Found the k-th smallest element

            current = current.right

    # function to check if two trees have same structure
    def isSameStructure(self, root1, root2):
        if root1 == None and root2 == None:
            return True
        if (root1 != None and root2 != None):
            return (self.isSameStructure(root1.left, root2.left) and self.isSameStructure(root1.right, root2.right))
        return False


    def isSubTree(self, T, S):
        if S is None:
            return True
        if T is None:
            return False
        arr1 = []
        self.preorder1(T, arr1)
        arr2 = []
        self.preorder1(S, arr2)
        i = 0
        j = 0
        while i < len(arr1) and j < len(arr2):
            if arr1[i] == arr2[j]:
                i += 1
                j += 1
            else:
                i += 1
                j = 0
        if j == len(arr2):
            return True
        return False

    #function to build a binary tree from inorder and preorder traversal
    def buildTreeRecur(self,mp,preorder,preIndex,l,r):
        if l > r:
            return None

        rootval = preorder[preIndex[0]]
        preIndex[0] += 1

        root = TreeNode(rootval)

        index = mp[rootval]

        root.left = self.buildTreeRecur(mp , preorder,preIndex,l,index -1)
        root.right = self.buildTreeRecur(mp, preorder, preIndex, index +1, r)

        return root

    def buildTree(self, inorder, preorder):
        mp = { value : idx for idx , value in enumerate(inorder)}
        preIndex = [0]
        return self.buildTreeRecur(mp , preorder,preIndex,0,len(inorder)-1)


arr1 = [10, 5, 3, 7, 15, 13, 17]
# arr2 = [10, 5, 3, 7, 15, 13, 17]
root1 = BST().buildBST(arr1)
# root2 = BST().buildBST(arr2)
# BST().preorder(root)
# print()
# BST().inorder(root)
# print()
# BST().postorder(root)
# print(BST().isSameStructure(root1,root2))
print(BST().MaxPathSum(root1))
