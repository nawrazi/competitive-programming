# https://leetcode.com/problems/evaluate-reverse-polish-notation/

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]

        for token in tokens:
            if token=='+':
                val = stack[-2] + stack[-1]
                stack.pop()
                stack[-1]=val

            elif token=='-':
                val = stack[-2] - stack[-1]
                stack.pop()
                stack[-1]=val

            elif token=='*':
                val = stack[-2] * stack[-1]
                stack.pop()
                stack[-1]=val

            elif token=='/':
                val = stack[-2] / stack[-1]
                val = math.trunc(val)
                stack.pop()
                stack[-1]=val

            else:
                stack.append(int(token))

        return stack[0]
