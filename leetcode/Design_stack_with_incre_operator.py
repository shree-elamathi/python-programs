'''
Design a stack that supports increment operations on its elements.
Implement the CustomStack class:
CustomStack(int maxSize) Initializes the object with maxSize which is the maximum number of elements in the stack.
void push(int x) Adds x to the top of the stack if the stack has not reached the maxSize.
int pop() Pops and returns the top of the stack or -1 if the stack is empty.
void inc(int k, int val) Increments the bottom k elements of the stack by val. If there are less than k elements in
the stack, increment all the elements in the stack.
'''
class CustomStack:
    def __init__(self, maxSize: int):
        self.stack = []
        self.maxSize = maxSize
        self.increment_array = [0] * maxSize  # To keep track of increment values

    def push(self, x: int) -> None:
        if len(self.stack) < self.maxSize:
            self.stack.append(x)
        # If the stack is full, do nothing

    def pop(self) -> int:
        if not self.stack:
            return -1
        idx = len(self.stack) - 1
        increment = self.increment_array[idx]
        if idx > 0:
            self.increment_array[idx - 1] += increment  # Propagate increment to the previous element
        self.increment_array[idx] = 0  # Reset increment for the popped element
        return self.stack.pop() + increment

    def increment(self, k: int, val: int) -> None:
        limit = min(k, len(self.stack)) - 1
        if limit >= 0:
            self.increment_array[limit] += val