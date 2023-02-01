# https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/description/

class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        blocks += 'B'
        window = blocks[:k].count('W')
        left, right = 0, k
        recolors = window
        
        while right < len(blocks):
            recolors = min(recolors, window)
            window += int(blocks[right] == 'W')
            window -= int(blocks[left] == 'W')
            left += 1
            right += 1
            
        return recolors
    
