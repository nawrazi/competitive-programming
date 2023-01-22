# https://leetcode.com/problems/palindrome-partitioning-iv/description/

class Solution:
    def checkPartitioning(self, s: str) -> bool:
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
        def canPartition(start, cuts):
            if start >= len(s):
                return cuts == 3
              
            if cuts >= 3:
                return False
            
            for end in palindromes[start]:
                if canPartition(end + 1, cuts + 1):
                    return True
        
        return canPartition(0, 0)
    
