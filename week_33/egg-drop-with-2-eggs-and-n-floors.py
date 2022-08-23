# https://leetcode.com/problems/egg-drop-with-2-eggs-and-n-floors/

class Solution:
    def twoEggDrop(self, n: int) -> int:
        diff = 1
        while n > 0:
            n -= diff
            diff += 1
            
        return diff - 1
    
