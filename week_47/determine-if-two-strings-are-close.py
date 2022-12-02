# https://leetcode.com/problems/determine-if-two-strings-are-close/

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if set(word1) != set(word2):
            return False
        
        count1 = Counter(word1).values()
        count2 = Counter(word2).values()
        
        return Counter(count1) == Counter(count2)
    
