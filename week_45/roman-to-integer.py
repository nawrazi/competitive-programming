# https://leetcode.com/problems/roman-to-integer/

class Solution:
    def romanToInt(self, s: str) -> int:
        numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        prev = inf
        integer = 0
        
        for i, roman in enumerate(s):
            if numerals[roman] > prev:
                integer -= 2 * numerals[s[i - 1]]
            integer += numerals[roman]
            prev = numerals[roman]

        return integer
    
