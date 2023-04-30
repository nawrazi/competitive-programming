# https://leetcode.com/problems/sliding-puzzle/

class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        def toTuple(board):
            return tuple(map(tuple, board))
        
        def toList(board):
            return (list(map(list, board)))
        
        def findZero(board):
            if 0 in board[0]:
                return 0, board[0].index(0)
            return 1, board[1].index(0)
        
        queue = deque([(toTuple(board), 0)])
        seen = set([toTuple(board)])
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        inBound = lambda r, c: 0 <= r < 2 and 0 <= c < 3
        solved = ((1,2,3), (4,5,0))
        
        while queue:
            board, moves = queue.popleft()
            
            if board == solved:
                return moves
            
            row, col = findZero(board)
            for x, y in directions:
                nr, nc = row + x, col + y
                if not inBound(nr, nc):
                    continue
                new_board = toList(board)
                new_board[row][col] = new_board[nr][nc]
                new_board[nr][nc] = 0
                tup = toTuple(new_board)
                
                if tup not in seen:
                    queue.append((tup, moves + 1))
                    seen.add(tup)
                    
        return -1
    
