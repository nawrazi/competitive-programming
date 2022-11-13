# https://leetcode.com/problems/maximum-number-of-non-overlapping-palindrome-substrings/

class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        if k == 1:
            return len(s)
        
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
        
        pals = []
        for i in range(len(s)):
            length = getPalindrome(i, True)
            if length >= k:
                pals.append([i - (k // 2), i + (k // 2)])
                
            if i < len(s) - 1 and s[i] == s[i + 1]:
                length = getPalindrome(i, False)
                if length >= k:
                    pals.append([i - ((k // 2) - 1), i + (k // 2)])
                    
        last = -inf
        total = 0
        for start, end in sorted(pals, key = lambda p: p[1]):
            if start > last: 
                last = end
                total += 1
                
        return total
    
