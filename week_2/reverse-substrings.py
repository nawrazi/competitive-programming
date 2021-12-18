class Solution:
    def myStack(self, s2: str) -> str:
        stack = []
        l = 0
        i=0

        while i < len(s2):
            if s2[i]=='(':
                val,l = self.myStack(s2[i+1:])
                stack += val
                i+=l
                l+=2

            elif s2[i]==')':
                # l+=1
                return stack[::-1], l+2

            else:
                stack.append(s2[i])
                l+=1
                i+=1


    def reverseParentheses(self, s: str) -> str:
        stack2 = []
        i=0
        while i < len(s):
            if s[i]=='(':
                val,l = self.myStack(s[i+1:])
                stack2 += val
                print(stack2)
                i+=l
                continue

            stack2.append(s[i])
            i+=1

        return ''.join(stack2)
