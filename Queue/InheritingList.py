class Queue(list):
   
    
    def isEmpty(self):
        return len(self)==0
    
    def enqueue(self,data):
        self.append(data) 
        
    def dequeue(self):
        if self.isEmpty():
            raise IndexError("Queue is empty")
        else:
            self.pop(0)
    
    def getFront(self):
        return self[0]
    
    def getRear(self):
        return self[-1]
    
    def size(self):
        return len(self)
    
    def printQueue(self):
        print(self)
    
#Implementation    
q1=Queue()
print(q1.isEmpty())
print("size of queue is : ",q1.size())
q1.printQueue()
try :
    print("Front is : ",q1.getFront())
    print("Rear is : ",q1.getRear())
    q1.dequeue()
except Exception as e:
    print(e)

q1.enqueue(10)
q1.enqueue(20)
q1.enqueue(30)
q1.enqueue(40)
q1.enqueue(50)
print("Front is : ",q1.getFront())
print("Rear is : ",q1.getRear())
print("size of queue is : ",q1.size())
q1.printQueue()
q1.dequeue()
print("size of queue is : ",q1.size()) 
q1.printQueue()
print("Front is : ",q1.getFront())
print("Rear is : ",q1.getRear())      