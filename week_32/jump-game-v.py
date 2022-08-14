# https://leetcode.com/problems/jump-game-v/

class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        inBound = lambda i: 0 <= i < len(arr)
        
        @cache
        def getVisits(idx):
            visits = 0
            for jump in range(1, d + 1):
                nex = idx + jump
                if not inBound(nex):
                    continue
                if arr[nex] >= arr[idx]:
                    break
                visits = max(visits, getVisits(nex))
                
            for jump in range(1, d + 1):
                jump = -jump
                nex = idx + jump
                if not inBound(nex):
                    continue
                if arr[nex] >= arr[idx]:
                    break
                visits = max(visits, getVisits(nex))
                
            return visits + 1
        
        visits = 0
        for i in range(len(arr)):
            visits = max(visits, getVisits(i))
            
        return visits
    
