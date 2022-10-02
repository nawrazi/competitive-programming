# https://leetcode.com/problems/escape-the-ghosts/

class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        distance = lambda x, y: abs(target[0] - x) + abs(target[1] - y)
        
        for x, y in ghosts:
            if distance(x, y) <= distance(0, 0):
                return False
            
        return True
    
