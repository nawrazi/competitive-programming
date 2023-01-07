# https://leetcode.com/problems/adding-spaces-to-a-string/

class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        spaces.insert(0, 0)
        spaces.append(len(s))
        ans = []
        
        for i in range(1, len(spaces)):
            ans.append(s[spaces[i-1]:spaces[i]])
            
        return ' '.join(ans)
    
