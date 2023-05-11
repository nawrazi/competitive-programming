# https://leetcode.com/problems/delete-operation-for-two-strings/

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        @cache
        def count(idx1, idx2):
            if idx1 >= len(word1):
                return len(word2) - idx2
            
            if idx2 >= len(word2):
                return len(word1) - idx1
            
            if word1[idx1] == word2[idx2]:
                return count(idx1 + 1, idx2 + 1)
            
            return 1 + min(count(idx1 + 1, idx2), count(idx1, idx2 + 1))
        
        return count(0, 0)
    
