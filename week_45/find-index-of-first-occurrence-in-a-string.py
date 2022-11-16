# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)
        haystack += ' '
        prime = 31
        mod = (10 ** 9) + 7
        mod_inv = pow(prime, -1, mod)
        
        size = len(needle)
        left, right = 0, size
        value = lambda char: ord(char) - ord('a') + 1
        
        target = 0
        for i, c in enumerate(needle):
            target = (target +  (value(c) * pow(prime, i , mod)) % mod) % mod
            
        window = 0
        for i, c in enumerate(haystack[:right]):
            window = (window + (value(c) * pow(prime, i , mod)) % mod) % mod
            
        while right < len(haystack):
            if window == target and needle == haystack[left:right]:
                return left
            
            window = (window - value(haystack[left])) % mod
            window = (window * mod_inv) % mod
            window = (window + (value(haystack[right]) * pow(prime, size- 1, mod)) % mod) % mod
            
            left += 1
            right += 1
            
        return -1
    
