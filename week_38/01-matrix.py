# https://leetcode.com/problems/01-matrix/

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        inBound = lambda r, c: 0 <= r < m and 0 <= c < n
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        
        ans = [[-1] * n for _ in range(m)]
        h = []
        seen = set()
        for r, row in enumerate(mat):
            for c, cell in enumerate(row):
                if cell == 0:
                    heappush(h, (0, r, c))
                    seen.add((r, c))
        
        while h:
            lev, row, col = heappop(h)
            
            if ans[row][col] == -1:
                ans[row][col] = lev
                
            for x, y in directions:
                r, c = row + x, col + y
                if (r, c) not in seen and inBound(r, c):
                    heappush(h, (lev + 1, r, c))
                    seen.add((r, c))
                    
        return ans
    
