# https://leetcode.com/problems/check-if-word-is-valid-after-substitutions/

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for letter in s:
            if letter == 'c':
                if len(stack) > 1 and stack[-1] + stack[-2] == 'ba':
                    stack.pop()
                    stack.pop()
                    continue
                return False

            stack.append(letter)

        return not stack
