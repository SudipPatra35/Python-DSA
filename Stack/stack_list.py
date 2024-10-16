# Stack using list
class stack :
    def __init__(self):
        self.items=[]
        
    def isEmpty(self):
        return len(self.items)==0
    
    def push(self,data):
        self.items.append(data)
        
    def pop(self):
        if self.isEmpty() :
            raise IndexError("Stack is Empty")
        else:
            return self.items.pop()
    
    def peek(self):
        if not self.isEmpty() :
            return self.items[-1]
        else :
            raise IndexError("Stack is Empty")
    
    def size(self):
        return len(self.items)
    
    
# s1=stack()
# s1.push(10)
# s1.push(20)
# s1.push(30)
# s1.push(40)
# print("Top element is : ",s1.peek())
# print("size of stack is :",s1.size() )
# print("Deleted element is : ",s1.pop())
# print("Top element is : ", s1.peek())

