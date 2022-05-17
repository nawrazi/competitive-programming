# https://leetcode.com/problems/hamming-distance/

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        dist = 0
        for i in range(32):
            xbit = 1 if x & 1 << i else 0
            ybit = 1 if y & 1 << i else 0
            
            if xbit != ybit:
                dist += 1
                
        return dist
    
