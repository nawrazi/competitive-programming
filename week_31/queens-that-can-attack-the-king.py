# https://leetcode.com/problems/queens-that-can-attack-the-king/

class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        directions = [(0,1), (0,-1), (1,0), (-1,0), (1,1), (1,-1), (-1,-1), (-1,1)]
        inBound = lambda r, c : 0 <= r < 8 and 0 <= c < 8
        unsafe = { (r, c) for r, c in queens }
        ans = []
        
        for x, y in directions:
            r, c = king
            while inBound(r, c):
                if (r, c) in unsafe:
                    ans.append([r, c])
                    break
                r += x
                c += y
                
        return ans
    
