def bs(n):
    # li=n.copy()
    l=len(n)
    swap=False
    for i in range(l-1):
        for j in range(1,l-i):
            if (n[j]<n[j-1]):
                n[j],n[j-1]=n[j-1],n[j]
                swap=True
            if swap is False:
                break
            
arr=list(map(int,input().split()))
bs(arr)
print(arr)