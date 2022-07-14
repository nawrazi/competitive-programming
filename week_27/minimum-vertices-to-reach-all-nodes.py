# https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes/

class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        hasIn = set()
        m = 0
        for s, e in edges:
            hasIn.add(e)
            m = max(m, s, e)
            
        return [n for n in range(m + 1) if n not in hasIn]
    
