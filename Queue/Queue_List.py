class Queue:
    def __init__(self):
        self.items=[]
        
    def isEmpty(self):
        return len(self.items)==0
    
    def enqueue(self,data):
        self.items.append(data)
    
    def dequeue(self):
         if not self.isEmpty() :
           self.items.remove(self.items[0]) 
         else :
            raise IndexError("Queue is Empty")
        
    def getFront(self):
         if not self.isEmpty() :
            return self.items[0]
         else :
            raise IndexError("Queue is Empty")
    
    def getRear(self):
         if not self.isEmpty() :
            return self.items[-1]
         else :
            raise IndexError("Queue is Empty")
    
    def size(self):
        return len(self.items)
    
    def printQueue(self):
        for i in self.items:
            print(i,end=" ")
        print()

q1=Queue()
print(q1.isEmpty())
q1.enqueue(10)
q1.enqueue(20)
q1.enqueue(30)
q1.enqueue(40)
print("size of queue is : ",q1.size())
q1.printQueue()
print("Front is : ",q1.getFront())
print("Rear is : ",q1.getRear())
q1.dequeue()
q1.enqueue(50)
print("Front is : ",q1.getFront())
print("Rear is : ",q1.getRear())
q1.printQueue()
print("size of queue is : ",q1.size())