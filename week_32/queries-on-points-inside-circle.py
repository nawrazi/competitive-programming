# https://leetcode.com/problems/queries-on-number-of-points-inside-a-circle/

class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        answer = []
        
        for cx, cy, r in queries:
            inside = 0
            for x, y in points:
                if ((cx - x) ** 2 + (cy - y) ** 2) ** 0.5 <= r:
                    inside += 1
            answer.append(inside)
            
        return answer
    
