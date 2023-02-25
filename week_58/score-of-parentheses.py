# https://leetcode.com/problems/score-of-parentheses/description/

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]
        for c in s:
            if c == '(':
                stack.append(0)
            else:
                inner = stack.pop()
                stack[-1] += 2 * inner if inner else 1
                
        return stack.pop()
    
