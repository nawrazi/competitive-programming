# https://leetcode.com/problems/push-dominoes/

class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        q = deque()
        final = []
        for i, d in enumerate(dominoes):
            if d == 'L':
                q.append((i, -1, 0))
            elif d == 'R':
                q.append((i, 1, 0))
            final.append((0, 0))
            
        while q:
            pos, drn, lvl = q.popleft()
            
            if final[pos][0] == 0 or lvl == final[pos][1]:
                final[pos] = (final[pos][0] + drn, lvl)
            else:
                continue
                
            if 0 <= pos + drn < len(final):
                q.append((pos + drn, drn, lvl + 1))
                
        ans = []
        for d, _ in final:
            if d == 0:
                ans.append('.')
            elif d < 0:
                ans.append('L')
            else:
                ans.append('R')
                
        return ''.join(ans)
    
