# https://leetcode.com/problems/where-will-the-ball-fall/

class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        balls = [i for i in range(len(grid[0]))]
        
        for row in range(len(grid)):
            for col, ball in enumerate(balls):
                if ball == -1:
                    continue
                    
                if grid[row][ball] == 1:
                    if ball == len(grid[row]) - 1 or grid[row][ball + 1] == -1:
                        balls[col] = -1
                    else:
                        balls[col] = ball + 1
                        
                elif grid[row][ball] == -1:
                    if ball == 0 or grid[row][ball - 1] == 1:
                        balls[col] = -1
                    else:
                        balls[col] = ball - 1
                        
        return balls
    
