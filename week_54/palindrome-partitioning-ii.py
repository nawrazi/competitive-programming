# https://leetcode.com/problems/palindrome-partitioning-ii/description/

class Solution:
    def minCut(self, s: str) -> int:
        def getPalindromes(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                palindromes[l].add(r)
                l -= 1
                r += 1
        
        palindromes = defaultdict(set)
        for i in range(len(s)):
            getPalindromes(i, i)
            getPalindromes(i, i + 1)
        
        @cache
        def minCuts(start):
            if start >= len(s):
                return -1
            
            cuts = inf
            for end in palindromes[start]:
                cuts = min(cuts, 1 + minCuts(end + 1))
                
            return cuts
        
        return minCuts(0)
    
