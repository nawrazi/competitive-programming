# https://leetcode.com/problems/palindromic-substrings/

class Solution:
    def countSubstrings(self, s: str) -> int:
        def getPalindrome(idx, single):
            i, j = idx - 1, idx + 1
            center = [s[idx]]
            side = []
            
            if not single:
                center.append(s[j])
                j += 1
                
            while i >= 0 and j < len(s) and s[i] == s[j]:
                side.append(s[i])
                i -= 1
                j += 1
                
            return 2 * len(side) + len(center)
        
        subs = 0
        for i in range(len(s)):
            cur = getPalindrome(i, True)
            subs += (cur // 2) + 1
            
            if i < len(s) - 1 and s[i] == s[i + 1]:
                cur = getPalindrome(i, False)
                subs += cur // 2
                
        return subs
    
