# https://leetcode.com/problems/longest-palindromic-subsequence/

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        @cache
        def palindromeLength(left, right):
            if left > right:
                return 0
            if left == right:
                return 1
            
            if s[left] == s[right]:
                return 2 + palindromeLength(left + 1, right - 1)
            
            longest = palindromeLength(left + 1, right - 1)
            longest = max(longest, palindromeLength(left + 1, right))
            longest = max(longest, palindromeLength(left, right - 1))
            
            return longest
        
        return palindromeLength(0, len(s) - 1)
    
