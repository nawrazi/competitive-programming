# https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/description/

class Solution:
    def smallestSubsequence(self, s: str) -> str:
        stack = []
        added = set()
        count = Counter(s)
        
        for letter in s:
            if letter not in added:
                while stack and letter < stack[-1] and count[stack[-1]] > 0:
                    top = stack.pop()
                    added.remove(top)
                    
                stack.append(letter)
                added.add(letter)
                
            count[letter] -= 1
            
        return ''.join(stack)
    
