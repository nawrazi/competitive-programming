# https://leetcode.com/problems/min-stack/submissions/

class MinStack:

    def __init__(self):
        self.stack=[]

    def push(self, val: int) -> None:
        if len(self.stack)==0:
            self.stack.append((val,val))
            return

        if val<self.stack[-1][1]:
            self.stack.append((val,val))

        else:
            self.stack.append((val,self.stack[-1][1]))

    def pop(self) -> None:
        x,y = self.stack.pop()
        return(x)

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
