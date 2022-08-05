# https://leetcode.com/problems/shifting-letters/

class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        chars = []
        shift = 0
        for i in range(len(s) - 1, -1, -1):
            shift += shifts[i]
            c = ((ord(s[i]) - ord('a')) + shift) % 26
            chars.append(chr(c + ord('a')))
            
        return ''.join(reversed(chars))
    
