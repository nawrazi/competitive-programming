# https://leetcode.com/problems/minimum-window-substring/

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        lets = Counter(t)
        wind = defaultdict(int)
        unq = 0
        l, r = 0, 0
        ans = ''
        
        while r < len(s):
            if s[r] in lets:
                wind[s[r]] += 1
                if wind[s[r]] == lets[s[r]]:
                    unq += 1
                    
            while l <= r and unq == len(lets):
                if not ans or r - l + 1 < len(ans):
                    ans = s[l:r+1]
                    
                if s[l] in wind:
                    wind[s[l]] -= 1
                    if wind[s[l]] < lets[s[l]]:
                        unq -= 1
                l += 1
                
            r += 1
            
        return ans
    
