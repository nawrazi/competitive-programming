# https://leetcode.com/problems/find-players-with-zero-or-one-losses/

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        losses = defaultdict(int)
        
        for winner, loser in matches:
            losses[winner] += 0
            losses[loser] += 1
            
        return [
            sorted([k for k, v in losses.items() if v == 0]),
            sorted([k for k, v in losses.items() if v == 1])
        ]
    
