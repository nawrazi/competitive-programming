# https://leetcode.com/problems/minimum-jumps-to-reach-home/

class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        forb = set(forbidden)
        q = deque([(0, False, 0)])
        seen = {(0, False)}
        
        while q:
            pos, last_back, dist = q.popleft()
            
            if pos == x:
                return dist
            
            directions = [(pos + a, False)]
            if not last_back:
                directions.append((pos - b, True))
                
            for nex in directions:
                nex_pos, nex_back = nex
                if nex in seen or nex_pos in forb or not 0 <= nex_pos < 6000:
                    continue
                q.append((nex_pos, nex_back, dist + 1))
                seen.add((nex_pos, nex_back))
                
        return -1
    
