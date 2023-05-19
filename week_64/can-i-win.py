# https://leetcode.com/problems/can-i-win/description/

class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        @cache
        def canWin(turn1, chosen, total):
            if total >= desiredTotal:
                return not turn1
            
            if turn1:
                for num in range(maxChoosableInteger, 0, -1):
                    if chosen & (1 << num) == 0 and canWin(0, chosen | (1 << num), total + num):
                        return True
                return False
            else:
                for num in range(maxChoosableInteger, 0, -1):
                    if chosen & (1 << num) == 0 and not canWin(1, chosen | (1 << num), total + num):
                        return False
                return True
            
        if (maxChoosableInteger * (maxChoosableInteger + 1)) // 2 < desiredTotal:
            return False
        
        return desiredTotal == 0 or canWin(1, 0, 0)
    
