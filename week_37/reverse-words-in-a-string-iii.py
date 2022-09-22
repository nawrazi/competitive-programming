# https://leetcode.com/problems/reverse-words-in-a-string-iii/

class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join([''.join(reversed(w)) for w in s.split()])
    
