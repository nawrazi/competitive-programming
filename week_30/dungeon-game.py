# https://leetcode.com/problems/dungeon-game/

class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        inBound = lambda r, c: 0 <= r < len(dungeon) and 0<= c < len(dungeon[r])
        heap = [(-dungeon[0][0], -dungeon[0][0], 0, 0)]
        best = {}
        
        while heap:
            health, min_health, row, col = heappop(heap)
            
            if row == len(dungeon) - 1 and col == len(dungeon[row]) - 1:
                return max(min_health, 0) + 1
            
            for x, y in [(1,0), (0,1)]:
                r, c = row + x, col + y
                if not inBound(r, c):
                    continue
                new_health = health + (-1 * dungeon[r][c])
                new_min = max(min_health, new_health)
                if (r, c) not in best or new_health < best[(r, c)]:
                    best[(r, c)] = new_health
                    heappush(heap, (new_health, new_min, r, c))
                    
