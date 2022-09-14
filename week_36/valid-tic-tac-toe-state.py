# https://leetcode.com/problems/valid-tic-tac-toe-state/

class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        x, o = 0, 0
        xw, ow = False, False
        
        diags = {
            board[0][0] + board[1][1] + board[2][2],
            board[2][0] + board[1][1] + board[0][2]
        }
        
        for i, row in enumerate(board):
            col = [row[i] for row in board]
            
            xw = xw or row.count('X') == 3 or col.count('X') == 3 or 'XXX' in diags
            ow = ow or row.count('O') == 3 or col.count('O') == 3 or 'OOO' in diags
            x += row.count('X')
            o += row.count('O')
        
        if xw:
            return x - o == 1 and not ow
        if ow:
            return x == o
        
        return x - o in {0, 1}
    
