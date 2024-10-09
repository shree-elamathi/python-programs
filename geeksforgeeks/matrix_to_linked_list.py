'''
Given a Matrix mat of n*n size. Your task is constructing a 2D linked list representation of the given matrix.
'''


class Node:
    def __init__(self, value=0):
        self.val = value
        self.right = None
        self.down = None


class Solution:
    def construct2DLinkedList(self, mat):
        if not mat or not mat[0]:
            return None

        n = len(mat)

        # Create a matrix of Node references
        nodeMatrix = [[None for _ in range(n)] for _ in range(n)]

        # Fill the matrix with Nodes
        for i in range(n):
            for j in range(n):
                nodeMatrix[i][j] = Node(mat[i][j])

        # Link the Nodes
        for i in range(n):
            for j in range(n):
                if j < n - 1:
                    nodeMatrix[i][j].right = nodeMatrix[i][j + 1]  # Link right neighbor
                if i < n - 1:
                    nodeMatrix[i][j].down = nodeMatrix[i + 1][j]  # Link down neighbor

        # Return the head of the 2D linked list (top-left corner)
        return nodeMatrix[0][0]

    # Method to print the 2D linked list for debugging
    def print2DLinkedList(self, head):
        row_head = head
        while row_head:
            current = row_head
            while current:
                print(current.val, end=" -> ")
                current = current.right
            print("None")
            row_head = row_head.down


# Example usage:
mat = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

solution = Solution()
head = solution.construct2DLinkedList(mat)
solution.print2DLinkedList(head)
