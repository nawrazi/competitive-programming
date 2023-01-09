# https://leetcode.com/problems/stone-game-iv/description/

class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        @cache
        def canAliceWin(n, alice):
            if n == 0:
                return not alice
            
            if alice:
                val = 1
                while val <= n:
                    if canAliceWin(n - val, False):
                        return True
                    val = pow(sqrt(val) + 1, 2)
                    
                return False
            
            else:
                val = 1
                while val <= n:
                    if not canAliceWin(n - val, True):
                        return False
                    val = pow(sqrt(val) + 1, 2)
                    
                return True
            
        return canAliceWin(n, True)
    
