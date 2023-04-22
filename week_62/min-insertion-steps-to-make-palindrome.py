# https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/

class Solution:
    def minInsertions(self, s: str) -> int:
        @cache
        def count(left, right):
            if left >= right:
                return 0
            
            if s[left] == s[right]:
                return count(left + 1, right - 1)
            
            return 1 + min(count(left + 1, right), count(left, right - 1))
        
        return count(0, len(s) - 1)
    
