# https://leetcode.com/problems/surrounded-regions/

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        def save(row,col):
            safe.add((row,col))

            for x,y in directions:
                new_row = row+x
                new_col = col+y

                if inBound(new_row,new_col) and board[new_row][new_col]=='O' and (new_row,new_col) not in safe:
                    save(new_row,new_col)


        def captureUnsaved():
            for row in range(len(board)):
                for col in range(len(board[0])):
                    if board[row][col]=='O' and (row,col) not in safe:
                        board[row][col] = 'X'


        safe = set()
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        inBound = lambda r,c : 0<=r<len(board) and 0<=c<len(board[0])

        for row in range(len(board)):
            for col in (0,len(board[0])-1):
                if board[row][col]=='O' and (row,col) not in safe:
                    save(row,col)

        for col in range(len(board[0])):
            for row in (0,len(board)-1):
                if board[row][col]=='O' and (row,col) not in safe:
                    save(row,col)

        captureUnsaved()
