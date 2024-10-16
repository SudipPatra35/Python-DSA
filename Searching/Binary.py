def binarySearch(li,target):
     beg=0
     end=len(li)-1
     while(beg<=end):
         mid=beg+(end-beg)//2
         if li[mid]==target:
             return mid
         elif target<li[mid]:
             end=mid-1
         else:
             beg=mid+1
     return None
         
li=[1,2,3,4,5,6,7,8,9]
n=int(input("Enter the element to search : "))
pos=binarySearch(li,n)
print("Index of pos is :",pos)
