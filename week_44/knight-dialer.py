# https://leetcode.com/problems/knight-dialer/

class Solution:
    def knightDialer(self, n: int) -> int:
        mod = (10 ** 9) + 7
        phone = [[1,2,3], [4,5,6], [7,8,9], [-1,0,-1]]
        directions = [(-2,-1), (-1,-2), (-1,2), (-2,1), (1,2), (2,1), (1,-2), (2,-1)]
        
        @cache
        def getWays(row, col, moves):
            if moves == n:
                return 1
            
            ways = 0
            for x, y in directions:
                nr, nc = row + x, col + y
                if 0 <= nr < 4 and 0 <= nc < 3 and phone[nr][nc] >= 0:
                    ways = (ways + getWays(nr, nc, moves + 1)) % mod
                    
            return ways
        
        ways = 0
        for row in range(4):
            for col in range(3):
                if phone[row][col] >= 0:
                    ways = (ways + getWays(row, col, 1)) % mod
        
        return ways % mod
    
