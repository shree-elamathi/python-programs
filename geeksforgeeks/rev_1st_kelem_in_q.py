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


