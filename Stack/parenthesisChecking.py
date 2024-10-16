from stack_list import *
class parenthesisChecker:
    def __init__(self):
        self.s=stack()
        
    def isClosing(self,open,close):
        return (open=='(' and close==')') or (open=='{' and close=='}') or (open=='[' and close==']')
    
    def isMatching(self,str):
        for i in str:
            if i in "({[":
                self.s.push(i)
            elif i in ")}]":
                if self.s.isEmpty():
                    return False
                elif self.isClosing(self.s.peek(),i):
                    self.s.pop()
                    # return True
                else :
                    return False
        return self.s.isEmpty()
                
str="[{(a+b)+(c+d)}]"
p=parenthesisChecker()
print("Is it Balanced Parenthesis ? ")
print(p.isMatching(str))

