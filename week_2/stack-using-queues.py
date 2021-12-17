# https://leetcode.com/problems/implement-stack-using-queues/

class MyStack:

    def __init__(self):
        self.main_queue = []
        self.temp_queue = []

    def push(self, x: int) -> None:
        if len(self.main_queue)==0:
            self.main_queue.append(x)
            return

        while len(self.main_queue)>0:
            self.temp_queue.append(self.main_queue.pop(0))

        self.main_queue.append(x)

        while len(self.temp_queue)>0:
            self.main_queue.append(self.temp_queue.pop(0))

    def pop(self) -> int:
        print(self.main_queue, 'pop')
        if len(self.main_queue)==0:
            return

        return self.main_queue.pop(0)

    def top(self) -> int:
        print(self.main_queue)
        if len(self.main_queue)==0:
            return

        val = self.main_queue.pop(0)
        self.main_queue.insert(0,val)

        print(self.main_queue)
        return val

    def empty(self) -> bool:
        return len(self.main_queue)==0
