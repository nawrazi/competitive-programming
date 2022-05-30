# https://leetcode.com/problems/binary-number-with-alternating-bits/

class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        length = floor(log(n, 2)) + 1
        last = 1

        for i in range(length, -1, -1):
            bit = 1 if n & 1 << i else 0
            if bit ^ last:
                last = 1 - last
            else:
                return False
            
        return True
    