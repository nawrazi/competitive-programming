# https://leetcode.com/problems/valid-square/

class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        points = [p1, p2, p3, p4]
        sides, slopes = set(), set()
        
        for x1, y1 in points:
            for x2, y2 in points:
                if (x1, y1) == (x2, y2):
                    continue
                
                side = ((x1 - x2) ** 2) + ((y1 - y2) ** 2)
                sides.add(side)
                
                slope = (y2 - y1) / (x1 - x2) if x1 != x2 else inf
                slopes.add(slope)
                
        return len(sides) == 2 and len(slopes) == 4
    
