li=[5,6,8,9,1,0,4,3,2]
n=int(input("Enter the number to search : "))
temp=None
# for i in range (len(li)):
#     if li[i]==n:
#         print("The index is :",i)
#         temp=1
#         break
if n in li:
    print("Element found.")
    temp=1  
if temp is None:
    print("Element not found")