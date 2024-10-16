li=[5,8,1,6,4,3,2,7,9]
def insertion(li):
    for i in range (0,len(li)-1):
       for j in range (i+1,0,-1):
           if li[j-1]>li[j]: 
               li[j],li[j-1]=li[j-1],li[j]
           elif li[j-1]<li[j]:
               break
    return li

print("Before sorting : ")
print(li)
insertion(li)
print("After sorting : ")
print(li)
