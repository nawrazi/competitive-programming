# https://leetcode.com/problems/reordered-power-of-2/

class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        count = Counter(str(n))
        cur = 1
        
        for i in range(30):
            if Counter(str(cur)) == count:
                return True
            cur <<= 1
            
        return False
    
