# Print N natural Numbers
def printNum(n):
    if n==0 :
        return
    printNum(n-1)
    print(n)
# printNum(10)

#Print N odd natural Numbers :
def printOddNum(n):
    if n<=0:
        return
    printOddNum(n-1)
    print(2*n-1,end=' ')
# printOddNum(10)

#Print N even natural Numbers :
def printEvenNum(n):
    if n<=0:
        return
    printEvenNum(n-1)
    print(2*n,end=' ')
printEvenNum(10)    
