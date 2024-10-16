def BinSer(n,ele):
    i=0
    j=len(n[0])-1
    # end=len(n)-1
    while(i<len(n) and j>-1):
        if (n[i][j]==ele):
            return True
        if (ele<n[i][j]):
            j-=1
        else:
            i+=1
    return False
    
    
li=[[1,2,3],[4,5,6],[7,8,9]]
print(BinSer(li,9))