#Given an integer K and a queue of integers, we need to reverse the order of the first K elements of the
# queue, leaving the other elements in the same relative order.Only following standard operations are allowed on queue.
# enqueue(x) : Add an item x to rear of queue
# dequeue() : Remove an item from front of queue
# size() : Returns number of elements in queue.
# front() : Finds front item.
# Note: The above operations represent the general processings. In-built functions of the respective
# languages can be used to solve the problem.
from collections import deque
class solution:
    def modifyQueue(self,q,k):
        q=deque(q)
        p=deque([])
        for i in range(k):
            p.appendleft(q.popleft())
        for i in q:
            p.append(i)
        return p
q=[1,2,3,4,5,6,7]
k=4
solution().modifyQueue(q,k)


