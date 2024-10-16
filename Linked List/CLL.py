class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next

class CLL:
    def __init__(self,last=None):
        self.last=last
    
    def isEmpty(self):
        return self.last is None
 
# insert Element :   
    def insertAtStart(self,data):
        n=Node(data)
        if self.last is None:
            self.last=n
            self.last.next=self.last
        else :
            n.next=self.last.next
            self.last.next=n
         
    def insertAtLast(self,data):
        n=Node(data)
        if self.last is None:
            self.last=n
            self.last.next=self.last
        else :
            n.next=self.last.next
            self.last.next=n
            self.last=n
     
    def insertAfter(self,after,data):
        if self.last.item==after:
            self.insertAtLast(data)
        else :
            temp=self.search(after)
            n=Node(data,temp.next)
            temp.next=n
                
 #Delete Element :
    def deleteAtStart(self):
        if self.last is not None:       
            if self.last.next == self.last :
                self.last=None
            else :
                temp=self.last.next.next
                self.last.next.next=None
                self.last.next=temp
                
    def deleteAtLast(self):
        if self.last is not None:       
            if self.last.next == self.last :
                self.last=None
            else :
                temp=self.last.next
                while True:
                    if temp.next==self.last :
                        temp.next=self.last.next
                        self.last.next=None
                        self.last=temp
                        break
                    temp=temp.next
                    
    def deleteEle(self,data):
        if self.last is not None:       
            if self.last.item==data:
                self.deleteAtLast()
            elif self.last.next.item == data :
                self.deleteAtStart()
            else :
                temp =self.last.next
                while temp!=self.last : 
                    if temp.next.item==data:
                        x=temp.next.next
                        temp.next.next=None
                        temp.next=x
                        break
                    temp=temp.next        
        else :
             print("Empty list")
               
 #Search Element :
    def search(self,data):
        if self.isEmpty() :
            return None
        else :
            temp=self.last.next
            while True:
                if(temp.item==data):
                    return temp
                temp=temp.next
                if temp==self.last.next:
                    break
        return None
        
 #Print element :       
    def printLL(self):
        if self.isEmpty():
            print("List is empty")
        else :
            temp=self.last.next
            while True:
                print(temp.item, end=" ")
                temp=temp.next
                if temp==self.last.next:
                    break
            print()
            
    def isCirculer(self):
        if self.isEmpty():
            return True
        if self.last.next is self.last :
            return True
        else :
            temp=self.last.next
            while(temp is not self.last):
                if(temp.next is self.last and temp.next.next is not None):
                    return True
                temp=temp.next
                    
# Iterator :
    def __iter__(self):
        if self.last== None:
            return CLLIterator(None)
        else:
            return CLLIterator(self.last.next)    
           
# Iterator class :
class CLLIterator:
    def __init__(self,start):
        self.current=start
        self.start=start
    def __iter__(self):
        return self
    def __next__(self):
        if self.current == None :
            raise StopIteration
        data=self.current.item
        self.current=self.current.next
        if self.current != self.start:
            return data
        else: 
            raise StopIteration
 
                
myList=CLL()
print(myList.isEmpty())
myList.insertAtStart(20)
myList.insertAtStart(10)
myList.insertAtLast(30)
myList.insertAtLast(40)
myList.insertAtStart(5)
myList.insertAfter(40,50)
myList.printLL()
# myList.deleteEle(50)
myList.printLL()
# for i in myList:
#     print(i,end=" ")
print(myList.isCirculer())