# https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/

class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        swaps = [[0, 1], [1, 0]]
        
        for j, target in enumerate([tops[0], bottoms[0]]):
            for i in range(1, len(tops)):
                if tops[i] == target or swaps[0][j] == inf:
                    pass
                elif bottoms[i] == target:
                    swaps[0][j] += 1
                else:
                    swaps[0][j] = inf
                    
            for i in range(1, len(bottoms)):
                if bottoms[i] == target or swaps[1][j] == inf:
                    pass
                elif tops[i] == target:
                    swaps[1][j] += 1
                else:
                    swaps[1][j] = inf
                    
        min_swaps = inf
        for pos, neg in swaps:
            min_swaps = min(min_swaps, pos, neg)
            
        return min_swaps if min_swaps != inf else -1
    
