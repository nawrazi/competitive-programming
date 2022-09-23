# https://leetcode.com/problems/detonate-the-maximum-bombs/

class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        graph = defaultdict(list)
        for i, (x1, y1, r1) in enumerate(bombs):
            for j, (x2, y2, r2) in enumerate(bombs):
                if i != j and ((x1 - x2) ** 2) + ((y1 - y2) ** 2) <= r1 ** 2:
                    graph[(x1, y1)].append((j, x2, y2))
                    
        def search(i, x, y):
            seen.add(i)
            det.add(i)
            area = 1
            for ni, nx, ny in graph[(x, y)]:
                if ni not in seen:
                    area += search(ni, nx, ny)
            return area
        
        ans = 0
        det = set()
        for i, (x, y, _) in enumerate(bombs):
            seen = set()
            if i not in det:
                ans = max(ans, search(i, x, y))
            
        return ans
    
