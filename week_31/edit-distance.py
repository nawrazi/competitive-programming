# https://leetcode.com/problems/edit-distance/

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        @cache
        def edit(cur1, cur2):
            if cur1 >= len(word1) or cur2 >= len(word2):
                return max(len(word1) - cur1, len(word2) - cur2)
            
            if word1[cur1] == word2[cur2]:
                return edit(cur1 + 1, cur2 + 1)
            
            return min(edit(cur1, cur2 + 1), edit(cur1 + 1, cur2), edit(cur1 + 1, cur2 + 1)) + 1
        
        return edit(0, 0)
    
