class Stack:
    def __init__(self):
        self.items = []
        
    def isEmpty(self):
        return len(self.items) == 0
    
    def push(self, data):
        self.items.append(data)
        
    def pop(self):
        if self.isEmpty():
            raise IndexError("Stack is Empty")
        else:
            return self.items.pop()
    
    def peek(self):
        if not self.isEmpty():
            return self.items[-1]
        else:
            raise IndexError("Stack is Empty")
    
    def size(self):
        return len(self.items)

def infix_to_postfix(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    associativity = {'+': 'L', '-': 'L', '*': 'L', '/': 'L', '^': 'R'}
    
    def is_operator(c):
        return c in precedence
    
    def is_operand(c):
        return c.isalnum()
    
    def higher_precedence(op1, op2):
        return precedence[op1] > precedence[op2] or \
               (precedence[op1] == precedence[op2] and associativity[op1] == 'L')
    
    output = []
    stack = Stack()
    
    for char in expression:
        if is_operand(char):
            output.append(char)
        elif is_operator(char):
            while not stack.isEmpty() and is_operator(stack.peek()) and higher_precedence(stack.peek(), char):
                output.append(stack.pop())
            stack.push(char)
        elif char == '(':
            stack.push(char)
        elif char == ')':
            while not stack.isEmpty() and stack.peek() != '(':
                output.append(stack.pop())
            stack.pop()  # pop '(' from stack
    
    while not stack.isEmpty():
        output.append(stack.pop())
    
    return ''.join(output)

# Example usage
expression = "A+B*(C^D-E)"
print("Infix expression:", expression)
postfix = infix_to_postfix(expression)
print("Postfix expression:", postfix)
