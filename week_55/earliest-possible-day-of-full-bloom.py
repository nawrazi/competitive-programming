# https://leetcode.com/problems/earliest-possible-day-of-full-bloom/

class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        plants = reversed(sorted(zip(growTime, plantTime)))
        finish = 0
        start = 0
        
        for grow, plant in plants:
            start += plant
            finish = max(finish, start + grow)
            
        return finish
    
