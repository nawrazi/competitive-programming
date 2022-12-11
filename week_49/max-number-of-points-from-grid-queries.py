# https://leetcode.com/problems/maximum-number-of-points-from-grid-queries/description/

class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        inBound = lambda r, c : 0 <= r < len(grid) and 0 <= c < len(grid[0])
        heap = [(grid[0][0], 0, 0)]
        visited = {(0, 0)}
        
        def collect(limit):
            points = 0
            
            while heap:
                val, row, col = heappop(heap)
                if val >= limit:
                    heappush(heap, (val, row, col))
                    break
                points += 1
                
                for x, y in directions:
                    r, c = row + x, col + y
                    if inBound(r, c) and (r, c) not in visited:
                        heappush(heap, (grid[r][c], r, c))
                        visited.add((r, c))
                        
            return points
        
        queries = sorted((q, i) for i, q in enumerate(queries))
        result = [0 for _ in queries]
        prev = 0
        
        for query, idx in queries:
            if query > grid[0][0]:
                result[idx] = collect(query) + prev
                prev = result[idx]
                
        return result
    
