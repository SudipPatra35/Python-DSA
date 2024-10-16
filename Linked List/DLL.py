class Node:
    def __init__(self,item=None,prev=None,next=None):
        self.prev=prev
        self.item=item
        self.next=next

class DLL:
    def __init__(self,start=None):
        self.start=start
    
    def isEmpty(self):
        return self.start is None 
    
# Insert Element            
    def insertAtStart(self,data):
        n=Node(data,None,self.start)
        if self.isEmpty() is False:
            self.start.prev = n
        self.start=n
       
    def insertAtlast(self,data):
        n=Node(data,None,None)
        if self.isEmpty() is False :
            temp=self.start
            while temp.next is not None:
                temp=temp.next
            temp.next=n
            n.prev=temp
        else:
            self.start=n
    
    def insertAfter(self,afterwhat,data):
        temp=self.search(afterwhat)
        if temp is not None:
            n=Node(data,temp,temp.next)
            if temp.next is not None :
                temp.next.prev=n
            temp.next=n
  
  # Delete Element 
    def deleteFirst(self):
        if self.start is not None:
            self.start.next.prev=None
            self.start=self.start.next

    def deleteLast(self):
        if self.start is None:
            return
        else :
            if self.start.next is None:
                self.start=None
            else:
                temp=self.start
                while temp.next.next is not None :
                   temp=temp.next
                # print(temp.item)
                temp.next=None
        
        
    def deleteEle(self, data):
     if self.start is not None:
        # Check if the node to delete is the start node
        if self.start.item == data:
            self.start = self.start.next
            if self.start is not None:
                self.start.prev = None
            return
        
        # Traverse the list to find the node with the given data
        temp = self.start
        while temp is not None:
            if temp.item == data:
                # Adjust pointers to remove the node
                if temp.prev is not None:
                    temp.prev.next = temp.next
                if temp.next is not None:
                    temp.next.prev = temp.prev
                return
            temp = temp.next
            
  # Search Element   
    def search(self, data):
        temp = self.start
        while temp is not None:
            if temp.item == data:
                return temp
            temp = temp.next
        return None  
        
    def totalelement(self):
        temp = self.start
        count=0
        while temp is not None:
            count+=1
            temp = temp.next
        return count
    
    def PrintLL(self):
        if self.isEmpty():
            print("List is Empty")
        else:   
            temp=self.start
            while temp is not None:
                print(temp.item,end=" ")
                temp=temp.next
            print()
    def __iter__(self):
        return DLLIterator(self.start)
    
class DLLIterator:
    def __init__(self,start) :
        self.current=start
    def __iter__(self):
        return
    def __next__(self):
        if self.current is None:
            raise StopIteration
        data = self.current.item
        self.current=self.current.next
        return data     
        
myList=DLL()
print(myList.isEmpty())   
myList.insertAtStart(30)
myList.insertAtlast(40)
myList.insertAtStart(50)
myList.insertAtlast(10)
myList.insertAfter(10,60)  
myList.PrintLL()
print(myList.totalelement())
myList.deleteFirst()
# myList.PrintLL()
for i in myList:
    print(i,end=" ")