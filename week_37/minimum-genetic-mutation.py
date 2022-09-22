# https://leetcode.com/problems/minimum-genetic-mutation/

class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        def getDiff(g1, g2):
            diff = 0
            for i in range(8):
                if g1[i] != g2[i]:
                    diff += 1
            return diff
        
        q = deque([(start, 0)])
        seen = {start}
        while q:
            gene, mut = q.popleft()
            
            if gene == end:
                return mut
            
            for nex in bank:
                if nex not in seen and getDiff(gene, nex) == 1:
                    q.append((nex, mut + 1))
                    seen.add(nex)
                    
        return -1
    
