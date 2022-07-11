# https://leetcode.com/problems/rabbits-in-forest/

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        total = 0
        seen = {}
        for ans in answers:
            if ans not in seen or ans == 0:
                total += ans + 1
                seen[ans] = ans
            else:
                seen[ans] -= 1
                if seen[ans] <= 0:
                    del seen[ans]
                
        return total
    
