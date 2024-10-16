class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next

class Stack:
    def __init__(self):
        self.start=None
        self.count=0
    
    def isEmpty(self):
        return self.start is None
    
    def push(self,data):
        n=Node(data,self.start)
        self.start=n
        self.count=self.count+1
        
    def pop(self):
        if self.isEmpty():
            raise IndexError ("Stack is Empty ")
        else :
            data=self.start.item
            self.start=self.start.next
            self.count=self.count-1
            return data
    def peek(self):
         if self.isEmpty():
            raise IndexError ("Stack is Empty ")
         else :
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
            
            