# https://leetcode.com/problems/pacific-atlantic-water-flow/

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        dirs = [[0,1], [1,0], [-1,0], [0,-1]]
        
        def search(row, col, ocean):
            q = deque([(row, col)])
            seen = set(q)
            
            while q:
                r, c = q.popleft()
                
                for x, y in dirs:
                    nr, nc = r + x, c + y
                    if nr >= m or nc >= n:
                        if ocean == 'a': return True
                        else: continue
                    if nr < 0 or nc < 0:
                        if ocean == 'p': return True
                        else: continue
                    if heights[r][c] < heights[nr][nc] or (nr, nc) in seen:
                        continue
                    q.append((nr, nc))
                    seen.add((nr, nc))
                    
            return False
        
        ans = []
        for r, row in enumerate(heights):
            for c, cell in enumerate(row):
                if search(r, c, 'a') and search(r, c, 'p'):
                    ans.append([r, c])
                    
        return ans
    
