li=[5,8,1,6,4,3,2,7,9]
def bubble(li):
    swap=False
    for i in range (0,len(li)-1):
       for j in range (1,len(li)-i):
           if li[j]<li[j-1]:
               li[j],li[j-1]=li[j-1],li[j]
               swap=True
       if swap is False:
            break
    return li

print("Before sorting : ")
print(li)
bubble(li)
print("After sorting : ")
print(li)