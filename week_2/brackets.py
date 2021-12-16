# https://leetcode.com/problems/valid-parentheses/submissions/

class Solution:
    def isValid(self, s: str) -> bool:
        d = {'(':')', '{':'}', '[':']'}
        stack = []

        for b in s:
            if b in d.keys():
                stack.append(b)

            else:
                if not stack:
                    return False
                if b == d[stack[-1]]:
                    stack.pop()
                else:
                    return False

        if not stack:
            return True
