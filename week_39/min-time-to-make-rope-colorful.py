# https://leetcode.com/problems/minimum-time-to-make-rope-colorful/

class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        similar = []
        cur = colors[0]
        indexes = []
        for i, color in enumerate(colors + ' '):
            if color != cur:
                if len(indexes) > 1:
                    similar.append(indexes[:])
                cur = color
                indexes = []
            indexes.append(i)
            
        total = 0
        for sim in similar:
            time = 0
            longest = 0
            for i in range(sim[0], sim[-1] + 1):
                time += neededTime[i]
                longest = max(longest, neededTime[i])
            total += (time - longest)
            
        return total
    
