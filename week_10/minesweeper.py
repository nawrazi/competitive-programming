# https://leetcode.com/problems/minesweeper/

class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        def sweep(row,col):
            seen.add((row,col))
            mine_counter = 0

            for x,y in directions:
                new_row = row + x
                new_col = col + y

                if inBound(new_row,new_col) and board[new_row][new_col] == 'M':
                    mine_counter += 1

            if mine_counter>0:
                board[row][col] = str(mine_counter)
                return
            else:
                board[row][col] = 'B'

            for x,y in directions:
                new_row = row + x
                new_col = col + y

                if not inBound(new_row,new_col) or (new_row,new_col) in seen:
                    continue

                elif board[new_row][new_col] == 'E':
                    seen.add((new_row,new_col))
                    sweep(new_row,new_col)


        seen = set()
        inBound = lambda r,c : 0<=r<len(board) and 0<=c<len(board[0])
        directions = [(-1,-1), (-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1)]
        row, col = click

        if board[row][col] == 'M':
            board[row][col] = 'X'
            return board

        if board[row][col] == 'E':
            sweep(row,col)

        return board
