# https://binarysearch.com/problems/Minimum-Stack/

class MinimumStack:
    def __init__(self):
        self.stack = []
        
    def append(self, val):
        top = self.stack[-1][1] if self.stack else float('inf')
        self.stack.append([val, min(val, top)])

    def peek(self):
        return self.stack[-1][0]
    
    def min(self):
        return self.stack[-1][1]
    
    def pop(self):
        return self.stack.pop()[0]
    
