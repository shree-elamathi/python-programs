'''
Design your implementation of the circular double-ended queue (deque).
Implement the MyCircularDeque class:
MyCircularDeque(int k) Initializes the deque with a maximum size of k.
boolean insertFront() Adds an item at the front of Deque. Returns true if the operation is successful, or false
otherwise.
boolean insertLast() Adds an item at the rear of Deque. Returns true if the operation is successful, or false
otherwise.
boolean deleteFront() Deletes an item from the front of Deque. Returns true if the operation is successful, or false
otherwise.
boolean deleteLast() Deletes an item from the rear of Deque. Returns true if the operation is successful, or false
otherwise.
int getFront() Returns the front item from the Deque. Returns -1 if the deque is empty.
int getRear() Returns the last item from Deque. Returns -1 if the deque is empty.
boolean isEmpty() Returns true if the deque is empty, or false otherwise.
boolean isFull() Returns true if the deque is full, or false otherwise.
'''
class MyCircularDeque:

    def __init__(self, k: int):
        self.deque = [0] * k  # Create a fixed-size list
        self.front = 0  # Pointer for front
        self.rear = 0  # Pointer for rear
        self.size = 0  # Current size of the deque
        self.capacity = k  # Maximum capacity of the deque

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        self.front = (self.front - 1) % self.capacity  # Move front pointer backward
        self.deque[self.front] = value
        self.size += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        self.deque[self.rear] = value
        self.rear = (self.rear + 1) % self.capacity  # Move rear pointer forward
        self.size += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.front = (self.front + 1) % self.capacity  # Move front pointer forward
        self.size -= 1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.rear = (self.rear - 1 + self.capacity) % self.capacity  # Move rear pointer backward
        self.size -= 1
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.deque[self.front]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.deque[(self.rear - 1 + self.capacity) % self.capacity]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capacity

