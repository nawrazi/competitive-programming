# https://leetcode.com/problems/simplified-fractions/submissions/

class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        fractions = []
        
        for denom in range(2, n + 1):
            for numer in range(denom):
                if gcd(numer, denom) == 1:
                    fractions.append(f'{numer}/{denom}')
                    
        return fractions
    
