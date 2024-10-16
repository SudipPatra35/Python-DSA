import sys
class Node :
    def __init__(self,data=None,left=None,right=None):
        self.data=data
        self.left=left
        self.right=right
        
class BST:
    def insert(self,root,value):
        # new=input()
        # if new=='':
        #     return None
        # # For int Nodes :
        # n=Node(int(new))
        # # For string Nodes :
        # # n=Node(new)
        # # Left child create
        # print("Enter the left child of "+new+" (press enter to skip) : ",end="")
        # n.left=self.insert()
        # # Right child create
        # print("Enter the right child of "+new+" (press enter to skip) : ",end="")
        # n.right=self.insert()
        # return n
        if root is None:
            temp=Node(value)
            return temp
        if value< root.data:
            root.left=self.insert(root.left,value)
        if value>root.data:
            root.right=self.insert(root.right,value)     
        return root
    
    def search(self,root,target):
        if root is None:
            return False
        if target == root.data:
            return True
        elif target < root.data:
            return self.search(root.left,target)
        else:
            return self.search(root.right,target)
    
    def delete(self,root,target):
        if root is None:
            return None
        if (target<root.data):
            root.left=self.delete(root.left,target)
            return root
        elif (target>root.data):
            root.right=self.delete(root.right,target)
            return root
        else:
        # 1) target is Leaf node:
            if (root.left is None and root.right is None):
                return None
        # 2) has only one child
           # 2.1) has only left child :
            elif (root.right is None):    
                temp= root.left
                root.left=None
                return temp
           # 2.2 ) has only right child :
            elif (root.left is None):    
                temp= root.right
                root.right=None
                return temp
        # 3) Has two child 
            else:
                # Find the greatest element from left
                child=root.left
                parent=root
                while(child.right):
                    parent=child
                    child=child.right
           # 3.1 ) if root!=parent
                if parent!=root:
                    parent.right=child.left
                    child.left=root.left
                    child.right=root.right
                    root.left=None
                    root.right=None
                    return child
            # 3.2 ) if root == parent
                if parent==root:
                    child.right=root.right
                    root.left=None
                    root.right=None
                    return child
   
    def inorder(self,root):
        if root is None:
            return None
        self.li=[]
        self.rInorder(root)
        return self.li
    def rInorder(self,root):
        if root is None:
            return
        self.rInorder(root.left)
        self.li.append(root.data)
        self.rInorder(root.right)        
    
    def isBST(self,root):
        if root is None:
            return None
        li=self.inorder(root)
        for i in range(len(li)-1):
            if li[i]>li[i+1]:
                return False
        return True
    
    def minDistance(self,root):
        if root is None:
            return None
        li=self.inorder(root)
        min=li[1]-li[0]
        for i in range(1,len(li)-1):
            if (li[i+1]-li[i]<min):
                min = li[i+1]-li[i]
        return min
    
    def ksum(self,root,k):
        if root is None:
            return 0
        self.sum=0
        self.k=k
        self.ksumUtil(root)
        return self.sum               
    def ksumUtil(self,root):
        if root is None:
            return 
        self.ksumUtil(root.left)
        if(self.k>0):
            self.sum+=root.data
            self.k-=1
        if self.k<=0:
            return
        self.ksumUtil(root.right)
    
    def kLargest(self,root,k):
        if root is None:
            return None
        self.k=k
        self.ans=None
        self.kLargestUtil(root)
        return self.ans
    def kLargestUtil(self,root):
        if root is None:
            return
        self.kLargestUtil(root.right)
        self.k-=1
        if self.k==0:
            self.ans=root.data
        if self.k<0:
            return
        self.kLargestUtil(root.left)
    
    def ArrToBST(self,arr):
        # if root is None:
        #     return None
        self.li=[]
        self.ArrToBSTUtil(arr,0,len(arr)-1)
        return self.li   
    def ArrToBSTUtil(self,arr,start,end):
        if start>end:
            return
        mid=start+(end-start)//2
        self.li.append(arr[mid])
        self.ArrToBSTUtil(arr,start,mid-1)
        self.ArrToBSTUtil(arr,mid+1,end)
    
    def bstFromPreorder(self,preorder):
        self.index=0
        root=self.bstFromPreorderUtil(preorder,(-sys.maxsize-1),(sys.maxsize))
        return root
    def bstFromPreorderUtil(self,preorder,lower,upper):
        if self.index==len(preorder) or lower>preorder[self.index] or upper<preorder[self.index]:
            return None
        root=Node(preorder[self.index])
        value=preorder[self.index]
        self.index+=1
        root.left=self.bstFromPreorderUtil(preorder,lower,value)
        root.right=self.bstFromPreorderUtil(preorder,value,upper)
        return root
    
    def bstFromPostorder(self,postorder):
        self.index=len(postorder)-1
        root=self.bstFromPostorderUtil(postorder,(-sys.maxsize-1),(sys.maxsize))
        return root
    def bstFromPostorderUtil(self,postorder,lower,upper):
        if self.index<0 or lower>postorder[self.index] or upper<postorder[self.index]:
            return None
        value=postorder[self.index]
        root=Node(value)
        self.index-=1
        root.right=self.bstFromPostorderUtil(postorder,value,upper)
        root.left=self.bstFromPostorderUtil(postorder,lower,value)
        return root

    def LCA(self,root,a,b):
        if root is None:
            return None
        if a<root.data and b<root.data:
            return self.LCA(root.left,a,b)
        elif a>root.data and b>root.data:
            return self.LCA(root.right,a,b)
        else:
            return root
    
    def printGivenRange(self,root,a,b):
        if root is None:
            return
        if root.data>a and root.data>b:
            self.printGivenRange(root.left,a,b)
        elif root.data<a and root.data<b:
            self.printGivenRange(root.right,a,b)
        else:
            self.printGivenRange(root.left,a,b)
            print(root.data,end=" ")
            self.printGivenRange(root.right,a,b)

    def merge2BST(self,root1,root2):
        ans1=self.inorder(root1)
        ans2=self.inorder(root2)
        ans=[]
        i=0
        j=0
        while(i<len(ans1) and j<len(ans2)):
            if (ans1[i]<ans2[j]):
                ans.append(ans1[i])
                i+=1
            else:
                ans.append(ans2[j])
                j+=1
        ans.extend(ans1[i:])
        ans.extend(ans2[j:])
        return ans


    
b=BST()
# print("Enter the root node of 1st tree : ",end="")
# root=b.insert()
li1=[10,5,15,4,7,14,18,6,9]
root1=None
for i in li1:
    root1=b.insert(root1,i)
li2=[7,4,8,2,5,9]
root2=None
for i in li2:
    root2=b.insert(root2,i)

print("Inorder of 1st tree : ",b.inorder(root1))
print("Inorder of 2nd tree : ",b.inorder(root2))

ans=b.merge2BST(root1,root2)
print("Merged tree : ",ans)
# x=int(input("Enter the 1st node :"))
# y=int(input("Enter the 2nd node :"))
# ans=b.LCA(root,x,y)
# print("LCA is :",ans.data)

# b.printGivenRange(root,x,y)
# print()
     
# root=b.bstFromPreorder(l)
# ans=b.inorder(root)
# print(ans)

# postorder=[1,7,5,50,40,10]
# root=b.bstFromPostorder(postorder)
# ans=b.inorder(root)
# print(ans)

# b.delete(root,7)
# print("After delete :",end=" ")
   

# ans=b.search(root,5)
# print(ans)

# print("is BST ? :",b.isBST(root))
# print("Minimum distance :", b.minDistance(root))

# sum=b.ksum(root,3)
# print("Ksum is :",sum)

# kLargest=b.kLargest(root,1)
# print("KLargest is :",kLargest)

# arr=[1,2,3,4,5,6]
# ans=b.ArrToBST(arr)


# print(ans)
