# https://leetcode.com/problems/detect-squares/description/

class DetectSquares:

    def __init__(self):
        self.x_axis = defaultdict(list)
        self.y_axis = defaultdict(list)
        self.points = defaultdict(int)
        
    def add(self, point: List[int]) -> None:
        x, y = point
        self.x_axis[x].append((x, y))
        self.y_axis[y].append((x, y))
        self.points[(x, y)] += 1
        
    def count(self, point: List[int]) -> int:
        x1, y1 = point
        squares = 0
        
        for x2, y2 in self.x_axis[x1]:
            side = abs(y2 - y1)
            
            if side == 0:
                continue
                
            if (x1 + side, y1) in self.points and (x2 + side, y2) in self.points:
                squares += self.points[(x1 + side, y1)] * self.points[(x2 + side, y2)]
                
            if (x1 - side, y1) in self.points and (x2 - side, y2) in self.points:
                squares += self.points[(x1 - side, y1)] * self.points[(x2 - side, y2)]
                
        return squares
    
