# https://leetcode.com/problems/divisor-game/

class Solution:
    def divisorGame(self, n: int) -> bool:
        @cache
        def canWin(num, alice):
            if num <= 1:
                return num != 0 and not alice
            
            for fac in range(1, ceil(sqrt(num))):
                if num % fac == 0:
                    aliceWins = canWin(num - fac, not alice) or canWin(num - (num // fac), not alice)
                    if (alice and aliceWins) or (not alice and not aliceWins):
                        return alice
                    
            return not alice
        
        return canWin(n, True)
    
