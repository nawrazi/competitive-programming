# https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/

class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        mods = {}
        pairs = 0
        
        for t in time:
            if t % 60 in mods:
                pairs += mods[t % 60]
            diff = (60 - (t % 60)) % 60
            mods[diff] = mods.get(diff, 0) + 1
            
        return pairs
    
