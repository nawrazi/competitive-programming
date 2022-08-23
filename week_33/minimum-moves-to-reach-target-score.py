# https://leetcode.com/problems/minimum-moves-to-reach-target-score/

class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        moves = 0
        while target > 0:
            if maxDoubles > 0 and target % 2 == 0:
                target //= 2
                maxDoubles -= 1
            elif maxDoubles == 0:
                moves += target
                break
            else:
                target -= 1
            moves += 1
            
        return moves - 1
    
