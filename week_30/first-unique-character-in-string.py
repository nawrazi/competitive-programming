# https://leetcode.com/problems/first-unique-character-in-a-string/

class Solution:
    def firstUniqChar(self, s: str) -> int:
        q = deque([])
        unique = {}
        
        for i, c in enumerate(s):
            if c not in unique:
                unique[c] = True
                q.append((c, i))
            else:
                unique[c] = False
                
        while q and not unique[q[0][0]]:
            q.popleft()
            
        return q.popleft()[1] if q else -1
    
