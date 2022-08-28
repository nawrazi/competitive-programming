# https://leetcode.com/problems/integer-to-roman/

class Solution:
    def intToRoman(self, num: int) -> str:
        roman = {
            1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L',
            90: 'XC', 100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'
        }
        
        ans = ''
        keys = sorted(roman.keys())
        cur = len(keys) - 1
        while num > 0:
            if num >= keys[cur]:
                ans += roman[keys[cur]] * (num // keys[cur])
                num %= keys[cur]
            cur -= 1
            
        return ans
    
