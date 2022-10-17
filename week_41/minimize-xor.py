# https://leetcode.com/problems/minimize-xor/

class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        ones1, ones2 = 0, 0
        bit = 1
        for i in range(31):
            if num1 & bit:
                ones1 += 1
            if num2 & bit:
                ones2 += 1
            bit <<= 1
            
        if ones2 > ones1:
            ans = num1
            bit = 1
            while ones2 > ones1:
                if ans & bit == 0:
                    ans |= bit
                    ones2 -= 1
                bit <<= 1
        else:
            ans = 0
            bit = 1 << 31
            while ones2 > 0:
                if num1 & bit:
                    ans |= bit
                    ones2 -= 1
                bit >>= 1
                
        return ans
    
