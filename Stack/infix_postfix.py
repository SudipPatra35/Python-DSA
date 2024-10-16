
def precedence(operator):
    if operator=="+" or operator=="-":
        return 1
    if operator=="*" or operator=="/":
        return 2
    if operator=="^":
        return 3
    else:
        return 0
    
def infix_postfix(expression):
    output=" "
    stack=[]

    for symbol in expression:
        if symbol.isalnum():
            output+=symbol
        elif symbol=="(":
            stack.append(symbol)
        elif symbol==")":
            while stack and stack[-1]!="(":
                output+=stack.pop()
            #pop the left paranthesis
            stack.pop()
        else:
            while stack and precedence(stack[-1])>=precedence(symbol):
                output+=stack.pop()
            
            stack.append(symbol)

    while stack:
        output+=stack.pop() 

    return output
    
if __name__=="__main__":
    expression=input("Enter the expression: ")
    ans=infix_postfix(expression)
    print(ans)

