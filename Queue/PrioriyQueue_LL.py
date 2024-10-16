class Node:
    def __init__(self,item=None,next=None,priority=0):
        self.priority=priority
        self.item=item
        self.next=next
        
class PriorityQueue:
    def __init__(self,start=None):
        self.start=start
        self.count=0
    
    def isEmpty(self):
        return self.start is None
        
    def push(self,data,priority):
        n=Node(data,None,priority)
        if self.isEmpty():
            self.start=n
        else:
            if priority<self.start.priority:
                n.next=self.start
                self.start=n
            elif self.start.next is None and priority>self.start.priority:
                    self.start.next=n
            
            else :
                temp=self.start
                while temp.next is not None and priority>=temp.next.priority:
                    temp=temp.next
                n.next=temp.next
                temp.next=n
        self.count+=1
            
    def pop(self):
        if self.isEmpty():
            raise IndexError("Queue is Empty")
        else :
            data=self.start.item
            self.start=self.start.next
            self.count-=1
            return data
            
    def size(self):
        return self.count
    
pq=PriorityQueue()
pq.push("Sudip",3)
pq.push("Soumodip",4)
pq.push("Ganesh",1)
pq.push("Shantana",2)
while pq.isEmpty() is not True:
    print(pq.pop())
                