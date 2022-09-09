# https://leetcode.com/problems/maximum-length-of-pair-chain/

class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        chain = [inf]
        
        for s, e in sorted(pairs):
            if e < chain[-1]:
                chain[-1] = e
            elif s > chain[-1]:
                chain.append(e)
                
        return len(chain)
    
