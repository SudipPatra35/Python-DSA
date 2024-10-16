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
        
class Queue():
    def __init__(self):
        self.s1=stack()
        self.s2=stack()
    def enqueue(self, data):
        self.s1.push(data)
    
    def dequeue(self):
        while not self.s1.isEmpty():
            self.s2.push(self.s1.pop())
        data=self.s2.pop()
        while not self.s2.isEmpty():
            self.s1.push(self.s2.pop())
        return data
    
    def printQueue(self):
        for i in self.s1.items:
            print(i,end=" ")
        print()
        
q1=Queue()
q1.enqueue(10)
q1.enqueue(20)
q1.enqueue(30)
q1.enqueue(40)
q1.printQueue()
print(q1.dequeue())
q1.printQueue()