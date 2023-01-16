# https://leetcode.com/problems/letter-tile-possibilities/description/

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        ways = set()
        seen = set()
        cur = []
        
        def backtrack():
            ways.add(''.join(cur))
            
            for nex in range(len(tiles)):
                if nex not in seen:
                    seen.add(nex)
                    cur.append(tiles[nex])
                    backtrack()
                    seen.remove(nex)
                    cur.pop()
                    
        backtrack()
        return len(ways) - 1
    
