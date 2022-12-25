# https://leetcode.com/problems/count-anagrams/description/

class Solution:
    def countAnagrams(self, s: str) -> int:
        words = [(len(word), Counter(word).values()) for word in s.split()]
        mod = pow(10, 9) + 7
        anagrams = 1
        
        for length, counts in words:
            ways = factorial(length)
            for count in counts:
                ways //= factorial(count)
                
            anagrams *= ways
            
        return anagrams % mod
    
