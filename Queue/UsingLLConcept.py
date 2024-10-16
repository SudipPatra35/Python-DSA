class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next
        
class Queue:
    def __init__(self):
        self.front=None
        self.rear=None
        self.count=0
        
    def isEmpty(self):
        return self.rear is None
    
    def getFront(self):
        if  self.isEmpty():
            raise IndexError("Queue is Empty")  
        else :
            return self.front.item
    def getRear(self):
         if  self.isEmpty():
            raise IndexError("Queue is Empty")  
         else:
            return self.rear.item
      
    def enqueue(self,data):
        n=Node(data)
        if self.isEmpty():
            self.front=n
        else:
            self.rear.next=n
        self.rear=n
        self.count+=1
        
    def dequeue(self):
        if  self.isEmpty():
            raise IndexError("Queue is Empty")  
        elif self.rear==self.front:
            self.rear=None
            self.front=None
        else :
            self.front=self.front.next
        self.count-=1
            
    def size(self):
        return self.count
    
    def printQueue(self):
        if self.isEmpty():
            print ("Queue is Empty")
        else:
            temp = self.front
            while temp is not None:
                print(temp.item, end=" ")
                temp = temp.next
            print()
 
 
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