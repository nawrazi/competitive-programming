# https://leetcode.com/problems/shifting-letters-ii/

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        prefix = [0 for _ in range(len(s) + 1)]
        
        for start, end, shift in shifts:
            prefix[start] += 1 if shift else -1
            prefix[end + 1] += -1 if shift else 1
            
        ans = []
        shift = 0
        for i, c in enumerate(s):
            shift += prefix[i]
            asc = ((ord(c) - ord('a')) + shift) % 26
            ans.append(chr(asc + ord('a')))
            
        return ''.join(ans)
    
