# https://leetcode.com/problems/word-search/

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = ((1,0), (-1,0), (0,1), (0,-1))
        inBound = lambda r, c: 0 <= r < len(board) and 0 <= c < len(board[r])
        
        def search(row, col, idx):
            if word[idx] != board[row][col]:
                return False
            
            if idx == len(word) - 1:
                return True
            
            for x, y in directions:
                r, c = row + x, col + y
                if not inBound(r, c) or (r, c) in seen:
                    continue
                seen.add((r, c))
                if search(r, c, idx + 1):
                    return True
                seen.remove((r, c))
                
            return False
        
        wordCount = Counter(word)
        boardCount = Counter()
        for row in board:
            boardCount += Counter(row)
            
        for c, count in wordCount.items():
            if c not in boardCount or count > boardCount[c]:
                return False
        
        for r in range(len(board)):
            for c in range(len(board[r])):
                seen = {(r, c)}
                if board[r][c] == word[0] and search(r, c, 0):
                    return True
                
        return False
    
