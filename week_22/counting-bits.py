# https://leetcode.com/problems/counting-bits/

class Solution:
    def countBits(self, n: int) -> List[int]:
        ones = [0 for _ in range(n + 1)]
        power_2 = 1
        
        for i in range(1, n+1):
            if i == power_2 << 1:
                ones[i] = 1
                power_2 <<= 1
            else:
                diff = i - power_2
                ones[i] = 1 + ones[diff]
            
        return ones
    
