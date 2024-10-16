# Sum of N natural number
def SumOfN(n):
    if n<=0:
        return 0
    return n+SumOfN(n-1)
# print(SumOfN(10))

# Sum of Odd N natural number
def SumOfOddN(n):
    if n<=0:
        return 0
    return 2*n-1+SumOfOddN(n-1)

# Sum of Even N natural number
def SumOfEvenN(n):
    if n<=0:
        return 0
    return 2*n+SumOfEvenN(n-1)

# Factorial N natural number
def fact(n):
    if n==0:
        return 1
    elif n==1 :
        return 1
    return n*fact(n-1)

# Sum of Square N natural number
def SumOfSqN(n):
    if n<=0:
        return 0
    return n*n+SumOfSqN(n-1)


print(SumOfSqN(10))