# https://leetcode.com/problems/snakes-and-ladders/description/

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        move = [i for i in range(n ** 2 + 1)]
        if n % 2 == 0:
            cur = n ** 2
            right = -1
        else:
            cur = (n ** 2) - n + 1
            right = 1
            
        for row in range(n):
            for col in range(n):
                if board[row][col] != -1:
                    move[cur] = board[row][col]
                cur += right
            cur -= (n + right)
            right *= -1
            
        queue = deque([(move[1], 0)])
        seen = {move[1]}
        
        while queue:
            cell, moves = queue.popleft()
            if cell == n ** 2:
                return moves
            
            for i in range(1, 7):
                if cell + i > n ** 2:
                    continue
                nex = move[cell + i]
                if nex not in seen:
                    queue.append((nex, moves + 1))
                    seen.add(nex)
                    
        return -1
    
