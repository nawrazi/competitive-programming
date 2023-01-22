# https://leetcode.com/problems/palindrome-partitioning-iii/description/

class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        def getPalindromes(l, r):
            swaps = 0
            while l >= 0 and r < len(s):
                if s[l] != s[r]:
                    swaps += 1
                palindromes[l].add((r, swaps))
                l -= 1
                r += 1
        
        palindromes = defaultdict(set)
        for i in range(len(s)):
            getPalindromes(i, i)
            getPalindromes(i, i + 1)
        
        @cache
        def minSwaps(start, parts):
            if start >= len(s):
                return 0, parts == k
            
            if parts >= k:
                return 0, False
            
            min_swaps = inf
            for end, swaps in palindromes[start]:
                nex_swaps, found = minSwaps(end + 1, parts + 1)
                if found:
                    min_swaps = min(swaps + nex_swaps, min_swaps)
            
            return min_swaps, min_swaps != inf
        
        return minSwaps(0, 0)[0]
    
