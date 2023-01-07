# https://leetcode.com/problems/print-words-vertically/description/

class Solution:
    def printVertically(self, s: str) -> List[str]:
        words = s.split()
        size = len(max(words, key=len))
        result = []
        
        for i in range(size):
            cur = []
            for word in words:
                if i < len(word):
                    cur.append(word[i])
                else:
                    cur.append(' ')
                    
            while cur and cur[-1] == ' ':
                cur.pop()
                
            result.append(''.join(cur))
            
        return result
    
