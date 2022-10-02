# https://leetcode.com/problems/freedom-trail/

class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        index = defaultdict(list)
        for i, c in enumerate(ring):
            index[c].append(i)
            
        @cache
        def getDistance(center, target):
            if target >= len(key):
                return 0
            
            dist = inf
            for pos in index[key[target]]:
                mn, mx = min(pos, center), max(pos, center)
                trav = min(abs(pos - center), (len(ring) - mx) + mn)
                dist = min(dist, trav + getDistance(pos, target + 1))
                
            return dist + 1
        
        return getDistance(0, 0)
    
