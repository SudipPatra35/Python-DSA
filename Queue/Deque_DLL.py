class Node:
    def __init__(self,item=None,prev=None,next=None):
        self.item=item
        self.next=next
        self.prev=prev
        
class Deque:
    def __init__(self):
        self.front=None
        self.rear=None
        self.count=0
    
    def isEmpty(self):
        return self.front is None
    
    def insertFront(self,data):
        n=Node(data,None,self.front)
        if self.isEmpty():
            self.rear=n
        else:
            self.front.prev=n
        self.front=n
        self.count+=1
    def insertRear(self,data):
        n=Node(data,self.rear,None)
        if self.isEmpty():
            self.front=n
        else:
            self.rear.next=n
        self.rear=n
        self.count+=1
    def deleteFront(self):
        if self.isEmpty():
            raise IndexError ("Deque is Empty")
        else :
            if(self.front==self.rear):
                self.front=None
                self.rear=None
                return
            self.front.next.prev=None
            self.front=self.front.next
            self.count-=1
            
    def deleteRear(self):
        if self.isEmpty():
            raise IndexError ("Deque is Empty")
        else :
            if(self.front==self.rear):
                self.front=None
                self.rear=None
                return
            self.rear.prev.next=None
            self.rear=self.rear.prev
            self.count-=1  
              
    def getFront(self):
        if self.isEmpty():
            raise IndexError("Deque is Empty")
        else:
            return self.front.item
        
    def getRear(self):
        if self.isEmpty():
            raise IndexError("Deque is Empty")
        else:
            return self.rear.item
        
    def size(self):
        return self.count
q1=Deque()
print(q1.isEmpty())
q1.insertFront(10)
# q1.insertRear(20)
q1.insertFront(30)
q1.insertFront(60)
q1.insertFront(35)
# q1.insertRear(40)
print("size of queue is :",q1.size())
print("Front is :",q1.getFront(),",Rear is :",q1.getRear())
q1.deleteFront()
# q1.insertRear(50)
print("Front is :",q1.getFront(),",Rear is :",q1.getRear())
q1.deleteRear()
# q1.printQueue()
print("Front is :",q1.getFront(),",Rear is :",q1.getRear())
print("size of queue is :",q1.size())
        