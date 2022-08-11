# https://leetcode.com/problems/largest-combination-with-bitwise-and-greater-than-zero/

class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        counts = defaultdict(int)
        for num in candidates:
            mask = 1
            for _ in range(24):
                if num & mask != 0:
                    counts[mask] += 1
                mask <<= 1
                
        return max(counts.values())
    
