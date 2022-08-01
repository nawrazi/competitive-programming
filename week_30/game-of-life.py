# https://leetcode.com/problems/game-of-life/

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        alive = {(r, c): board[r][c] for r in range(len(board)) for c in range(len(board[r]))}
        directions = [(1,0), (0,1), (-1,0), (0,-1), (1,1), (-1,-1), (1,-1), (-1,1)]
        inBound = lambda r, c : 0 <= r < len(board) and 0 <= c < len(board[r])
        
        def neighbors(row, col):
            count = 0
            for x, y in directions:
                r, c = row + x, col + y
                if inBound(r, c) and alive[(r, c)]:
                    count += 1
            return count
        
        for row in range(len(board)):
            for col in range(len(board[row])):
                ones = neighbors(row, col)
                if board[row][col] == 1 and ones <= 1:
                    board[row][col] = 0
                elif board[row][col] == 1 and ones >= 4:
                    board[row][col] = 0
                elif board[row][col] == 0 and ones == 3:
                    board[row][col] = 1
        
