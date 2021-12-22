# https://leetcode.com/problems/design-circular-deque/submissions/

class MyCircularDeque:

    def __init__(self, k: int):
        self.k = k
        self.deque = []

    def insertFront(self, value: int) -> bool:
        if len(self.deque)==self.k:
            return False

        self.deque.insert(0,value)
        return True

    def insertLast(self, value: int) -> bool:
        if len(self.deque)==self.k:
            return False

        self.deque.append(value)
        return True

    def deleteFront(self) -> bool:
        if not self.deque:
            return False

        self.deque.pop(0)
        return True

    def deleteLast(self) -> bool:
        if not self.deque:
            return False

        self.deque.pop()
        return True

    def getFront(self) -> int:
        return self.deque[0] if self.deque else -1

    def getRear(self) -> int:
        return self.deque[-1] if self.deque else -1

    def isEmpty(self) -> bool:
        return not self.deque

    def isFull(self) -> bool:
        return len(self.deque) == self.k
