# https://leetcode.com/problems/bitwise-and-of-numbers-range/

class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        result = 0
        bit = 1
        for _ in range(32):
            if left & bit and right & bit and right - left <= bit:
                result |= bit
            bit <<= 1
            
        return result
    
