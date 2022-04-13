# https://leetcode.com/problems/validate-stack-sequences/

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        i, j = 0, 0

        while i < len(pushed):
            if stack and popped[j] == stack[-1]:
                stack.pop()
                j += 1

            elif pushed[i] != popped[j]:
                stack.append(pushed[i])
                i += 1

            elif pushed[i] == popped[j]:
                i += 1
                j += 1

        while stack:
            if stack.pop() != popped[j]:
                return False
            j += 1

        return True
