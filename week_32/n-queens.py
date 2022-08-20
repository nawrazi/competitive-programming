# https://leetcode.com/problems/n-queens/

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols, pos_diags, neg_diags = set(), set(), set()
        current = [['.' for _ in range(n)] for _ in range(n)]
        arrangements = []
        
        def getArrangements(row):
            if row == n:
                arrangements.append([''.join(row) for row in current])
                
            for col in range(n):
                if col in cols or row + col in pos_diags or row - col in neg_diags:
                    continue
                    
                cols.add(col)
                pos_diags.add(row + col)
                neg_diags.add(row - col)
                current[row][col] = 'Q'
                
                getArrangements(row + 1)
                
                cols.remove(col)
                pos_diags.remove(row + col)
                neg_diags.remove(row - col)
                current[row][col] = '.'
                
        getArrangements(0)
        return arrangements
    
