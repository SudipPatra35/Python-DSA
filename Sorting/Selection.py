li=[5,8,1,6,4,3,2,7,9]
def selection(li):
    for i in range (0,len(li)-1):
        min=findMin(li,i)
        li[min],li[i]=li[i],li[min]
    return li

def findMin(li,index):
    min=index
    for j in range (index,len(li)-1):
           if li[j]<li[min]:
                min=j
    return min
              
print("Before sorting : ")
print(li)
selection(li)
print("After sorting : ")
print(li)


# li=[5,8,1,6,4,3,2,7,9]
# def selection(li):
#     for i in range (len(li)-1,0,-1):
#         max=findmax(li,i+1)
#         li[max],li[i]=li[i],li[max]
#     return li

# def findmax(li,last):
#     max=0
#     for j in range (1,last):
#            if li[j]>li[max]:
#                 max=j
#     return max
              
# print("Before sorting : ")
# print(li)
# selection(li)
# print("After sorting : ")
# print(li)