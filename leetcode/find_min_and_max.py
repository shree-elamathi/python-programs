'''
A critical point in a linked list is defined as either a local maxima or a local minima.
A node is a local maxima if the current node has a value strictly greater than the previous node and the
next node.
A node is a local minima if the current node has a value strictly smaller than the previous node and the
next node.
Note that a node can only be a local maxima/minima if there exists both a previous node and a next node.
Given a linked list head, return an array of length 2 containing [minDistance, maxDistance] where
minDistance is the minimum distance between any two distinct critical points and maxDistance is the
maximum distance
between any two distinct critical points. If there are fewer than two critical points, return [-1, -1].
'''
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def insert(self,data):
        new_Node=Node(data)
        current_Node=self.head
        if self.head is None:
            self.head=new_Node
            return
        while current_Node.next:
            current_Node=current_Node.next
        current_Node.next=new_Node
    def nodesBetweenCriticalPoints(self):
        temp=self.head
        arr=[]
        prev=None
        c=1
        count=[]
        while temp.next:
            if prev is None:
                prev=temp
                temp=temp.next
            else:
                c+=1
                if prev.data<temp.data>temp.next.data:
                    count.append(c)
                if prev.data>temp.data<temp.next.data:
                    count.append(c)
                prev=temp
                temp=temp.next
        if len(count)<2:
            return [-1,-1]
        else:
            i=0
            min_dist=count[len(count)-1]
            while i<len(count)-1:
                min_dist=min(min_dist,count[i+1]-count[i])
                i+=1
            max_dist=(count[len(count)-1]-count[0])
            arr.append(min_dist)
            arr.append(max_dist)
            return arr
ll=LinkedList()
arr1=[6,8,4,1,9,6,6,10,6]
for i in arr1:
    ll.insert(i)
print(ll.nodesBetweenCriticalPoints())