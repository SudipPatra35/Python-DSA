def prec(c):
    if c == '*' or c == '/':
        return 2
    elif c == '+' or c == '-':
        return 1
    elif c=="^":
        return 3
    else:
        return 0

def InfixToPostfix(exp):
    result = " "
    stack = []
    
    for c in exp:
        # c = exp[i]
        if c.isalnum():
            result+=c
        elif c == '(':
            stack.append(c)
        elif c == ')':
            while stack and stack[-1]!="(":
                result+=stack.pop()
            stack.pop()
        else:
            while stack and prec(c) <= prec(stack[-1]):
                result+=stack.pop()
            stack.append(c)
    
    # Pop remaining operators from stack
    while stack:
        result+=stack.pop()
    
    return result

exp = "a+b*(c^d-e)^(f+g*h)-i"
res = InfixToPostfix(exp)
print(res)
