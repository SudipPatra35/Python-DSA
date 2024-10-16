def quicksort(li,s,e):
    if s>=e:
        return
    p=partition(li,s,e)
    quicksort(li,s,p-1)
    quicksort(li,p+1,e)
    
    
def partition(li,s,e):
    pivot=li[s]
    count=0
    for i in range(s+1,e+1,1):
        if li[i]<pivot:
            count+=1
    pivotIndex=s+count
    li[s],li[pivotIndex]=li[pivotIndex],li[s]
    i=s
    j=e
    while(i<pivotIndex and j>pivotIndex):
        while(li[i]<li[pivotIndex]):
            i+=1
        while (li[j]>li[pivotIndex]):
            j-=1
        if(i<pivotIndex and j>pivotIndex):
            li[i],li[j]=li[j],li[i]
            i+=1
            j-=1
    
    return pivotIndex
    
    
li=[2,8,4,1,9,7,6]
print("Before Sorting : ",li)
quicksort(li,0,len(li)-1)
print("After Sorting : ",li)