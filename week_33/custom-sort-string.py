# https://leetcode.com/problems/custom-sort-string/

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        count = Counter(s)
        final = ""
        
        for c in order:
            if c in count:
                final += c * count[c]
                del count[c]
                
        for c, i in count.items():
            final += c * i
            
        return final
    
