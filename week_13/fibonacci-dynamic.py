# https://leetcode.com/problems/fibonacci-number/

class Solution:
    def __init__(self):
        self.mem = {}

    def fib(self, n: int) -> int:
        if n==1 or n==0:
            return n

        if n-1 in self.mem:
            one_back = self.mem[n-1]
        else:
            one_back = self.fib(n-1)
            self.mem[n-1] = one_back

        if n-2 in self.mem:
            two_back = self.mem[n-2]
        else:
            two_back = self.fib(n-2)
            self.mem[n-2] = two_back

        return one_back + two_back
