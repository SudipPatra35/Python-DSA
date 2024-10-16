class Deque:
    def __init__(self):
        self.myList=[]
        
    def isEmpty(self):
        return len(self.myList)==0
    
    def insertFront(self,data):
        self.myList.insert(0,data)
    
    def insertRear(self,data):
        self.myList.append(data)
    
    def deleteFront(self):
        if self.isEmpty():
            raise IndexError ("Deque is Empty")
        else :
            self.myList.remove(self.myList[0])
    
    def deleteRear(self):
        if self.isEmpty():
            raise IndexError ("Deque is Empty")
        else :
            self.myList.remove(self.myList[-1])
    
    def getFront(self):
        if self.isEmpty():
            raise IndexError ("Deque is Empty")
        else :
            return self.myList[0]
    
    def getRear(self):
        if self.isEmpty():
            raise IndexError ("Deque is Empty")
        else :
            return self.myList[-1]
    
    def size(self):
        return len(self.myList)
    

q1=Deque()
print(q1.isEmpty())
q1.insertFront(10)
q1.insertRear(20)
q1.insertFront(30)
q1.insertRear(40)
print("size of queue is :",q1.size())
print("Front is :",q1.getFront(),",Rear is :",q1.getRear())
q1.deleteFront()
q1.insertRear(50)
print("Front is :",q1.getFront(),",Rear is :",q1.getRear())
q1.deleteRear()
# q1.printQueue()
print("size of queue is :",q1.size())