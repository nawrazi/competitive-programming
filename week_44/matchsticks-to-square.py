# https://leetcode.com/problems/matchsticks-to-square/

class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        matchsticks.sort(reverse = True)
        sides = [0, 0, 0, 0]
        perimeter = sum(matchsticks)
        if perimeter % 4 != 0:
            return False
        
        def arrange(idx):
            if idx >= len(matchsticks):
                return len(set(sides)) == 1
            
            for side in range(4):
                sides[side] += matchsticks[idx]
                if sides[side] <= perimeter // 4 and arrange(idx + 1):
                    return True
                sides[side] -= matchsticks[idx]
                if sides[side] == 0:
                    return False
                
        return arrange(0)
    
