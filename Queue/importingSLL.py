from SLL import * 
class Queue:
    def __init__(self):
        self.myList=SLL()
        self.rear=self.myList.start
        self.count=0
        
    def isEmpty(self):
        return self.front is None
    
    def enqueue(self,data):
        if self.myList.start is None:
            self.myList.insertAtStart(data)
        self.rear=self.rear.next
        self.count +=1
        
    def dequeue(self):
        
    
    
    
    
q1=Queue()
print(q1.isEmpty())    