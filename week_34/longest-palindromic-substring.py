# https://leetcode.com/problems/longest-palindromic-substring/

class Solution:
    def longestPalindrome(self, s: str) -> str:
        def getPalindrome(idx, single):
            if single:
                i, j = idx - 1, idx + 1
                center = [s[idx]]
            else:
                i, j = idx - 1, idx + 2
                center = [s[idx], s[idx + 1]]
            side = []
                
            while i >= 0 and j < len(s) and s[i] == s[j]:
                side.append(s[i])
                i -= 1
                j += 1
            
            return list(reversed(side)) + center + side
        
        longest = ''
        for i in range(len(s)):
            cur = getPalindrome(i, True)
            if len(cur) > len(longest):
                longest = cur
                
            if i < len(s) - 1 and s[i] == s[i + 1]:
                cur = getPalindrome(i, False)
                if len(cur) > len(longest):
                    longest = cur
            
        return ''.join(longest)
    
