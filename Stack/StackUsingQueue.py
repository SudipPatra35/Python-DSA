class Queue:
    def __init__(self):
        self.items=[]
    def isEmpty(self):
        return len(self.items)==0
    
    def push(self,data):
        self.items.append(data)
        
    def pop(self):
        if self.isEmpty():
            # print("Empty")
            return
        else :
            return self.items.pop(0)
            
    def printQueue(self):
        for i in self.items:
            print(i,end=" ")
        print()
        
        
class Stack(Queue):
    def __init__(self):
        self.q1=Queue()
        self.q2=Queue()
        
    def push(self,data):
        while not self.q1.isEmpty():
             self.q2.push(self.q1.pop())
        self.q1.push(data)  
        while not self.q2.isEmpty():
             self.q1.push(self.q2.pop())   
    def pop(self):
        return self.q1.pop()
      
    def printStack(self) :
        for i in self.q1.items:
            print(i)  
        
        
# q1=Queue()
# print(q1.isEmpty())
# q1.push(10)
# q1.push(20)
# q1.push(30)
# q1.push(40)
# q1.printQueue()

s=Stack()
s.push(10)
s.push(20)
s.push(30)
s.push(40)
s.push(50)
s.printStack()
print(s.pop())