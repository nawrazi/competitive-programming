# https://leetcode.com/problems/fibonacci-number/

class Solution:
    def __init__(self):
        self.mem = {}

    def fib(self, n: int) -> int:
        if n==1 or n==0:
            return n

        cur_sum = 0
        for move in [n-1, n-2]:
            if move in self.mem:
                move_result = self.mem[move]
            else:
                move_result = self.fib(move)
                self.mem[move] = move_result

            cur_sum += move_result

        return cur_sum
