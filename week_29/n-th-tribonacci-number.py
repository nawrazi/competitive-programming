# https://leetcode.com/problems/n-th-tribonacci-number/

class Solution:
    def __init__(self):
        self.cache = {}
    
    def tribonacci(self, n: int) -> int:
        if n <= 2:
            return 1 if n else 0

        if n - 1 not in self.cache:
            self.cache[n-1] = self.tribonacci(n-1)
        if n - 2 not in self.cache:
            self.cache[n-2] = self.tribonacci(n-2)
        if n - 3 not in self.cache:
            self.cache[n-3] = self.tribonacci(n-3)

        return self.cache[n-1] + self.cache[n-2] + self.cache[n-3]
    
