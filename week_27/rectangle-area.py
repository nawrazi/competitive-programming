# https://leetcode.com/problems/rectangle-area/

class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        areaA = (ay2 - ay1) * (ax2 - ax1)
        areaB = (by2 - by1) * (bx2 - bx1)

        hor, ver = 0, 0
        if ax1 <= bx1 <= ax2:
            hor = min(ax2, bx2) - bx1   # b's left is inside a
        elif ax1 <= bx2 <= ax2:
            hor = bx2 - max(ax1, bx1)   # b's right is inside a
        elif bx2 >= ax2 and bx1 <= ax1:
            hor = ax2 - ax1             # b covers a horizontally
        elif ax2 >= bx2 and ax1 <= bx1:
            hor = bx2 - bx1             # a covers b horizontally
        
        if ay1 <= by2 <= ay2:
            ver = by2 - max(ay1, by1)   # b's top is inside a
        elif ay1 <= by1 <= ay2:
            ver = min(ay2, by2) - by1   # b's bottom is inside a
        elif by2 >= ay2 and by1 <= ay1:
            ver = ay2 - ay1             # b covers a vertically
        elif ay2 >= by2 and ay1 <= by1:
            ver = by2 - by1             # a covers b vertically
            
        return areaA + areaB - hor * ver
    
