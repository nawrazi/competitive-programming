# https://leetcode.com/problems/path-with-minimum-effort/

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        inBound = lambda r, c : 0 <= r < len(heights) and 0 <= c < len(heights[0])
        bottomRight = lambda r, c : (r, c) == (len(heights) - 1, len(heights[-1]) - 1)
        seen = defaultdict(int)
        seen[(0, 0)] = 0
        
        heap = [(0, 0, 0)]
        while heap:
            cur_effort, row, col = heappop(heap)
            
            if bottomRight(row, col):
                return cur_effort
            
            for x, y in directions:
                nrow, ncol = row + x, col + y
                if inBound(nrow, ncol):
                    effort = abs(heights[nrow][ncol] - heights[row][col])
                    nex_effort = max(cur_effort, effort)
                    if (nrow, ncol) not in seen or nex_effort < seen[(nrow, ncol)]:
                        seen[(nrow, ncol)] = nex_effort
                        heappush(heap, (nex_effort, nrow, ncol))
                        
