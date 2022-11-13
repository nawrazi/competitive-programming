# https://leetcode.com/problems/maximum-number-of-non-overlapping-palindrome-substrings/

class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        def getPalindrome(idx, single):
            i, j = idx - 1, idx + 1
            length = 1
            
            if not single:
                length += 1
                j += 1
                
            while i >= 0 and j < len(s) and s[i] == s[j]:
                length += 2
                i -= 1
                j += 1
                
            return length
        
        palindromes = []
        for i in range(len(s)):
            length = getPalindrome(i, True)
            if length >= k:
                palindromes.append([i - (k // 2), i + (k // 2)])
                
            if k > 1 and i < len(s) - 1 and s[i] == s[i + 1]:
                length = getPalindrome(i, False)
                if length >= k:
                    palindromes.append([i - ((k // 2) - 1), i + (k // 2)])
                    
        last = -inf
        total = 0
        for start, end in sorted(palindromes, key = lambda p: p[1]):
            if start > last: 
                last = end
                total += 1
                
        return total
    
