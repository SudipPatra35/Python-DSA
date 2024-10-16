from collections import deque
class Node :
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
    def size(self):
        return len(self.item)
    
class stack:
    def __init__(self):
        self.item=[]
    def isEmpty(self):
        return len(self.item)==0
    def push(self,data):
        self.item.append(data)
    def pop(self):
        if not self.isEmpty():
            return self.item.pop(-1)
    def front(self):
        if not self.isEmpty():
            return self.item[-1]    

class QueueNode:
    def __init__(self,node,hd):
        self.node=node
        self.hd=hd      
class BinTree:
       
    def Totalsize(self,root):
        if root is None:
            return 0
        return 1+ self.Totalsize(root.left)+self.Totalsize(root.right)
        
    def insert(self):
        new=input()
        if new=='':
            return None
        # For int Nodes :
        n=Node(int(new))
        # For string Nodes :
        # n=Node(new)
        # Left child create
        print("Enter the left child of "+new+" (press enter to skip) : ",end="")
        n.left=self.insert()
        # Right child create
        print("Enter the right child of "+new+" (press enter to skip) : ",end="")
        n.right=self.insert()
        return n
    
    def preorder(self,root): # N-L-R
        # if (root is None):
        #     return
        # # print
        # print(root.data,end=" ")
        # #left
        # self.preorder(root.left)
        # #right
        # self.preorder(root.right)
        # # Without Recursion
        s=stack()
        s.push(root)
        while(not s.isEmpty()):
            temp=s.pop()
            print(temp.data,end=" ")
            if temp.right:
                s.push(temp.right)
            if temp.left:
                s.push(temp.left)
                 
    def postorder(self,root): # N-L-R
        # if (root is None):
        #     return
        # #left
        # self.postorder(root.left)
        # #right
        # self.postorder(root.right)
        # # print
        # print(root.data,end=" ")
        
        # #  Without Recursion
        s=stack()
        ans=stack()
        s.push(root)
        # li=[]
        while(not s.isEmpty()):
            temp=s.pop()
            ans.push(temp.data)
            if temp.left:
                s.push(temp.left)
            if temp.right:
                s.push(temp.right)
        while(not ans.isEmpty()):
            print(ans.pop(),end=" ") 
               
    def inorder(self,root): # N-L-R
        # if (root is None):
        #     return
        # #left
        # self.inorder(root.left)
        # # print
        # print(root.data,end=" ")
        # #right
        # self.inorder(root.right)
        
        # # Without Recursion :
        s=stack()
        temp=root
        while(True):
            if(temp is not None):
                s.push(temp)
                temp=temp.left
            else:
                if(s.isEmpty()):
                    break
                temp=s.pop()
                print(temp.data,end=" ")
                temp=temp.right
                  
    def levelorder(self,root):
        if root is None:
            return
        self.q=queue()
        self.q.push(root)
        while not self.q.isEmpty() :
            node=self.q.pop()
            print(node.data,end=" ") 
            if node.left is not None :
                self.q.push(node.left)
            if node.right is not None :
                self.q.push(node.right)
    
    def SumOfNodes(self,root):
        if root is None:
            return 0
        return root.data+ self.SumOfNodes(root.left)+ self.SumOfNodes(root.right)
     
    def countLeaves(self,root):
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        return self.countLeaves(root.left)+ self.countLeaves(root.right)
    
    def nonLeaves(self,root):
        if root is None:
            return 0
        if root.left is None or root.right is None :
            return 0
        return 1+self.nonLeaves(root.left)+self.nonLeaves(root.right)
    
    def height(self, root):
        if root is None:
            return 0
        return 1 + max(self.height(root.left), self.height(root.right))
    def diameter(self,root):
        if root is None:
            return 0,0
        lh,ld=self.diameter(root.left)
        rh,rd=self.diameter(root.right)
        height=1+max(lh,rh)
        dia=max(ld,rd,1+lh+rh)
        return height, dia
    
    def isBalance(self,root):
        if root is None:
            return False
        return self.checkBalance(root) !=-1
    def checkBalance(self,root):
        if root is None:
            return 0
        l=self.checkBalance(root.left)
        r=self.checkBalance(root.right)
        if abs(l-r) > 1:
            return -1
        return 1 + max(l,r)
    
    def spiralTravesal(self,root):
        s1=stack()
        s2=stack()
        li=[]
        if root is None:
            return
        s1.push(root)
        while(not s1.isEmpty() or not s2.isEmpty()):
           if not s1.isEmpty(): 
              while(not s1.isEmpty()):
                n=s1.pop()
                li.append(n.data)
                if n.right:
                    s2.push(n.right)
                if n.left:
                    s2.push(n.left)
           else:
               while(not s2.isEmpty()):
                n=s2.pop()
                li.append(n.data)
                if n.left:
                    s1.push(n.left)
                if n.right:
                    s1.push(n.right)
        return li
               
    def identical(self,root1,root2):
        if root1 is None and root2 is None: 
            return True
        if (root1 and not root2 ) or (not root1 and root2):
            return False
        if (root1.data!=root2.data):
            return False
        return self.identical(root1.left,root2.left) and self.identical(root1.right,root2.right)
     
    def mirror(self,root):
        if root is None:
            return
        temp=root.left
        root.left=root.right
        root.right=temp
        self.mirror(root.left)   
        self.mirror(root.right)   
    
    def parent(self,root,a,b):
        if root is None:
            return False
        if (root.left and root.right):
            if (root.left.data==a and root.right.data==b):
                return True
            if (root.left.data==b and root.right.data==a):
                return True
            
        return self.parent(root.left,a,b) or self.parent(root.right,a,b)
    
    def isCousins(self,root,a,b):
        q=queue()
        q.push(root)
        l1=-1
        l2=-1
        level=0
        while(not q.isEmpty()):
            n=q.size()
            while (n>0):
                n-=1
                temp=q.pop()
                if(temp.data==a):
                    l1=level
                if(temp.data==b):
                    l2=level
                if (temp.left):
                    q.push(temp.left)
                if temp.right:
                    q.push(temp.right)
            level+=1
            if(l1!=l2): # Jekono aktar peye gechi, ar level are different 
                return False
            if (l1!=-1 and l2!=-1): # dujon er ei peye gechi but same noy
                 break
        return not self.parent(root,a,b)
      
    def leftView(self,root):
        li=[]
        self.leftViewCall(root,0,li)
        return li
        # q=queue()
        # q.push(root)
        # while(not q.isEmpty()):
        #     li.append(q.front().data)
        #     n=q.size()
        #     while (n>0):
        #         n-=1
        #         temp=q.pop()
        #         if(temp.left):
        #             q.push(temp.left)
        #         if (temp.right):
        #             q.push(temp.right)       
        # return li        
    
    def leftViewCall(self,root,level,li):
        if root is None:
            return 
        if level==len(li):
            li.append(root.data)
        self.leftViewCall(root.left,level+1,li)                
        self.leftViewCall(root.right,level+1,li)                
    
    def rightView(self,root):
        li=[]
        self.rightViewCall(root,0,li)
        return li    
    def rightViewCall(self,root,level,li):
        if root is None:
            return 
        if level==len(li):
            li.append(root.data)
        self.rightViewCall(root.right,level+1,li)
        self.rightViewCall(root.left,level+1,li)

    def topView(self,root):
        q=queue()
        tview={}
        q.push(QueueNode(root,0))
        while(not q.isEmpty()):
            temp=q.pop()
            hd=temp.hd
            node=temp.node
            if (hd not in tview):
                tview[hd]=node.data
            if node.left is not None:
                q.push(QueueNode(node.left,hd-1))
            if node.right is not None:
                q.push(QueueNode(node.right,hd+1))
            
        for key in sorted(tview):
            print(tview[key],end=" ")
    def bottomView(self,root):
        q=queue()
        bview={}
        q.push(QueueNode(root,0))
        while(not q.isEmpty()):
            temp=q.pop()
            hd=temp.hd
            node=temp.node
            bview[hd]=node.data
            if node.left is not None:
                q.push(QueueNode(node.left,hd-1))
            if node.right is not None:
                q.push(QueueNode(node.right,hd+1))
            
        for key in sorted(bview):
            print(bview[key],end=" ")    
    
    def toDLLUtil(self,root):
        if root is None:
            return None
        self.toDLLUtil(root.left)
        if self.prev is None :
            self.head=root
        else:
            root.left=self.prev
            self.prev.right=root
        self.prev=root
        self.toDLLUtil(root.right)
    def toDLL(self,root):
        self.head=None
        self.prev=None
        self.toDLLUtil(root)
        return self.head
    def printDLL(self,head):
        while head:
            print(head.data,end=" ")
            head=head.right
        print()
    
    def lca(self,root,a,b):
        if (root is None):
            return None
        if (root.data==a or root.data==b):
            return root
        left=self.lca(root.left,a,b)
        right=self.lca(root.right,a,b)
        if left is None:
            return right
        if right is None:
            return left
        return root
    
    def burn(self,root,timer,target):
        if root is None:
            return 0
        if root.data == target:
            return -1
        left=self.burn(root.left,timer,target)
        right=self.burn(root.right,timer,target)
        if left<0:
            timer=max(timer,abs(left)+right)
            return left-1
        if right<0:
            timer=max(timer,left+abs(right))
            return right-1
        return 1+max(left,right)
    def minTime(self,root,target):
        timer=self.burn(root,0,target)
        # Target node er nicher node gulor jonno height ber korte hobe
        bNode=self.find(root,target)
        height=self.height(bNode)-1
        return max(timer,height)
    def find(self,root,target):
        if root is None:
            return None
        if root.data == target:
            return root
        self.find(root.left,target)
        self.find(root.right,target)
        
                        
bt1=BinTree()
bt2=BinTree()
print("Enter the root node of 1st tree : ",end="")
root1=bt1.insert()
# print("Enter the root node of 2nd tree: ",end="")
# root2=bt1.insert()
# print(root.data)
# print("First tree is : ",end="")

# bt1.topView(root1)
# bt1.bottomView(root1)

# head=bt1.toDLL(root1)
# bt1.printDLL(head)

# _,dia=bt1.diameter(root1)
# print("Diameter is :",dia)

# a=int(input("Enter 1st element : "))
# b=int(input("Enter 2nd element : "))
# lca=bt1.lca(root1,a,b)
# print("LCA is :",lca.data)

# bt1.mirror(root1)
# print("Second tree is : ",end="")
# bt1.preorder(root1)
print()

# print("Left view is : ",bt1.leftView(root1))
# print("Right view is : ",bt1.rightView(root1))


# a=int(input("Enter 1st element to find cousin : "))
# b=int(input("Enter 2nd element to find cousin : "))
# print("Is Cousins ? :",bt1.isCousins(root1,a,b))

# print("Spiral Traversal :",bt1.spiralTravesal(root1))

# isBal=bt1.isBalance(root1)
# print("Is balance ? :",isBal)

# res=bt1.identical(root1,root2)
# print("Is identical ? :",res)

# sum=bt.SumOfNodes(root)
# print("Sum of nodes is :",sum)

# leaves=bt.countLeaves(root)
# print("Total of Leaves is :",leaves)

# nonleaves=bt.nonLeaves(root)
# print("Total of Non Leaves is :",nonleaves)

# print("Size of tree is :",bt.Totalsize(root))

# h=bt.height(root)
# print("Height is :",h)


def burnTreeGFG():
    # Burn a Binary tree

# class Solution:
#     def maxDepth(self, n):
#         # finding the most distant leaf node from given node
#         if n is None:
#             return 0
#         return 1 + max(( self.maxDepth(n.left) , self.maxDepth(n.right) ))
    
#     def traverse(self,n,target):
#         if n is None:
#             # base case
#             return (0,0)
        
#         if n.data==target:
#             # target found, hence returning distance from it
#             ans = self.maxDepth(n.right)
#             ans = max( ans, self.maxDepth(n.left) )
#             return (ans,1)
        
#         # this func return 2 integers
#         # ans represents a possible answer
#         # dist represents distance from target node if it was found in subtree
        
#         ans, dist = self.traverse(n.left, target)
#         if dist:
#             # dist != 0 means target was found at distance = dist
#             ans = max( ans, dist+self.maxDepth(n.right) )
#             # finding max Depth on right as target was on left
#             return (ans,dist+1)
        
#         ans, dist = self.traverse(n.right, target)
#         if dist:
#             ans = max( ans, dist+self.maxDepth(n.left) )
#             # finding max Depth on left as target was on right
#             return (ans,dist+1)
        
#         return (0,0)
    
#     def minTime(self,root,target):
#         return ( self.traverse(root,target) )[0]
    pass

