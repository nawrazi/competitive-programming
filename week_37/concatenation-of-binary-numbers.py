# https://leetcode.com/problems/concatenation-of-consecutive-binary-numbers/

class Solution:
    def concatenatedBinary(self, n: int) -> int:
        mod = (10 ** 9) + 7
        num = ''
        for i in range(1, n + 1):
            num += format(i, 'b')
            
        return int(num, 2) % mod
    
