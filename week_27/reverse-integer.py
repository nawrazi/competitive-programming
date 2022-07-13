# https://leetcode.com/problems/reverse-integer/

class Solution:
    def reverse(self, x: int) -> int:
        sign = 1
        if x < 0:
            sign = -1
            x *= -1
            
        digits = []
        while x > 0:
            digits.append(x % 10)
            x //= 10
        
        size = len(digits)
        ans = 0
        for i, num in enumerate(digits):
            ans += num * (10 ** (size - i - 1))
        
        if ans > (2 ** 31) - 1:
            return 0
        
        return ans * sign
    
