# https://leetcode.com/problems/simplify-path/

class Solution:
    def simplifyPath(self, path: str) -> str:
        simple = []
        
        for d in path.split('/'):
            if d in ['', '.']:
                continue
            if d == '..':
                if simple: simple.pop()
            else:
                simple.append(d)
                
        return '/' + '/'.join(simple)
    
