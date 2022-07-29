# https://leetcode.com/problems/find-and-replace-pattern/

class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        matches = []
        
        for word in words:
            match = True
            w_to_p = {}
            p_to_w = {}
            
            for i in range(len(word)):
                if word[i] in w_to_p and pattern[i] in p_to_w:
                    if w_to_p[word[i]] != pattern[i]:
                        match = False
                    if p_to_w[pattern[i]] != word[i]:
                        match = False
                elif word[i] not in w_to_p and pattern[i] not in p_to_w:
                    w_to_p[word[i]] = pattern[i]
                    p_to_w[pattern[i]] = word[i]
                else:
                    match = False
                    
                if not match:
                    break
                    
            if match:
                matches.append(word)
            
        return matches
    
