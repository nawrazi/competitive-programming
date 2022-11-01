# https://leetcode.com/problems/battleships-in-a-board/

class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        ships = 0
        
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == '.':
                    continue
                if row >= 1 and board[row - 1][col] == 'X':
                    continue
                if col >= 1 and board[row][col - 1] == 'X':
                    continue
                ships += 1
                
        return ships
    
