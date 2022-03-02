# https://leetcode.com/problems/surrounded-regions/submissions/

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
            if board[row][0]=='O' and (row,0) not in safe:
                save(row,0)
            if board[row][len(board[0])-1]=='O' and (row,len(board[0])-1) not in safe:
                save(row,len(board[0])-1)

        for col in range(len(board[0])):
            if board[0][col]=='O' and (0,col) not in safe:
                save(0,col)
            if board[len(board)-1][col]=='O' and (len(board)-1,col) not in safe:
                save(len(board)-1,col)

        captureUnsaved()
