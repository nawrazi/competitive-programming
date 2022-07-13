# https://leetcode.com/problems/valid-sudoku/

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)
        
        for r in range(9):
            for c in range(9):
                item = board[r][c]
                row = rows[r]
                col = cols[c]
                box = boxes[(r//3, c//3)]
                
                if item not in row and item not in col and item not in box:
                    rows[r].add(item)
                    cols[c].add(item)
                    boxes[(r//3, c//3)].add(item)
                    
                elif item != '.':
                    return False
                
        return True
    
