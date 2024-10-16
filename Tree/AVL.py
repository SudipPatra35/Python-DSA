class Node:
    def __init__(self,data=None,left=None,right=None,height=None):
        self.data=data
        self.left=left
        self.right=right
        self.height=1

class AVL:
    def __init__(self):
        self.root=None
    def getHeight(self,root):
        if not root:
            return 0
        return root.height 
    
    def getBalance(self,root):
        if not root:
            return 0
        return self.getHeight(root.left)-self.getHeight(root.right)
    
    def leftRotation(self,root):
        child=root.right
        childLeft=child.left 
        child.left=root
        root.right=childLeft
        #Update height
        root.height=1+max(self.getHeight(root.left),self.getHeight(root.right))
        child.height=1+max(self.getHeight(child.left),self.getHeight(child.right))
        return child
    def rightRotation(self,root):
        child=root.left
        childRight=child.right
        child.right=root
        root.left=childRight
        #Update height
        root.height=1+max(self.getHeight(root.left),self.getHeight(root.right))
        child.height=1+max(self.getHeight(child.left),self.getHeight(child.right))
        return child
        
    def insert(self,root,data):
      # Dose not exist
        if not root:
            return Node(data)
      # Exist hain:
        if (data<root.data):
            root.left=self.insert(root.left,data)
        elif (data>root.data):
            root.right=self.insert(root.right,data)
        else:
            return root # Duplicate not allowed
        
      # Update Height :
        root.height=1+max(self.getHeight(root.left),self.getHeight(root.right))
      
      # Check balancing :  
        balance=self.getBalance(root)
        # Left Left Case
        if(balance>1 and data<root.left.data):
            return self.rightRotation(root)
        # Right Right Case
        elif(balance<-1 and data>root.right.data):
            return self.leftRotation(root)
        # Left Right Case
        elif(balance>1 and data>root.left.data):
            root.left=self.leftRotation(root.left)
            return self.rightRotation(root)
        # Right Left Case
        elif(balance<-1 and data<root.right.data):
            root.right=self.rightRotation(root.right)
            return self.leftRotation(root)
        # No Unbalance
        else:
            return root
    
    def delete(self,root,data):
        if root is None:
            return None
        if (data<root.data):
            root.left=self.delete(root.left,data)
        elif (data>root.data):
            root.right=self.delete(root.right,data)
        else:
        #Leaf Node :
            if (root.left is None and root.right is None):
                return None
        #Single Child Exist:
            elif(root.left and not root.right): #Left child
                temp=root.left
                del root
                return temp
            elif(not root.left and root.right): #Right child
                temp=root.right
                del root
                return temp
        # Both Child Exist :
            else:
                #Right side smallest element :
                curr=root.right
                while(curr.left):
                    curr=curr.left
                root.data=curr.data
                root.right=self.delete(root.right,curr.data)
                
        # Update Height :
            root.height=1+max(self.getHeight(root.left),self.getHeight(root.right))
            balance=self.getBalance(root)
            # Left Side Unbalance :
            if balance>1:
                #LL 
                if (self.getBalance(root.left)>=0):
                    return self.rightRotation(root)
                #LR
                if (self.getBalance(root.left) < 0):
                    root.left=self.leftRotation(root.left)
                    return self.rightRotation(root)
            # Right Side Unbalace
            elif balance<-1:
                #RR
                if (self.getBalance(root.right) <= 0):
                    return self.leftRotation(root)
                #RL
                elif(self.getBalance(root.right)>0):
                    root.right=self.rightRotation(root.right)
                    return self.leftRotation(root)
            # Balance hain
    
            return root
                
            
    def preorder(self,root):
        if root is None:
            return
        print(root.data,end=" ")
        self.preorder(root.left)
        self.preorder(root.right)
        
    def inorder(self,root):
        if root is None:
            return
        self.inorder(root.left)
        print(root.data,end=" ")
        self.inorder(root.right)
  
a=AVL()
keys = [10, 20, 30, 50, 70, 5,100,95]

for key in keys:
    a.root = a.insert(a.root, key)
        
a.inorder(a.root)
print()
          