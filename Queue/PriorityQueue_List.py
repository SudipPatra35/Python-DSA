class PriorityQueue:
    def __init__(self):
        self.items=[]
    
    def isEmpty(self):
        return len(self.items)==0
        
    def push(self,data,priority):
        index=0
        while index<len(self.items) and self.items[index][1] < priority:
            index+=1
        self.items.insert(index,(data,priority))
        
    def pop(self):
        if self.isEmpty():
            raise IndexError("Queue is empty")
        else :
            data=self.items.pop(0)[0]
            return data
        
    def size(self):
        return len(self.items)
    
pq=PriorityQueue()
pq.push("Sudip",3)
pq.push("Soumodip",4)
pq.push("Ganesh",1)
pq.push("Shantana",2)
while pq.isEmpty() is not True:
    print(pq.pop())