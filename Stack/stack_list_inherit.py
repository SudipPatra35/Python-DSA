# Stack using inherit list class
class stack(list) : 
    def isEmpty(self):
        return len(self)==0
    
    def push(self,data):
        self.append(data)
        
    def pop(self):
        if self.isEmpty()==True:
            raise IndexError("Stack is Empty")
        else :
            return super().pop()
        
    def peek(self):
        if self.isEmpty()==True:
            raise IndexError("Stack is Empty")
        else :
            return self[-1]
        
    def size(self):
        return len(self)
    
    def insert(self,index,data):
        raise AttributeError("No attribute, There is no 'insert' in Stack")

s1=stack()
s1.push(10)
s1.push(20)
s1.push(30)
s1.push(40)
print("Top element is : ",s1.peek())
print("size of stack is :",s1.size())
print("Deleted element is : ",s1.pop())
print("Top element is : ", s1.peek()) 
s1.insert(2,50)
    