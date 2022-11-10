# https://leetcode.com/problems/max-points-on-a-line/

class Solution:
    def getSlope(self, x1, y1, x2, y2):
        if x1 == x2:
            return inf
        return (y2 - y1) / (x2 - x1)
    
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) == 1:
            return 1
        
        max_line = 0
        for x1, y1 in points:
            collinear = defaultdict(int)
            for x2, y2 in points:
                if (x1, y1) == (x2, y2):
                    continue
                slope = self.getSlope(x1, y1, x2, y2)
                collinear[slope] += 1
            max_line = max(max_line, 1 + max(collinear.values()))
            
        return max_line
    
