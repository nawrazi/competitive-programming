# https://leetcode.com/problems/minimum-operations-to-make-array-equal/description/

class Solution:
    def minOperations(self, n: int) -> int:
        last = (2 * n) - 1
        ops = 0
        while last > n:
            ops += last - n
            last -= 2
            
        return ops
    
