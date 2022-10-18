# https://leetcode.com/problems/spiral-matrix-iii/

class Solution:
    def inBound(self, row, col, height, width):
        return 0 <= row < height and 0 <= col < width
    
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        traversal = []
        length = 1
        direction = [0, 1]
        
        while len(traversal) < rows * cols:
            for _ in range(2):
                for i in range(length):
                    if self.inBound(rStart, cStart, rows, cols):
                        traversal.append([rStart, cStart])
                    rStart += direction[0]
                    cStart += direction[1]
                direction.reverse()
                direction[1] *= -1
            length += 1
            
        return traversal
    
