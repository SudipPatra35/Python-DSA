from SLL import *

class Stack(SLL):
    def __init__(self):
        super().__init__()
        self.count=0
        
    def isEmpty(self):
        return super().isEmpty()
    
    def push(self,data):
        self.insertAtStart(data)
        self.count+=1
        
    def pop(self):
        if self.isEmpty():
            raise IndexError("Stack is Empty")
        else:
            data=self.start.item
            self.deleteAtFirst()
            self.count-=1
            return data
            
    def peek(self):
        if self.isEmpty():
            raise IndexError("Stack is Empty")
        else:
            return self.start.item
            
    def size(self):
        return self.count
       

s1=Stack()
s1.push(10)
s1.push(20)
s1.push(30)
s1.push(40)
print("Top element is : ",s1.peek())
print("size of stack is :",s1.size() )
print("Deleted element is : ",s1.pop())
print("Top element is : ", s1.peek())  
print("size of stack is :",s1.size() ) 