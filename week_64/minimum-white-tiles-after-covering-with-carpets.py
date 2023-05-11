# https://leetcode.com/problems/minimum-white-tiles-after-covering-with-carpets/

class Solution:
    def minimumWhiteTiles(self, floor: str, numCarpets: int, carpetLen: int) -> int:
        whitesAfter = list(accumulate((map(int, floor[::-1]))))[::-1]
        
        @cache
        def count(tile, carpets):
            if tile >= len(floor):
                return 0
            
            if carpets == numCarpets:
                return whitesAfter[tile]
            
            use = count(tile + carpetLen, carpets + 1)
            dont = int(floor[tile]) + count(tile + 1, carpets)
            
            return min(use, dont)
        
        return count(0, 0)
    
