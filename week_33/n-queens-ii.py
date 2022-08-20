# https://leetcode.com/problems/n-queens-ii/

class Solution:
    def totalNQueens(self, n: int) -> int:
        cols, pos_diags, neg_diags = set(), set(), set()
        self.arrangements = 0
        
        def getArrangements(row):
            if row == n:
                self.arrangements += 1
                
            for col in range(n):
                if col in cols or row + col in pos_diags or row - col in neg_diags:
                    continue
                    
                cols.add(col)
                pos_diags.add(row + col)
                neg_diags.add(row - col)
                
                getArrangements(row + 1)
                
                cols.remove(col)
                pos_diags.remove(row + col)
                neg_diags.remove(row - col)
                
        getArrangements(0)
        return self.arrangements
    
