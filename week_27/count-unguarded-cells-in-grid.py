# https://leetcode.com/problems/count-unguarded-cells-in-the-grid/

class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        def search(row, col):
            for x, y in [(1,0), (0,1), (-1,0), (0,-1)]:
                r, c = row, col
                while inBound(r+x, c+y) and (r+x, c+y) not in obs:
                    seen.add((r+x, c+y))
                    r += x
                    c += y
             
        inBound = lambda r, c : 0 <= r < m and 0 <= c < n
        guards = [(r, c) for r, c in guards]
        walls = [(r, c) for r, c in walls]
        obs = set(guards + walls)
        seen = set()
        for r, c in guards:
            search(r, c)
        
        return (m * n) - len(obs) - len(seen)
    
