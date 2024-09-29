'''
Design a data structure to store the strings' count with the ability to return the strings with minimum and maximum
counts.
Implement the AllOne class:
AllOne() Initializes the object of the data structure.
inc(String key) Increments the count of the string key by 1. If key does not exist in the data structure, insert it
with count 1.
dec(String key) Decrements the count of the string key by 1. If the count of key is 0 after the decrement, remove it
from the data structure. It is guaranteed that key exists in the data structure before the decrement.
getMaxKey() Returns one of the keys with the maximal count. If no element exists, return an empty string "".
getMinKey() Returns one of the keys with the minimum count. If no element exists, return an empty string "".
Note that each function must run in O(1) average time complexity.
'''


class Node:
    def __init__(self, count):
        self.count = count
        self.keys = set()
        self.prev = None
        self.next = None


class AllOne:
    def __init__(self):
        self.key_count_map = {}  # Maps key to its count
        self.count_node_map = {}  # Maps count to its corresponding node in the doubly linked list
        self.head = Node(float('-inf'))  # Dummy head node
        self.tail = Node(float('inf'))  # Dummy tail node
        self.head.next = self.tail
        self.tail.prev = self.head

    def _add_node_after(self, new_node, prev_node):
        """Add new_node right after prev_node."""
        new_node.prev = prev_node
        new_node.next = prev_node.next
        prev_node.next.prev = new_node
        prev_node.next = new_node

    def _remove_node(self, node):
        """Remove node from the doubly linked list."""
        node.prev.next = node.next
        node.next.prev = node.prev
        del self.count_node_map[node.count]

    def inc(self, key: str) -> None:
        # Step 1: Increment the count of the key
        if key in self.key_count_map:
            count = self.key_count_map[key]
            self.key_count_map[key] += 1
        else:
            count = 0
            self.key_count_map[key] = 1

        # Step 2: Move the key to the next count node
        current_node = self.count_node_map.get(count)
        next_count = count + 1

        if next_count not in self.count_node_map:
            new_node = Node(next_count)
            self.count_node_map[next_count] = new_node
            self._add_node_after(new_node, current_node if current_node else self.head)

        self.count_node_map[next_count].keys.add(key)

        if current_node:
            current_node.keys.remove(key)
            if not current_node.keys:
                self._remove_node(current_node)

    def dec(self, key: str) -> None:
        # Step 1: Decrement the count of the key
        count = self.key_count_map[key]
        current_node = self.count_node_map[count]
        next_count = count - 1

        if count == 1:
            del self.key_count_map[key]
        else:
            self.key_count_map[key] -= 1

        # Step 2: Move the key to the previous count node (or remove it if count is 0)
        current_node.keys.remove(key)
        if not current_node.keys:
            self._remove_node(current_node)

        if next_count > 0:
            if next_count not in self.count_node_map:
                new_node = Node(next_count)
                self.count_node_map[next_count] = new_node
                self._add_node_after(new_node, current_node.prev)
            self.count_node_map[next_count].keys.add(key)

    def getMaxKey(self) -> str:
        if self.tail.prev == self.head:
            return ""
        return next(iter(self.tail.prev.keys))

    def getMinKey(self) -> str:
        if self.head.next == self.tail:
            return ""
        return next(iter(self.head.next.keys))
