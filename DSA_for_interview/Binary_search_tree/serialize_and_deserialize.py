'''
Serialization is to store a tree in an array so that it can be later restored and deserialization is reading tree
back from the array. Complete the functions

serialize() : stores the tree into an array a and returns the array.
deSerialize() : deserializes the array to the tree and returns the root of the tree.
Note: Multiple nodes can have the same data and the node values are always positive integers. Your code will be
correct if the tree returned by deSerialize(serialize(input_tree)) is same as the input tree. Driver code will
print the in-order traversal of the tree returned by deSerialize(serialize(input_tree)).
'''


class Solution:
    def serializehelper(self, root, arr):
        if root is None:
            arr.append(-1)
            return
        arr.append(root.data)
        self.serializehelper(root.left, arr)
        self.serializehelper(root.right, arr)

    # Function to serialize a tree and return a list containing nodes of tree.
    def serialize(self, root):
        arr = []
        self.serializehelper(root, arr)
        return arr
        # code here

    def deserializehelper(self, i, arr):
        if arr[i[0]] == -1:
            i[0] += 1
            return None
        root = Node(arr[i[0]])
        i[0] += 1
        root.left = self.deserializehelper(i, arr)
        root.right = self.deserializehelper(i, arr)

        return root

    # Function to deserialize a list and construct the tree.
    def deSerialize(self, arr):
        i = [0]
        return self.deserializehelper(i, arr)
