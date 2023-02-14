# https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/

class Solution:
    def sumZero(self, n: int) -> List[int]:
        result = []
        
        for i in range((n // 2)):
            result.append(-(i + 1))
            result.append(i + 1)
            
        if n % 2 != 0:
            result.append(0)
            
        return result
    
