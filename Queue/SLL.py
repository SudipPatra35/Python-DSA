# singly linked list 
class Node:
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next
        
class SLL:
    def __init__(self, start=None,tail=None):
        self.start = start
        self.tail=tail
        
    def isEmpty(self):
        return self.start is None
    
# Insert Element
    def insertAtStart(self, data):
        new = Node(data, self.start)
        self.start = new
        
    def insertAtLast(self, data):
        new = Node(data)
        if not self.isEmpty():
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            temp.next = new
        else:
            self.start = new   
    def insertAfter(self,temp,data):
        if temp != None :
            new = Node(data,temp.next)
            temp.next=new
    
    def insertBefore(self,before,data):
        if before != None :
            if self.start.item == before:
                self.insertAtStart(data)
            else:
                temp=self.start
                new = Node(data)
                while temp.next.item!=before :
                    temp=temp.next
                new.next=temp.next
                temp.next=new  
        
# Search Element
    def search(self,data):
        temp =self.start
        while temp.next != None :
            if(temp.item==data):
                return temp
            temp =temp.next
        return None
    
            
# Print Element
    def printLL(self):
        if self.isEmpty():
            print("List is empty")
        else:
            temp = self.start
            while temp is not None:
                print(temp.item, end=" ")
                temp = temp.next
            print()
            
# Delete Element 
    def deleteAtFirst(self):
        if self.start is None:
            print("List is empty ")
            return
        else :
            temp=self.start
            self.start=temp.next
    def deleteAtLast(self): 
        if self.start is None:
            print("List is empty ")
            return
        elif(self.start.next==None):
            self.start=None
        else:
            temp=self.start;
            while temp.next.next !=None :
                temp=temp.next
            temp.next=None
            # print(temp.item)
    def deleteEle(self,data):
        if self.start is None:
            print("List is empty ")
            return
        elif(self.start.next==None):
            if(self.start.item==data):
                self.start=None
        else :
            temp=self.start 
            if(self.start.item==data):
                self.start=self.start.next
            else :
                while(temp.next!=None):
                    if(temp.next.item==data) :
                        temp.next=temp.next.next
                        return
                    temp=temp.next
   #to make SLL iterator
    def __iter__(self):
        return SLLIterator(self.start)               
# Make SLL itarable :                    
class SLLIterator :
#Must written functions :  __init__(self,start) , __iter__(self) 
    def __init__(self,start):
        self.current = start  # current is as temp variable use to point the current node;
    def __iter__(self):
        return self
    def __next__(self):  #next method will call itself         
        if self.current==None:
            raise StopIteration
        data = self.current.item
        self.current=self.current.next
        return data
# Implementation 
# myList = SLL()
# # myList.insertAtStart(20)
# myList.insertAtLast(20)
# myList.insertAtLast(30)
# myList.insertAtStart(10)
# myList.insertAfter(myList.search(20),25)
# myList.printLL()
# myList.insertBefore(10,45)
# myList.printLL()
# # myList.deleteAtFirst()
# # myList.deleteAtLast()
# # myList.deleteEle(30)
# # myList.printLL()
# for i in myList:
#     print(i ,end=" ")
