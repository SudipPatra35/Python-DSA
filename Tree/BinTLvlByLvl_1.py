class Node:
    def __init__(self,data=None,left=None,right=None):
        self.data=data
        self.left=left
        self.right=right
class queue:
    def __init__(self):
        self.item=[]
    def isEmpty(self):
        return len(self.item)==0
    def push(self,data):
        self.item.append(data)
    def pop(self):
        if not self.isEmpty():
            return self.item.pop(0)
    def front(self):
        if not self.isEmpty():
            return self.item[0]
    
    
class BinTree:
    def __init__(self):
        n=input("Enter the root node : ")
        self.root=Node(n)
        self.q=queue()
        self.q.push(self.root)
        
    def insert(self):
        while not self.q.isEmpty():
        #left node :
            temp=self.q.pop()
            
            left=input("Enter the left child of "+temp.data+" (-1 for no child): ")
            if(left != '-1'):
                ln=Node(left)
                self.q.push(ln)
                temp.left=ln
            right=input("Enter the right child of "+temp.data+" (-1 for no child): ")
            if(right!='-1'):
                rn=Node(right)
                self.q.push(rn)
                temp.right=rn        

bt=BinTree()
bt.insert()        
        
    
        