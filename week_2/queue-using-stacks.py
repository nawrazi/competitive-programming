# https://leetcode.com/problems/implement-queue-using-stacks/

class MyQueue:

    def __init__(self):
        self.main_stack = []
        self.temp_stack = []

    def push(self, x: int) -> None:
        if len(self.main_stack)==0:
            self.main_stack.append(x)
            return

        while len(self.main_stack)>0:
            self.temp_stack.append(self.main_stack.pop())

        self.temp_stack.append(x)

        while len(self.temp_stack)>0:
            self.main_stack.append(self.temp_stack.pop())

    def pop(self) -> int:
        if len(self.main_stack)==0:
            return

        return self.main_stack.pop()

    def peek(self) -> int:
        val = self.main_stack.pop()
        self.main_stack.append(val)

        return val

    def empty(self) -> bool:
        return len(self.main_stack)==0
