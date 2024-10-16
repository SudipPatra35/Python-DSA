class Node:
    def __init__(self,item=None,prev=None,next=None):
        self.item=item
        self.prev=prev
        self.next=next

class CDLL:
    def __init__(self,start=None):
        self.start=start
        
    def isEmpty(self):
        return self.start is None
    
    def insertAtStart(self,data):
        n=Node(data)
        if self.start is None:
            n.prev=n
            n.next=n
            self.start=n
        else : 
            n.prev=self.start.prev
            n.next=self.start
            self.start.prev.next=n
            self.start.prev=n
            if self.start.next==self.start.prev :
                self.start.next=n
            self.start=n
        
    def insertAtLast(self,data):
        n=Node(data)
        if self.start is None:
            n.prev=n
            n.next=n
            self.start=n
        else :
            n.prev=self.start.prev
            n.next=self.start
            self.start.prev.next=n
            self.start.prev=n  
    
    def insertAfter(self,after,data):
         temp=self.search(after)
         if temp is not None:
             if temp.item==self.start.prev.item:
                 self.insertAtLast(data)
             else:
                 n=Node(data,temp,temp.next)
                 temp.next.prev=n
                 temp.next=n
#Delete Element :
    def deleteAtStart(self):
        if self.start.next==self.start:
            self.start=None
        else :
            self.start.next.prev=self.start.prev
            self.start.prev.next=self.start.next
            self.start=self.start.next
            
    def deleteAtLast(self):
        if self.start.next==self.start:
            self.start=None
        else:
            self.start.prev.prev.next=self.start
            self.start.prev=self.start.prev.prev
            
    def deleteEle(self,data):
        if self.start.next==self.start and self.start.item==data:
            self.start=None
        else :
            temp=self.search(data)
            if temp.item==self.start.item :
                self.deleteAtStart()
            elif temp.item==self.start.prev.item:
                self.deleteAtLast()
            else :
                temp.next.prev=temp.prev
                temp.prev.next=temp.next

#Search Element :
    def search(self,data):
        if self.start is not None :
            temp =self.start
            while True:
                if temp.item == data:
                    return temp
                temp=temp.next
                if temp==self.start:
                    break
            return None   
#print List:
    def printLL(self):
        if self.isEmpty() is True: 
            print("List is Empty")
        else :
            temp=self.start
            while True :
                print(temp.item,end=" ")
                temp=temp.next
                if temp == self.start:
                    break 
            print()   
 #Iterator method :
    def __iter__(self):
        return CDLLIterator(self.start)        
#make Iterator :
class CDLLIterator:
    def __init__(self,start):
        self.current=start
        self.start=start
        self.count=0
    def __iter__(self):
        return self
    def __next__(self):
        if self.current == None :
            raise StopIteration
        if self.current == self.start and self.count==1:
            raise StopIteration
        else:
            self.count=1
        data=self.current.item
        self.current=self.current.next
        return data
        
        
                    
myList=CDLL()
print(myList.isEmpty())
myList.insertAtStart(20)
myList.insertAtLast(40)
myList.insertAtStart(10)
myList.insertAtLast(50)
myList.insertAfter(50,60)
myList.insertAfter(20,30)
myList.printLL()
myList.deleteEle(30)
print("After delete : ")
for i in myList:
    print(i,end=" ")