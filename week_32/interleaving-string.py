# https://leetcode.com/problems/interleaving-string/

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        @cache
        def getInterleaving(idx1, idx2, idx3):
            if idx3 == len(s3):
                return idx1 == len(s1) and idx2 == len(s2)
            
            if idx1 == len(s1) and idx2 == len(s2):
                return False
            
            found = False
            if idx1 < len(s1) and s1[idx1] == s3[idx3]:
                found = found or getInterleaving(idx1 + 1, idx2, idx3 + 1)
            
            if not found and idx2 < len(s2) and s2[idx2] == s3[idx3]:
                found = found or getInterleaving(idx1, idx2 + 1, idx3 + 1)
                
            return found
        
        return getInterleaving(0, 0, 0)
    
