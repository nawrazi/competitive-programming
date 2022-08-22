# https://leetcode.com/problems/sudoku-solver/

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)
        empties = []
        for r, row in enumerate(board):
            for c, cell in enumerate(row):
                if cell == '.':
                    empties.append((r, c))
                else:
                    rows[r].add(cell)
                    cols[c].add(cell)
                    boxes[(r//3, c//3)].add(cell)
                    
        def backtrack(idx):
            if idx >= len(empties):
                return True
            
            row, col = empties[idx]
            
            for i in range(9):
                num = str(i + 1)
                if num in rows[row] | cols[col] | boxes[(row//3, col//3)]:
                    continue
                
                board[row][col] = num
                rows[row].add(num)
                cols[col].add(num)
                boxes[(row//3, col//3)].add(num)
                
                if backtrack(idx + 1):
                    return True
                
                board[row][col] = '.'
                rows[row].remove(num)
                cols[col].remove(num)
                boxes[(row//3, col//3)].remove(num)
                
        backtrack(0)
        
