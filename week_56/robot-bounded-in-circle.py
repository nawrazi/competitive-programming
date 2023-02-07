# https://leetcode.com/problems/robot-bounded-in-circle/description/

class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        directions = [(0, 1), (-1, 0), (0, -1), (1, 0)]
        pos, drn = (0, 0), 0
        
        for move in instructions:
            if move == 'L':
                drn = (drn + 1) % 4
            elif move == 'R':
                drn = drn - 1 if drn != 0 else 3
            else:
                pos = (pos[0] + directions[drn][0], pos[1] + directions[drn][1])
                
        return pos == (0, 0) or drn != 0
    
