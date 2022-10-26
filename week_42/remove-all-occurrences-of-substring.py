# https://leetcode.com/problems/remove-all-occurrences-of-a-substring/

class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        part = list(part)
        stack = []
        for char in s:
            stack.append(char)
            if stack[-len(part):] == part:
                for _ in range(len(part)):
                    stack.pop()
                    
        return ''.join(stack)
    
