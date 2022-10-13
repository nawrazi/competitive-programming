# https://leetcode.com/problems/destroying-asteroids/

class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        for asteroid in sorted(asteroids):
            if mass < asteroid:
                return False
            mass += asteroid
            
        return True
    
